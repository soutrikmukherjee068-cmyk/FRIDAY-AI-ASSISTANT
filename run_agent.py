import os
import sys
import subprocess
from pathlib import Path


def run(cmd):
    print(">", " ".join(cmd))
    subprocess.check_call(cmd)


def ensure_env_file():
    env_path = Path(".env")
    if not env_path.exists():
        env_path.write_text(
            "GEMINI_API_KEY=PASTE_YOUR_GOOGLE_AI_STUDIO_API_KEY_HERE\n"
            "GEMINI_VOICE=Kore\n"
            "LAN=Hindi\n"
            "FRIDAY_VARIANT=Humanized\n"
            "USER_NAME=Boss\n",
            encoding="utf-8"
        )
        print("⚠️ .env created. Add your Gemini API key inside .env first.")
        sys.exit(1)


def ensure_requirements():
    req_path = Path("requirements.txt")
    if req_path.exists():
        run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        run([
            sys.executable,
            "-m",
            "pip",
            "install",
            "google-genai",
            "python-dotenv",
            "livekit-agents",
            "livekit-plugins-google",
            "livekit-plugins-noise-cancellation",
        ])


def main():
    ensure_env_file()
    ensure_requirements()

    mode = sys.argv[1] if len(sys.argv) > 1 else "console"

    print(f"🚀 Launching Friday (agent.py {mode}) ...")
    subprocess.run([sys.executable, "agent.py", mode])


if __name__ == "__main__":
    main()