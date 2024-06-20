document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendation-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const crop = document.getElementById('crop').value;
        const nitrogen = document.getElementById('nitrogen').value;
        const phosphorus = document.getElementById('phosphorus').value;
        const potassium = document.getElementById('potassium').value;

        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ crop, nitrogen, phosphorus, potassium })
        })
        .then(response => response.json())
        .then(data => {
            if (data.recommendation) {
                document.getElementById('recommendation').textContent = data.recommendation;
            } else if (data.error) {
                document.getElementById('recommendation').textContent = data.error;
            }
        })
        .catch(error => {
            document.getElementById('recommendation').textContent = 'An error occurred: ' + error;
        });
    });
});
