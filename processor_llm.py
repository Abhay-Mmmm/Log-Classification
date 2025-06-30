from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq = Groq()

def classify_with_llm(log_message):
    prompt = f'''Classify the following log message into one of the categories:
    1. Workflow Error, 2. Deprecation Warning, 
    If you are not sure, classify it as "Unclassified". Only return the category name.
    No preamble, no explanation, just the category name.
    Log Message: {log_message}'''

    chat_completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))