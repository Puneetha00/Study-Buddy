async function loadTool(action) {
    const topic = document.getElementById('topic').value.trim();
    const area = document.getElementById('display-area');
    
    if (!topic) {
        alert("Please enter a topic first! 📚");
        return;
    }

    area.innerHTML = `<div style="text-align: center; padding: 50px;">
                        <div class="spinner"></div>
                        <h3>Fetching ${action} for ${topic}... 🧠</h3>
                      </div>`;

    try {
        const response = await fetch('/ai-action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type: action, topic: topic })
        });
        
        const data = await response.json();
        
        // We use innerHTML with clean formatting
        area.innerHTML = `
            <div class="result-card">
                <h3 style="color: #60a5fa; margin-bottom: 20px;">${action.toUpperCase()}: ${topic}</h3>
                <div class="result-content" style="white-space: pre-wrap; font-size: 1.1rem; line-height: 1.8;">
                    ${data.result}
                </div>
            </div>`;
    } catch (error) {
        area.innerHTML = `<p style="color: #ff6b6b;">Error: Could not reach the server. Make sure your Flask app is running!</p>`;
    }
}