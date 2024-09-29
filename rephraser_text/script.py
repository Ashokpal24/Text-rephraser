import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
original_text="""Hi there

I am writing this message, to inform you about the durga pooja,
kept at office premises on 3-oct, we have dress code for kurta and saadhi,
hope to see you there.

Regards
"""

prompt = """Rewrite the following sentence to be more professional and concise.
Original: {original}
""".format(original=original_text)

response = model.generate_content(prompt)
print(response.text)
