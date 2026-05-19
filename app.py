import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize the Groq client
# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai-action', methods=['POST'])
def ai_action():
    data = request.json
    action = data.get('type')
    topic = data.get('topic')
    
    # Custom prompts for engineering students
    prompts = {
        "plan": f"Create a structured 7-day study plan for '{topic}' for an engineering student. Use bullet points.",
        "quiz": f"Create 5 challenging multiple-choice questions on '{topic}' with the correct answers clearly listed at the bottom.",
        "summary": f"Provide a comprehensive, technical summary of '{topic}' including key formulas and concepts.",
        "resources": f"Suggest 3 high-quality educational YouTube channels, 2 recommended textbooks, and 1 website for mastering '{topic}'."
    }
    
    selected_prompt = prompts.get(action, f"Explain {topic}")
    
    try:
        # Calling Groq's Llama 3 model (Free and fast)
        # Change the model to the current standard
        chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful and intelligent AI tutor for engineering students."},
        {"role": "user", "content": selected_prompt}
    ],
    model="llama-3.3-70b-versatile", 
)
        
        result = chat_completion.choices[0].message.content
        return jsonify({"result": result})
        
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

# Change the end of app.py to this:
if __name__ == '__main__':
    # Do not call app.run() here. 
    # Gunicorn handles it for you.
    pass