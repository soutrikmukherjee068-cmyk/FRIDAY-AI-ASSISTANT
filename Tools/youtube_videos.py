from typing import Literal
import asyncio
import aiohttp
import webbrowser
import os
from dotenv import load_dotenv
from livekit.agents import function_tool
import logging

load_dotenv()
logger = logging.getLogger(__name__)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

@function_tool()
async def play_media(media_name: str, media_type: Literal["song", "video"] = "song") -> str:
    """
    Plays media content from YouTube.
    
    Args:
        media_name: Name of song/video
        media_type: Content type (default: "song")
        
    Behavior:
        - Uses YouTube Data API if key available
        - Falls back to browser search
        
    Returns:
        str: Currently playing confirmation or search link

    """
    try:
        print(f"🎵 Playing media: {media_name} (type: {media_type})")

        def open_url(url: str):
            """Open browser without blocking the async event loop."""
            webbrowser.open(url)

        if not YOUTUBE_API_KEY:
            # Fire-and-forget: open browser in background, return immediately
            asyncio.get_event_loop().run_in_executor(None, open_url,
                f"https://www.youtube.com/results?search_query={media_name}")
            return f"YouTube-এ '{media_name}' খুলে দিচ্ছি Boss।"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={media_name}&type=video&key={YOUTUBE_API_KEY}",
                    timeout=aiohttp.ClientTimeout(total=5)  # reduced from 10s to 5s
                ) as response:
                    data = await response.json()

            if data.get('items'):
                video = data['items'][0]
                url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                title = video['snippet']['title']
                # Fire-and-forget: don't wait for browser to finish loading
                asyncio.get_event_loop().run_in_executor(None, open_url, url)
                return f"🎵 চালু করছি Boss: {title}"

        except asyncio.TimeoutError:
            logger.warning("YouTube API timeout — falling back to search")

        # Fallback: open YouTube search without waiting
        asyncio.get_event_loop().run_in_executor(None, open_url,
            f"https://www.youtube.com/results?search_query={media_name}")
        return f"YouTube-এ '{media_name}' search করছি Boss।"

    except Exception as e:
        logger.error(f"Media error: {e}")
        return f"❌ '{media_name}' চালাতে সমস্যা হলো Boss: {str(e)}"
