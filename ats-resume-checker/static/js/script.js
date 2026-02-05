async function analyze() {
    const jd = document.getElementById('jd').value;
    const file = document.getElementById('resume').files[0];
    const resDiv = document.getElementById('result');

    if (!jd || !file) return alert("Upload both!");

    const formData = new FormData();
    formData.append('job_description', jd);
    formData.append('resume', file);

    resDiv.innerText = "Processing...";
    try {
        const response = await fetch('/analyze', { method: 'POST', body: formData });
        const data = await response.json();
        resDiv.innerText = data.analysis || data.error;
    } catch (e) {
        resDiv.innerText = "Error connecting to server.";
    }
}