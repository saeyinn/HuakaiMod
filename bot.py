import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
AUTO_RESPOND_CHANNEL = 1286859873195130890

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ── Punishment data ───────────────────────────────────────────────────────────

PUNISHMENTS = {
    "dm_harassment": {
        "name": "DM Harassment",
        "desc": "Harassing someone through DMs",
        "steps": ["Warn", "6 hour mute", "Kick", "Permanent ban"],
    },
    "server_harassment": {
        "name": "In-Server Harassment",
        "desc": "Harassing someone in the server/community",
        "steps": ["Warn", "9 hour mute", "Kick", "Permanent ban"],
    },
    "racist": {
        "name": "Racist Behavior",
        "desc": "Comments regarding race or sex inequality",
        "steps": ["Warn", "Kick", "25 day ban", "Permanent ban"],
        "serious": True,
    },
    "disrespect": {
        "name": "Disrespectful Comments",
        "desc": "Being rude, mean, toxic, etc.",
        "steps": ["Warn", "3 hour mute", "Kick", "25 day ban"],
    },
    "cursing": {
        "name": "Direct Cursing",
        "desc": "Cursing directly at someone (e.g. 'f*** you')",
        "steps": ["Warn", "2 hour mute", "Kick", "25 day ban"],
    },
    "server_advertising": {
        "name": "Server Advertising",
        "desc": "Advertising games, apps, servers, etc. in the server",
        "steps": ["3 hour mute", "Kick", "25 day ban", "Permanent ban"],
    },
    "dm_advertising": {
        "name": "DM Advertising",
        "desc": "Advertising through DMs",
        "steps": ["Warn", "Kick", "25 day ban", "Permanent ban"],
    },
    "drama": {
        "name": "Inciting Drama",
        "desc": "Creating drama within the server or community",
        "steps": ["Kick", "30 day ban", "Permanent ban", None],
        "serious": True,
    },
    "ban_evading": {
        "name": "Ban Evading",
        "desc": "Using an alt account to bypass a ban",
        "steps": ["Permanent ban", None, None, None],
        "serious": True,
    },
    "inappropriate": {
        "name": "Inappropriate Content",
        "desc": "Inappropriate gifs, videos, images, or conversations",
        "steps": ["6 hour mute", "Kick", "25 day ban", "Permanent ban"],
    },
    "spamming": {
        "name": "Spamming",
        "desc": "Spamming the chat with messages or images",
        "steps": ["6 hour mute", "Kick", "Permanent ban", None],
    },
    "channel_misuse": {
        "name": "Channel Misuse",
        "desc": "Using the wrong channel (e.g. chatting in the commands channel)",
        "steps": ["Warn", "3 hour mute", "Kick", "25 day ban"],
    },
    "everyone_ping": {
        "name": "@everyone Attempts",
        "desc": "Trying to ping @everyone without permission",
        "steps": ["Warn", "3 hour mute", "Kick", "25 day ban"],
    },
    "non_english": {
        "name": "Non-English Use",
        "desc": "Not using English in the server",
        "steps": ["Warn", "6 hour mute", "Kick", "25 day ban"],
    },
    "sensitive_topics": {
        "name": "Sensitive Topics",
        "desc": "Talking about suicide, self-harm, etc.",
        "steps": ["9 hour mute", "Kick", "Permanent ban", None],
        "serious": True,
    },
    "mini_modding": {
        "name": "Mini-Modding",
        "desc": "A non-moderator trying to enforce rules or tell people what to do",
        "steps": ["Warn", "6 hour mute", "Kick", "25 day ban"],
    },
}

# ── Static info ───────────────────────────────────────────────────────────────

ACTIVITY_INFO = """**Weekly Activity Requirements**
- **Mod Intern** — Complete tasks + 75 messages
- **Junior Mod** — 150 msgs + 1 mod action *or* 200 msgs
- **Moderator** — 200 msgs + 2 mod actions *or* 300 msgs
- **Senior Mod** — 300 msgs + 3 mod actions *or* 375 msgs

cant meet requirements? just let your team lead know in advance. max inactivity (LOA) is 3 weeks — need longer, contact Mod Leadership."""

