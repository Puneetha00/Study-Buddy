import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

# 1. Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# 2. Get API key and initialize client
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("---------------------------------------------------------")
    print("ERROR: GROQ_API_KEY not found in .env file!")
    print("Please ensure .env is in the same folder as app.py")
    print("---------------------------------------------------------")
    client = None
else:
    client = Groq(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Check if client was initialized
    if client is None:
        return jsonify({"result": "Error: API Key is missing. Check your .env file."}), 500

    try:
        data = request.get_json()
        topic = data.get('topic')
        prompt_type = data.get('type')
        
        if not topic:
            return jsonify({"result": "Please enter a topic!"}), 400

        # AI Prompts
        prompts = {
            "timetable": f"Create a structured 7-day study timetable for {topic}.",
            "quiz": f"Generate 5 quiz questions with answers for {topic}.",
            "summary": f"Provide a clear, concise summary of {topic}.",
            "resources": f"List 5 essential concepts and resources to master {topic}."
        }

        # API Call to Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional Engineering Tutor."},
                {"role": "user", "content": prompts.get(prompt_type, "Explain " + topic)}
            ],
            model="llama-3.3-70b-versatile",
        )

        result = chat_completion.choices[0].message.content
        return jsonify({"result": result})

    except Exception as e:
        print("ERROR IN GENERATE:", str(e))
        return jsonify({"result": f"AI Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)