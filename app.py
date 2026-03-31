from gmail_client import get_gmail_service, get_unread_emails
from triage import triage_email, generate_briefing

def main():
    print("\n=== AI Email Triage Agent ===")
    print("Connecting to Gmail...")
    service = get_gmail_service()
    print("Connected! Fetching unread emails...")

    emails = get_unread_emails(service, max_results=10)
    print(f"Found {len(emails)} unread emails.\n")

    if not emails:
        print("No unread emails found!")
        return

    triaged = []
    for i, email in enumerate(emails):
        print(f"Triaging {i+1}/{len(emails)}: {email['subject'][:50]}...")
        result = triage_email(email)
        triaged.append(result)
        icon = {
            "URGENT": "🔴",
            "HIGH": "🟡",
            "LOW": "🟢",
            "SPAM": "⚫"
        }.get(result["category"], "⚪")
        print(f"  {icon} {result['category']} — {result['reason']}")
        if result["draft_reply"] != "NONE":
            print(f"  Draft reply ready")

    print(generate_briefing(triaged))

    print("\nDraft replies for urgent/high emails:")
    for e in triaged:
        if e["category"] in ["URGENT", "HIGH"] and e["draft_reply"] != "NONE":
            print(f"\nTo: {e['sender']}")
            print(f"Re: {e['subject']}")
            print(f"Draft: {e['draft_reply']}")

if __name__ == "__main__":
    main()