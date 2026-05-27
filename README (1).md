# HuakaiMod Bot 🌴

An AI-powered Discord bot for the HUAKAI moderation team.
Built with Pycord + Claude API. Knows your full handbook and punishment guide.

---

## Features

- 💬 Chat with the AI by **mentioning** the bot or using `/ask`
- ⚖️ Look up punishments with `/punishment`
- 📖 Look up rules with `/rule`
- 📊 Check activity requirements with `/activity`
- ⚠️ Check strike consequences with `/strike`
- 🏛️ View the full hierarchy with `/hierarchy`
- 🧹 Clear conversation history with `/clearhistory`

---

## Setup

### 1. Create your Discord Bot
1. Go to https://discord.com/developers/applications
2. New Application → Bot tab → Reset Token → copy token
3. Enable **Message Content Intent** under Privileged Gateway Intents
4. OAuth2 → URL Generator → select `bot` + `applications.commands`
5. Permissions: `Send Messages`, `Read Messages`, `Embed Links`, `Read Message History`
6. Copy the generated URL and invite the bot to your server

### 2. Get your Anthropic API Key
1. Go to https://console.anthropic.com
2. API Keys → Create Key → copy it

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
```bash
# Linux/Mac
export DISCORD_TOKEN=your_token_here
export ANTHROPIC_API_KEY=your_key_here

# Windows
set DISCORD_TOKEN=your_token_here
set ANTHROPIC_API_KEY=your_key_here
```
Or rename `.env.example` to `.env` and use python-dotenv.

### 5. Run the bot
```bash
python bot.py
```

---

## Hosting on Railway (recommended)

1. Push this folder to a GitHub repo
2. Go to https://railway.app → New Project → Deploy from GitHub
3. Add environment variables: `DISCORD_TOKEN` and `ANTHROPIC_API_KEY`
4. Railway auto-detects Python and runs `python bot.py`
5. Done — runs 24/7 ✅

---

## Optional: AI responds to ALL messages in a channel

In `bot.py`, find this line:
```python
AI_CHANNEL_ID = None
```
Change it to your channel's ID:
```python
AI_CHANNEL_ID = 1234567890123456789
```
The bot will then respond to every message in that channel.
