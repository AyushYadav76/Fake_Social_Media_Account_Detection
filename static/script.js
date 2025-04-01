document.getElementById('prediction-form').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    // Get form data
    const formData = new FormData(event.target);
  
    // Show loading state on the button
    const button = document.getElementById('predict-button');
    button.disabled = true;
    button.textContent = 'Predicting...';
  
    try {
      // Send POST request to Flask backend
      const response = await fetch('/predict', {
        method: 'POST',
        body: formData
      });
  
      const result = await response.json();
      const resultDiv = document.getElementById('result');
  
      // Display the result
      if (result.error) {
        resultDiv.textContent = `Error: ${result.error}`;
        resultDiv.className = 'result error';
      } else {
        resultDiv.innerHTML = `
          <p>Prediction: <strong>${result.prediction === 1 ? 'Fake' : 'Real'}</strong></p>
          <p>Probability of being fake: ${(result.probability * 100).toFixed(2)}%</p>
        `;
        resultDiv.className = 'result success';
      }
    } catch (error) {
      console.error(error);
      const resultDiv = document.getElementById('result');
      resultDiv.textContent = 'An unexpected error occurred.';
      resultDiv.className = 'result error';
    }
  
    // Reset button state
    button.disabled = false;
    button.textContent = 'Predict';
  });