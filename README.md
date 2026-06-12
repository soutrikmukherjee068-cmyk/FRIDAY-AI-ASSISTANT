<h1 align="center">
  <img src="https://img.shields.io/badge/FRIDAY-AI%20ASSISTANT-6c47ff?style=for-the-badge&logo=google&logoColor=white" alt="Friday AI Assistant"/>
</h1>

<p align="center">
  <b>🤖 Your Intelligent Personal Desktop AI — Powered by Google Gemini</b><br/>
  Voice-controlled · Real-time · 60+ Tools · Bengali + English
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange?style=flat-square&logo=google" />
  <img src="https://img.shields.io/badge/LiveKit-Realtime-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Language-Bengali-red?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" />
</p>

---

## 🌟 What is Friday?

**Friday** is a powerful voice-first AI desktop assistant built on **Google Gemini 2.5 Flash Native Audio** and the **LiveKit Agents framework**. Inspired by Tony Stark's iconic AI companion from Iron Man, Friday speaks natural **Bengali (চলিত ভাষা)** mixed with English — just like everyday conversation. She controls your entire PC, automates complex tasks, and feels like having a real assistant by your side — 24/7.

> 💬 *"হ্যাঁ Boss… Friday এখানে আছি।"* — Friday is always listening.

---

## ✨ Features at a Glance

| Category | Capabilities |
|----------|-------------|
| 🎙️ **Voice** | Real-time Bengali + English voice conversation via Gemini Native Audio |
| 🖥️ **Desktop Control** | Open apps, manage windows, scroll, type, click via OCR |
| 🌐 **Web & Search** | DuckDuckGo, Wikipedia, live weather, top news |
| 📱 **WhatsApp** | Send text messages & media via desktop automation |
| 🎵 **Media** | YouTube playback, Spotify control (play/pause/next/prev) |
| 📄 **Documents** | Read & query PDFs, Word docs, create & edit Excel files |
| 🤖 **AI Image Gen** | Generate AI images via Pollinations.ai (free, no key needed!) |
| 💻 **Code Assistant** | Generate & run code via Groq AI directly in VS Code |
| 🔔 **Reminders** | Smart reminder system with voice alerts |
| 📸 **Screen Vision** | Screenshot + live screen analysis with Gemini Vision |
| 🧠 **Code Fixer** | Automatically detect and fix code errors |
| 🔒 **System Power** | Shutdown, restart, lock your PC by voice |
| 📷 **Camera** | Live camera feed analysis |
| 🎛️ **Volume/Brightness** | Voice-controlled system audio and display settings |
| 📁 **File Management** | Search, open, convert files (PDF ↔ Word ↔ Excel ↔ Image) |
| 🛡️ **Virus Scan** | Quick system security scan via Windows Defender |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/soutrikmukherjee068-cmyk/FRIDAY-AI-ASSISTANT.git
cd FRIDAY-AI-ASSISTANT
```

### 2. Set Up Python Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

### 3. Configure Your API Keys

Create a `.env` file in the root directory:

```env
# ✅ REQUIRED
GEMINI_API_KEY=your_google_ai_studio_api_key_here

# 🎙️ Voice & language settings
GEMINI_VOICE=Kore
LAN=Bengali
MJ_VARIANT=Humanized
USER_NAME=Boss

# 📧 Email (optional)
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password_here

# 🎵 YouTube (optional — for direct video search)
YOUTUBE_API_KEY=your_youtube_data_api_key_here

# 🤖 Code generation & PDF Q&A (optional)
GROQ_API_KEY=your_groq_api_key_here

# 📡 LiveKit (required for cloud/production deployment)
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

