<h1 align="center">
  <img src="https://img.shields.io/badge/FRIDAY-AI%20ASSISTANT-6c47ff?style=for-the-badge&logo=google&logoColor=white" alt="Friday AI Assistant"/>
</h1>

<p align="center">
  <b>🤖 Your Intelligent Personal Desktop AI — Powered by Google Gemini</b><br/>
  Voice-controlled · Real-time · 50+ Tools · Hindi + English
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange?style=flat-square&logo=google" />
  <img src="https://img.shields.io/badge/LiveKit-Realtime-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Groq-LLaMA%203-red?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" />
</p>

---

## 🌟 What is Friday?

**Friday (Friday AI Assistant)** is a powerful voice-first AI desktop assistant built on **Google Gemini 2.5 Flash Realtime** and the **LiveKit Agents framework**. Inspired by Tony Stark's iconic AI companion from Iron Man, Friday understands both **Hindi and English**, controls your entire PC, automates complex tasks, and feels like having a real assistant by your side — 24/7.

> 💬 *"Ready whenever you are, Boss."* — Friday is always listening.

---

## ✨ Features at a Glance

| Category | Capabilities |
|----------|-------------|
| 🎙️ **Voice** | Real-time Hindi + English voice conversation via Gemini |
| 🖥️ **Desktop Control** | Open apps, manage windows, scroll, type, click |
| 🌐 **Web & Search** | DuckDuckGo, Wikipedia, live weather, top news |
| 📱 **WhatsApp** | Send messages & media via desktop automation |
| 🎵 **Media** | YouTube playback, Spotify control (play/pause/next) |
| 📄 **Documents** | Read/query PDFs, Word docs, create Excel files |
| 🤖 **AI Image Gen** | Generate AI images via Pollinations.ai (free, no key!) |
| 💻 **Code Assistant** | Generate & run code via Groq AI in VS Code |
| 🔔 **Reminders** | Smart reminder system with voice alerts |
| 📸 **Screen Vision** | Screenshot analysis with Gemini Vision |
| 🧠 **Code Fixer** | Automatically fix code errors |
| 🔒 **System Power** | Shutdown, restart, lock your PC |
| 📷 **Camera** | Live camera analysis |
| 🎛️ **Volume/Brightness** | Voice-controlled system settings |
| 📁 **File Management** | Search, open, convert files (PDF↔Word↔Excel) |
| 🛡️ **Virus Scan** | Quick system virus scan |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/soutrikmukherjee068-cmyk/MJ-AI-ASSISTANT.git
cd MJ-AI-ASSISTANT
```

### 2. Set Up Python Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

### 3. Configure Your API Keys

Create a `.env` file in the root directory (copy from the template below):

```env
# ✅ REQUIRED
GEMINI_API_KEY=your_google_ai_studio_api_key_here

# 🎙️ Voice settings
GEMINI_VOICE=Kore
LAN=Hindi
FRIDAY_VARIANT=Humanized
USER_NAME=Boss

# 📧 Email (optional)
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password_here

# 🤖 Code generation (optional — needed for code gen & PDF Q&A)
GROQ_API_KEY=your_groq_api_key_here

# 🔴 LiveKit (optional — needed for cloud deployment)
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

> 🔑 **Get your free API keys:**
> - **Gemini** → [aistudio.google.com](https://aistudio.google.com)
> - **Groq** → [console.groq.com](https://console.groq.com)
> - **LiveKit** → [livekit.io](https://livekit.io)

### 4. Run Friday

```bash
# Simple launch (console mode)
python run_agent.py console

# Or directly with LiveKit
python agent.py console
```

---

## 🗂️ Project Structure

```
Friday-AI-ASSISTANT/
│
├── agent.py              # 🧠 Main agent — LiveKit + Gemini setup
├── prompts_mj.py         # 📝 Friday's personality & system prompts
├── gemini_voice.py       # 🎙️ Gemini TTS voice helper
├── run_agent.py          # 🚀 Easy launch script
├── tools.py              # 🔧 Core tools (legacy/monolithic)
│
├── Tools/                # 🧰 Modular tool collection
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
├── .env                  # 🔒 Your secrets (NOT committed)
├── .gitignore            # 🚫 Ignores .env, .venv, __pycache__
└── memory.json           # 🧠 Persistent memory (NOT committed)
```

---

## 🧠 Architecture

```
User Voice
    │
    ▼
LiveKit Room (WebRTC)
    │
    ▼
AgentSession ──► UltimateAdvancedNova (Agent)
    │                    │
    │               Gemini 2.5 Flash Realtime LLM
    │                    │
    └──────────► 50+ Function Tools
                  (system, web, media, docs, code...)
```

Friday uses **LiveKit's Agents framework** for real-time audio streaming, **Google Gemini 2.5 Flash Native Audio Preview** as the reasoning + voice backbone, and a rich ecosystem of **Python tools** for executing desktop tasks.

---

## 🛠️ Key Dependencies

| Package | Purpose |
|---------|---------|
| `livekit-agents` | Real-time agent framework |
| `livekit-plugins-google` | Gemini Realtime model integration |
| `google-genai` | Google AI Studio SDK |
| `aiohttp` | Async HTTP for APIs |
| `pyautogui` | Desktop GUI automation |
| `pygetwindow` | Window management |
| `groq` | LLaMA 3 via Groq API (code gen, PDF Q&A) |
| `PyPDF2` | PDF text extraction |
| `feedparser` | RSS news feeds |
| `pillow` | Image processing |
| `openpyxl` | Excel file handling |

---

## 🔒 Security & Privacy

- ✅ **No hardcoded secrets** — all API keys loaded from `.env`
- ✅ **`.env` is gitignored** — your credentials are never committed
- ✅ **`memory.json` is gitignored** — your personal data stays local


---

## 📋 Example Voice Commands

```
"Friday, WhatsApp mein Rahul ko message bhej do — kal milte hain"
"Google par search karo AI news"
"Mera system volume 60% kar do"
"Screen ka screenshot le lo"
"Python mein calculator banao aur VS Code mein type kar do"
"Spotify par Arijit Singh ka gaana chalao"
"Weather kya hai Delhi mein?"
"Excel mein ek table banao students ki"
"PDF upload karo aur mujhe summary do"
"Screen pe kya dikh raha hai?"
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/AmazingTool`
3. Commit: `git commit -m "Add AmazingTool"`
4. Push: `git push origin feature/AmazingTool`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ by <strong>Soutrik Mukherjee</strong><br/>
  <sub>Powered by Google Gemini · LiveKit · Groq · Python</sub>
</p>
