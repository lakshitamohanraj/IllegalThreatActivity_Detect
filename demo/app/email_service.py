import smtplib
import os
from email.mime.text import MIMEText
# from dotenv import load_dotenv

# load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email(content_summary):
    subject = "🚨 Urgent Alert: High-Risk Content Detected on Social Media"
    body = f"""
    Dear Team,

    Our AI-powered monitoring system has detected a significant volume of negative sentiment (above 75% threshold) related to illegal activities.

    📌 **Key Findings:**
    🔹 **Total Posts Analyzed:** {content_summary['count']}
    🔹 **Negative Sentiment Rate:** {content_summary['rate']}%
    🔹 **Primary Topics Detected:** {", ".join(content_summary['topics'])}
    🔹 **Timeframe:** {content_summary['monitoring_started']} to {content_summary['monitoring_ended']}
    
    📌 **Most Common Keywords:**
    {", ".join(content_summary['keywords'])}

    Please review the attached flagged posts for further action.

    Best regards,
    Findo.ai
    AI Monitoring Team | Cyber Threat Intelligence
    Kavilia AI Organization
    📞 892391923 | 📧 kaviliasupport@gmail.com
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")

if __name__ == "__main__":
    test_summary = {
        "count": 10,
        "rate": 80,
        "topics": ["Drug Dealing", "Human Trafficking"],
        "monitoring_started": "10:00 AM",
        "monitoring_ended": "11:00 AM",
        "keywords": ["DM for prices", "Pure white", "No cops"]
    }
    send_email(test_summary)
