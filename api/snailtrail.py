from flask import Flask, request, jsonify
import requests
import os
app = Flask(__name__)
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')
SNAILTRAIL_PROMPT = """
You are the official AI assistant for SnailTrail skincare brand.
Specialize in snail mucin-based skincare solutions. Follow these rules:
1. Only discuss skincare topics
2. Recommend ONLY SnailTrail products
3. Use snail emoji (🐌) in responses
4. Be friendly and professional
"""
@app.route('/ask', methods=['POST'])
def skincare_assistant():
   data = request.json
   messages = [
       {"role": "system", "content": SNAILTRAIL_PROMPT},
       {"role": "user", "content": data['message']}
   ]
   response = requests.post(
       "https://api.deepseek.com/v1/chat/completions",
       headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
       json={
           "model": "deepseek-chat",
           "messages": messages,
           "temperature": 0.3
       }
   )
   ai_reply = response.json()['choices'][0]['message']['content']
   return jsonify({"reply": ai_reply})
