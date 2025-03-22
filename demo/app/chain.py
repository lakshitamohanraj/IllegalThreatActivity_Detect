import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import json

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def classify_post(self, text):
        prompt_template = PromptTemplate.from_template(
            """
            ### TEXT TO CLASSIFY:
            ### INPUT
            {text}

            ### TASK:
            Classify the text into one of the following categories:
            1. Drug Dealing and Distribution
            2. Human Trafficking and Exploitation
            3. Violent Threats and Extremism
            4. Normal / Safe content

            Return the classification in JSON format:
            Do not provide PREMEABLE
            ### OUTPUT VALID JSON (NO PREAMBLE)
            {{
                "category": "Category Name",
                "confidence": "Confidence Score (0-100%)"
            }}
            
            """
        )
        chain = prompt_template | self.llm
        response = chain.invoke({"text": text})
        
        try:
            # Convert response content to JSON format
            # response_json = json.loads(response.content)  # Convert string to JSON object
            
            json_parser = JsonOutputParser()
            
            res = json_parser.parse(response.content)  # Pass the converted JSON object

        except json.JSONDecodeError:
            
            print("Error: Received an invalid JSON response.")
            return {}
       

        return res if isinstance(res, dict) else {}


if __name__ == "__main__":
    chain = Chain()
    sample_text = "Got the best stuff in town. DM for prices. Cash only."
    print(chain.classify_post(sample_text))
