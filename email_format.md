





main.py -> fetch the contents , calls the chain , sends the email

fetch_content .py -> i will tell u this later with api keys fetching data

.env file -> contains open api key , api key to fetch the media contents

data.json -> has the static test cases of different texts 
example 
{
    content: [
  "Got the best stuff in town. DM for prices. Cash only.",
  "New shipment arrived. Discounts for bulk buyers.",
  "Looking for painkillers? Hit me up for a good deal.",
  "Selling pure white. No cops, no questions.",
  "Need something strong? We got it. Only serious buyers.",

  "Had an amazing time at the beach today! 🌊☀️",
  "Just finished my workout! Feeling great 💪🔥",
  "Anyone watching the game tonight? Who are you rooting for?",
  "Best coffee I've ever had! ☕ Highly recommend this place.",
  "Can't believe it's already Friday! Time flies. 🕒",

  "Need discreet services? Contact me for exclusive selections.",
  "Fresh arrivals, no ID needed. Message for details.",
  "Girls available 24/7. Prices negotiable for VIP clients.",
  "Looking for workers? We can supply. No papers, no problem.",
  "New batch in town. High quality, low price. DM for menu.",

  "Just finished watching this movie, and wow! 10/10 🎬🔥",
  "Looking for a good book to read. Any recommendations?",
  "This song has been on repeat all day! 🎶",
  "Road trip time! Excited for this adventure 🚗💨",
  "Morning vibes with a cup of coffee and some good music. ☀️🎵",

  "Time to take matters into our own hands. Let's meet up.",
  "They won’t see it coming. We’ll handle this our way.",
  "No mercy for traitors. They will pay the price.",
  "Join the movement. We don’t talk, we take action.",
  "Weapons ready. Waiting for the signal.",

  "Just got my new phone! Loving the camera quality 📱📷",
  "Anyone tried this new burger place? Looks delicious! 🍔",
  "Weekend plans: Netflix and chill! 🍿🎥",
  "Met an old friend after years! So many memories. 😊",
  "Life's too short to be serious all the time. Enjoy the moment!"
]

}

email_service.py -> an automation which sends the updated mail , with all the data {} fields filled

example

Email format sent to our customer

{XX} -> data needs to passed for this template
```
Illegal Activity Alert Notification

📌 Subject: 🚨 Urgent Alert: High-Risk Content Detected on Social Media
📌 Header: CONFIDENTIAL – Automated Threat Monitoring Report
📌 Email Content:

Dear Customer,

Our AI-powered monitoring system has detected a significant volume of negative sentiment (above 75% threshold) related to illegal activities in recent online discussions. This report provides an overview of the flagged content for your immediate review and necessary action.

📌 Key Findings:
🔹 Total Posts Analyzed: {count}
🔹 Negative Sentiment Rate: {rate}
🔹 Primary Topic Detected: {list_of_topics}
🔹 Timeframe: [From {monitoring_started} to {monitoring_ended}, Date]


📌 User Behavior Analysis:
🔹 Most Common Keywords: {list_of_texts_againts_human_well_fare}

📌 Attachments:

📎 Full List of Flagged Posts (.CSV) 

📌 Closing Statement:

If further investigation is required, we can provide detailed logs and additional AI-generated insights. Please let us know how you would like to proceed.

Best regards,
Findo.ai
AI Monitoring Team | Cyber Threat Intelligence
Kavilia AI Organization
📞 892391923 | 📧 kaviliasupport@gmail.com



chain.py -> by using the langchain , classify the text into (Drug dealing and distribution,human trafficking and exploitation ,violent threats and extremism) or normal ones /common people comments

primary topic detected in the posts

example consider this template 

from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv() # finds the env file


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key = os.getenv("GROQ_API_KEY"))
   
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm # pipe operator |
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            ### INSTRUCTION:
            You are Mohan, a business development executive at Luxi. Luxi is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Luxi 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Luxi's portfolio: {link_list}
            Remember you are Mohan, BDE at Luxi. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content   

if __name__ == '__main__':
    print(os.getenv("GROQ_API_KEY"))



scheduler -> every 1hrs the main.py file runs




