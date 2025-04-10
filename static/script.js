document.getElementById('prediction-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const button = document.getElementById('predict-button');
  const resultDiv = document.getElementById('result');

  button.disabled = true;
  button.textContent = 'Predicting...';
  resultDiv.innerHTML = '⏳ Analyzing...';

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData
    });

    const result = await response.json();

    if (result.error) {
      resultDiv.textContent = `🚫 Error: ${result.error}`;
      resultDiv.className = 'result error';
    } else {
      resultDiv.innerHTML = `
        <p>Prediction: <strong>${result.prediction === 1 ? '🧠 Fake' : '✅ Real'}</strong></p>
        <p>Probability of being fake: <strong>${(result.probability * 100).toFixed(2)}%</strong></p>
      `;
      resultDiv.className = 'result success';
    }
  } catch (error) {
    console.error(error);
    resultDiv.textContent = 'An unexpected error occurred.';
    resultDiv.className = 'result error';
  }

  button.disabled = false;
  button.textContent = 'Predict';
});
