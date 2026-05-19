async function loadTool(action) {
    const topic = document.getElementById('topic').value.trim();
    const area = document.getElementById('display-area');
    
    if (!topic) {
        alert("Please enter a topic first! 📚");
        return;
    }

    area.innerHTML = `<h3>Generating... ⏳</h3>`;

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
        area.innerHTML = `<p>Error: Could not connect to the server.</p>`;
    }
}