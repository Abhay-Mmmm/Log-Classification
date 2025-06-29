from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq = Groq()
prompt = "What's the difference between ML and Deep Learning"
chat_completion = groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(chat_completion.choices[0].message.content)