STRIKE_INFO = """**Strike Consequences**
- **Mod Intern** — 2 strikes = Termination
- **Junior Mod** — 3 strikes = Termination
- **Moderator** — 2 strikes = Demotion to Jr. Mod | 3 strikes = Termination
- **Senior Mod** — 1 strike = Demotion to Mod | 2 strikes = Demotion to Jr. Mod | 3 strikes = Removal

Strikes are given for failing activity requirements, not following rules, or unprofessional behavior."""

CHAIN_INFO = """**Chain of Command**
Mod Intern → Junior Moderator → Moderator → Senior Moderator → Mod Lead/Co-Lead → Mod Overseer → Administration & Ownership

always report to the rank directly above you unless told otherwise."""

ROLE_INFO = """**Role Responsibilities**
- **Mod Intern** — Learn procedures, complete training tasks. Reports to: Jr. Mods+
- **Junior Mod** — Assist with basic mod tasks. Reports to: Moderators+
- **Moderator** — Enforce rules independently, apply punishments. Reports to: Senior Mods+
- **Senior Mod** — Handle escalated cases, approve/deny kicks & bans, guide lower staff. Reports to: Mod Lead
- **Mod Lead/Co-Lead** — Oversee the department, make final decisions. Reports to: Administration
- **Mod Overseer** — Oversee all systems, support leadership. Reports to: Administration"""

ESCALATION_INFO = """**Escalation Process**
Standard: **Warning → Mute → Kick → Ban**

you can skip steps for serious violations like racism, severe harassment/threats, malicious activity, or ban evasion. those should also be escalated to Senior Mod or Leadership."""

INACTIVITY_INFO = """**Inactivity / LOA Rules**
- Max period is **3 weeks** — need more, contact Mod Leadership
- You **cannot** perform any mod actions while on LOA or marked Inactive
- Returning on a **Monday or Tuesday**? you're still expected to meet that week's requirements
- Going above activity requirements can be considered for promotion"""

CONDUCT_INFO = """**Code of Conduct — Strictly Prohibited**
- Abuse of power
- Favoritism or bias
- Using your staff position for personal gain
- Leaking internal mod info — **immediate termination, no warning**

stay neutral, stay professional, and never let personal feelings affect your decisions."""

HELP_MSG = """hey! here's what i can help with:

**Punishment situations** — just describe it casually:
> "someone is spamming" / "member sent racist stuff" / "user advertising in dms"

**Other topics:**
> `activity` — weekly requirements per rank
> `strikes` — strike consequences
> `chain of command` — who reports to who
> `roles` — what each rank does
> `escalation` — when to skip steps
> `inactivity` or `loa` — inactivity request rules
> `conduct` — code of conduct for mods"""

# ── Matching logic ────────────────────────────────────────────────────────────

