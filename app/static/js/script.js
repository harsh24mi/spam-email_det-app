document.getElementById('spam-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent the default form submission

    const emailText = document.getElementById('email-text').value;
    const resultDiv = document.getElementById('result');
    const loader = document.getElementById('loader');

    // Clear previous results and show loader
    resultDiv.innerHTML = '';
    loader.classList.remove('d-none');

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email_text: emailText }),
        });

        loader.classList.add('d-none'); // Hide loader

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'An error occurred.');
        }

        const data = await response.json();
        
        // Display the result
        let alertClass = '';
        let resultText = '';
        
        if (data.prediction === 'spam') {
            alertClass = 'alert-danger';
            resultText = '<strong>Result:</strong> This looks like <strong>SPAM</strong>. 🗑️';
        } else {
            alertClass = 'alert-success';
            resultText = '<strong>Result:</strong> This looks like a <strong>SAFE</strong> email. ✅';
        }

        resultDiv.innerHTML = `<div class="alert ${alertClass}" role="alert">${resultText}</div>`;

    } catch (error) {
        loader.classList.add('d-none'); // Hide loader on error
        resultDiv.innerHTML = `<div class="alert alert-warning" role="alert"><strong>Error:</strong> ${error.message}</div>`;
    }
});