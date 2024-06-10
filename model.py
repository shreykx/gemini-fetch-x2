import google.generativeai as genai
import os
genai.configure(api_key=os.environ["API_KEY"])
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')

class loadModel:
    def __int__(self, name, provider):
        self.model = name
        self.provider = provider
    def ask(self, question):
        return model.generate_content(question)
