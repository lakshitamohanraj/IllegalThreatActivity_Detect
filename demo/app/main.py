from fetch_content import fetch_latest_content
from chain import Chain
from email_service import send_email
from dotenv import load_dotenv

load_dotenv()


def process_posts():
    posts = fetch_latest_content()
    chain = Chain()
    flagged_posts = []
    
    for post in posts:
        classification = chain.classify_post(post)
        category = classification.get("category")
        
        if category and category != "Normal / Safe content":
            flagged_posts.append({"post": post, "category": category})
    
    if flagged_posts:
        summary = {
            "count": len(posts),
            "rate": (len(flagged_posts) / len(posts)) * 100,
            "topics": list(set([fp["category"] for fp in flagged_posts])),
            "monitoring_started": "10:00 AM",
            "monitoring_ended": "11:00 AM",
            "keywords": ["DM", "Buy", "Sell"]
        }
        send_email(summary)

if __name__ == "__main__":
    process_posts()
