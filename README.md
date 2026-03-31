# Day 16: AI Email Triage Agent 📧

An AI agent that connects to your Gmail inbox, analyzes unread emails using Llama 3.3 (via Groq), categorizes them by priority, and generates a daily briefing with automated draft replies for urgent tasks.

## Features
- **Gmail Integration:** Uses Google API to fetch the latest unread emails.
- **AI Triaging:** Categorizes emails into:
  - 🔴 **URGENT:** Requires immediate attention.
  - 🟡 **HIGH:** High priority but not immediate.
  - 🟢 **LOW:** Informational or non-urgent.
  - ⚫ **SPAM:** Junk or unsolicited marketing.
- **Automated Drafts:** Prepares professional replies for high-priority emails.
- **Daily Briefing:** Summarizes your inbox status in a clean terminal report.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gnarendra9014-blind/day_16-of-ML-Projects.git
   cd day_16-of-ML-Projects
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Credentials:**
   - Create a `.env` file and add your `GROQ_API_KEY`.
   - Download your `credentials.json` from the Google Cloud Console and place it in the root folder.

5. **Run the App:**
   ```bash
   python app.py
   ```

## Tech Stack
- **Python**
- **Groq AI (Llama 3.3 70B)**
- **Google Gmail API**
- **python-dotenv**
