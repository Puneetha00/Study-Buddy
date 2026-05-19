async function fetchAI(type) {
    const topic = document.getElementById('topic').value;
    const output = document.getElementById('output');
    
    if (!topic) { alert("Please enter a topic!"); return; }

    output.innerText = "Loading...";

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({type: type, topic: topic})
        });

        // This will now capture the specific error from the server
        const data = await response.json();
        
        if (!response.ok) {
            output.innerText = "Server Error: " + (data.result || "Unknown error");
        } else {
            output.innerText = data.result;
        }
    } catch (error) {
        output.innerText = "Network Error: " + error.message;
    }
}