import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def triage_email(email: dict) -> dict:
    prompt = f"""You are an AI email assistant. Analyze this email and triage it.

From: {email['sender']}
Subject: {email['subject']}
Body: {email['body'][:300]}

Reply in EXACTLY this format:
CATEGORY: URGENT or HIGH or LOW or SPAM
REASON: one sentence why
ACTION: what the recipient should do
DRAFT_REPLY: a short professional reply if needed, else NONE"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
    )
    return parse_triage(res.choices[0].message.content, email)

def parse_triage(text: str, email: dict) -> dict:
    result = {
        "subject": email["subject"],
        "sender": email["sender"],
        "category": "LOW",
        "reason": "",
        "action": "",
        "draft_reply": "NONE",
    }
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("CATEGORY:"):
            val = line.split(":", 1)[-1].strip().upper()
            if val in ["URGENT", "HIGH", "LOW", "SPAM"]:
                result["category"] = val
        elif line.startswith("REASON:"):
            result["reason"] = line.split(":", 1)[-1].strip()
        elif line.startswith("ACTION:"):
            result["action"] = line.split(":", 1)[-1].strip()
        elif line.startswith("DRAFT_REPLY:"):
            result["draft_reply"] = line.split(":", 1)[-1].strip()
    return result

def generate_briefing(triaged: list) -> str:
    urgent = [e for e in triaged if e["category"] == "URGENT"]
    high = [e for e in triaged if e["category"] == "HIGH"]
    low = [e for e in triaged if e["category"] == "LOW"]
    spam = [e for e in triaged if e["category"] == "SPAM"]
    briefing = f"\n{'='*50}\nDAILY EMAIL BRIEFING\n{'='*50}\n"
    briefing += f"Total emails: {len(triaged)}\n"
    briefing += f"URGENT: {len(urgent)} | HIGH: {len(high)} | LOW: {len(low)} | SPAM: {len(spam)}\n"
    if urgent:
        briefing += "\nURGENT EMAILS:\n"
        for e in urgent:
            briefing += f"  - {e['subject']} from {e['sender']}\n"
            briefing += f"    Action: {e['action']}\n"
    if high:
        briefing += "\nHIGH PRIORITY:\n"
        for e in high:
            briefing += f"  - {e['subject']} from {e['sender']}\n"
    return briefing