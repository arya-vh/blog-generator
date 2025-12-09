async function generateBlog() {
    const prompt = document.getElementById('prompt').value;
    const response = await fetch('http://localhost:5500/generate-blog', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: prompt })
    });
    const data = await response.json();
    document.getElementById('blog-output').innerHTML = `<p>${data.blog}</p>`;
}
