document.getElementById('url-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const longUrl = document.getElementById('long-url').value;

    // Replace this with your API Gateway URL
    const apiUrl = 'https://your-api-id.execute-api.region.amazonaws.com/prod/shorten';

    const payload = {
        long_url: longUrl
    };

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        if (data.short_url) {
            document.getElementById('short-url').innerText = data.short_url;
            document.getElementById('result').style.display = 'block';
        } else {
            alert('Error: Unable to generate shortened URL');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error with the request');
    });
});