def detect_violation(msg: str):
    m = msg.lower()
    has_dm = any(w in m for w in ["dm", "dms", "direct message"])

    if any(w in m for w in ["harass", "bullying", "bully", "threatening", "threat"]):
        return "dm_harassment" if has_dm else "server_harassment"

    if any(w in m for w in ["advertis", "promo", "promoting", "invite link", "server link"]):
        return "dm_advertising" if has_dm else "server_advertising"

    if any(w in m for w in ["racist", "racism", "racial", "sexist", "sex inequality", "discriminat", "race comment"]):
        return "racist"

    if any(w in m for w in ["spam", "spamming", "flooding", "flood"]):
        return "spamming"

    if any(w in m for w in ["drama", "incit", "stirring", "stir"]):
        return "drama"

    if any(w in m for w in ["ban evad", "ban evasion", "alt account", "alt acc", "evading", "bypass ban", "banned account", "second account"]):
        return "ban_evading"

    if any(w in m for w in ["sensitive", "suicide", "self harm", "self-harm", "depression", "kms", "kill myself", "hurt myself"]):
        return "sensitive_topics"

    if any(w in m for w in ["inappropriate", "nsfw", "explicit", "inappropriate gif", "inappropriate vid", "inappropriate convo", "sexual content"]):
        return "inappropriate"

    if any(w in m for w in ["curse", "cursing", "swear", "swearing", "cuss", "cussing", "f you", "f*** you", "direct curse"]):
        return "cursing"

    if any(w in m for w in ["disrespect", "rude", "mean", "toxic", "insult", "offensive"]):
        return "disrespect"

    if any(w in m for w in ["channel misuse", "wrong channel", "side chat", "off topic", "wrong chat", "misusing channel"]):
        return "channel_misuse"

    if any(w in m for w in ["everyone", "@everyone", "mass ping", "ping everyone", "ping @"]):
        return "everyone_ping"

    if any(w in m for w in ["non english", "non-english", "foreign language", "not english", "other language", "different language"]):
        return "non_english"

    if any(w in m for w in ["mini mod", "mini-mod", "minimod", "backseat mod", "telling people what to do", "non mod", "pretending to mod"]):
        return "mini_modding"

    return None


def detect_topic(msg: str):
    m = msg.lower()
    if any(w in m for w in ["activity", "requirement", "message count", "weekly", "how many messages", "messages needed"]):
        return "activity"
    if any(w in m for w in ["strike", "strikes", "disciplinary"]):
        return "strikes"
    if any(w in m for w in ["chain of command", "hierarchy", "report to", "who do i report", "chain", "who to tell", "who to contact"]):
        return "chain"
    if any(w in m for w in ["role", "rank", "responsibilities", "what does", "what do", "what is a"]):
        return "roles"
    if any(w in m for w in ["escalat", "skip step", "bypass punishment", "go straight", "skip punishment"]):
        return "escalation"
    if any(w in m for w in ["inactiv", "loa", "leave of absence", "time off", "taking a break", "break"]):
        return "inactivity"
    if any(w in m for w in ["conduct", "code of conduct", "prohibited", "not allowed as mod", "rules for mods", "mod rules"]):
        return "conduct"
    if any(w in m for w in ["help", "what can you do", "commands", "what do you know", "how to use"]):
        return "help"
    return None


def format_punishment(key: str) -> str:
    v = PUNISHMENTS[key]
    steps = [s for s in v["steps"] if s]
    lines = [f"**{v['name']}** — {v['desc']}", ""]
    for i, step in enumerate(steps):
        lines.append(f"Offense {i + 1}: **{step}**")
    if v.get("serious"):
        lines.append("\n> Serious violation — escalate to Senior Mod or Leadership if needed.")
    return "\n".join(lines)


def get_response(message: str) -> str:
    topic = detect_topic(message)
    if topic == "activity":
        return ACTIVITY_INFO
    if topic == "strikes":
        return STRIKE_INFO
    if topic == "chain":
        return CHAIN_INFO
    if topic == "roles":
        return ROLE_INFO
    if topic == "escalation":
        return ESCALATION_INFO
    if topic == "inactivity":
        return INACTIVITY_INFO
    if topic == "conduct":
        return CONDUCT_INFO
    if topic == "help":
        return HELP_MSG

    violation = detect_violation(message)
    if violation:
        return format_punishment(violation)

    return "hmm not sure what that's about, can you be a bit more specific? try something like 'someone is spamming' or 'member sent racist stuff' and i'll give you the steps. say `help` to see everything i can answer"


# ── Bot events ────────────────────────────────────────────────────────────────

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="mod help | ping me!"
    ))


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    in_auto_channel = message.channel.id == AUTO_RESPOND_CHANNEL
    mentioned = bot.user.mentioned_in(message)

    if in_auto_channel or mentioned:
        content = message.content.replace(f"<@{bot.user.id}>", "").strip()

        if not content:
            if mentioned:
                await message.reply("hey! ask me about punishments, rules, or anything from the handbook. say `help` to see what i know")
            return

        await message.reply(get_response(content))

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