> 🔑 **Get your free API keys:**
> - **Gemini** → [aistudio.google.com](https://aistudio.google.com)
> - **Groq** → [console.groq.com](https://console.groq.com)
> - **LiveKit** → [livekit.io](https://livekit.io)
> - **YouTube Data API** → [console.cloud.google.com](https://console.cloud.google.com)

### 4. Run Friday

```bash
# Simple launch (console mode)
python run_agent.py console

# Or directly
python agent.py console
```

---

## 🗂️ Project Structure

```
FRIDAY-AI-ASSISTANT/
│
├── agent.py              # 🧠 Main agent — LiveKit + Gemini setup
├── prompts_mj.py         # 📝 Friday's personality & system prompts
├── gemini_voice.py       # 🎙️ Gemini TTS voice helper
├── run_agent.py          # 🚀 Easy launch script
│
├── Tools/                # 🧰 Modular tool collection (60+ tools)
│   ├── camera_analysis.py
│   ├── code_generator.py
│   ├── code_handler.py
│   ├── create_folder.py
│   ├── desktop_control.py
│   ├── excel_data_entery.py
│   ├── file_searching.py
│   ├── generate_ai_image.py
│   ├── image_analysis.py
│   ├── manage_windows.py
│   ├── multi_task.py
│   ├── news_provider.py
│   ├── open_app.py
│   ├── pdf_reader.py
│   ├── press_key.py
│   ├── read_screen_text.py
│   ├── reminder.py
│   ├── scan_system_for_viruses.py
│   ├── screen_analyzer.py
│   ├── screen_short.py
│   ├── scroll_content.py
│   ├── search_web.py
│   ├── send_media_whatsapp.py
│   ├── send_whatsapp_message.py
│   ├── spotify.py
│   ├── system_power_action.py
│   ├── time_volume_bright.py
│   ├── type_user_message_auto.py
│   ├── word_to_pdf.py
│   ├── write_in_notepad.py
│   └── youtube_videos.py
│
├── requirements.txt      # 📦 Python dependencies
├── .env                  # 🔒 Your secrets (NOT committed to git)
├── .gitignore            # 🚫 Ignores .env, .venv, __pycache__
└── memory.json           # 🧠 Persistent conversation memory (NOT committed)
```

---

## 🧠 Architecture

```
User speaks (Bengali / English)
        │
        ▼
  LiveKit Room (WebRTC)
        │
        ▼
  AgentSession (min_endpointing_delay=0.4s)
        │
        ▼
  UltimateAdvancedNova Agent
        │
        ├──► Gemini 2.5 Flash Native Audio (LLM + Voice)
        │         │
        │    Friday's Personality Prompt
        │    (Bengali · Colloquial · Warm · Confident)
        │
        └──► 60+ Function Tools
              ├── System & Desktop
              ├── Web & Search
              ├── Media (YouTube, Spotify)
              ├── Communication (WhatsApp, Email)
              ├── Documents & Files
              ├── Code (Generate, Fix, Run)
              ├── Vision (Camera, Screen)
              └── Reminders & Automation
```

---

## ⚡ Performance Optimizations

Recent updates significantly reduced response latency:

| Optimization | What Changed | Gain |
|---|---|---|
| **Removed redundant tool docs** | `AGENT_INSTRUCTION_FOR_TOOLS` removed from system prompt — LLM already receives tool schemas directly | ~1–2s faster |
| **Trimmed chat history** | Only last 15 messages sent to model per session (full history still saved locally) | ~0.5–1s faster |
| **Faster VAD** | `min_endpointing_delay=0.4s` — Friday responds 400ms after you stop talking (was ~800ms) | ~0.4s faster |
| **Non-blocking media open** | YouTube/browser opens in background — Friday replies instantly without waiting for browser to load | ~5–10s faster |

---

## 💬 Example Voice Commands

```
"Friday, Rahul ke WhatsApp e message pathao — kal dekha hobe"
"Google e search karo AI news"
"System volume 60% kore dao"
"Screen er screenshot nao"
"Python e calculator banao ar VS Code e type kore dao"
"Spotify te Arijit Singh er gaan chalao"
"Delhi te weather kemon?"
"Excel e students er ekta table banao"
"PDF upload karo ar summary dao"
"Screen e ki dekhachhe?"
```

---

## 🛠️ Key Dependencies

| Package | Purpose |
|---------|---------|
| `livekit-agents` | Real-time agent framework |
| `livekit-plugins-google` | Gemini Native Audio model integration |
| `livekit-plugins-noise-cancellation` | Background noise removal (BVC) |
| `livekit-plugins-silero` | Voice activity detection |
| `google-genai` | Google AI Studio SDK |
| `aiohttp` | Async HTTP for external APIs |
| `pyautogui` | Desktop GUI automation |
| `pygetwindow` | Window management |
| `groq` | LLaMA 3 via Groq (code gen, PDF Q&A) |
| `PyPDF2` | PDF text extraction |
| `feedparser` | RSS news feeds |
| `openpyxl` | Excel file handling |
| `pytesseract` | OCR — click by text on screen |
| `mss` | Fast screen capture |

---

## 🔒 Security & Privacy

- ✅ **No hardcoded secrets** — all API keys loaded from `.env`
- ✅ **`.env` is gitignored** — your credentials are never committed
- ✅ **`memory.json` is gitignored** — your personal conversation data stays local only
- ✅ **All tools run locally** — no third-party data collection

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/AmazingTool`
3. Commit your changes: `git commit -m "Add AmazingTool"`
4. Push to the branch: `git push origin feature/AmazingTool`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ by <strong>Soutrik Mukherjee</strong><br/>
  <sub>Powered by Google Gemini · LiveKit · Groq · Python</sub>
</p>
