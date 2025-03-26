from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('best_model.pkl')

# Define feature names
FEATURES = [
    'account_age', 
    'bio_length',
    'profile_picture_present', 
    'default_profile_image',
    'average_posts_per_day', 
    'retweet_to_like_ratio', 
    'engagement_rate',
    'peak_activity_hour',
    'clustering_coefficient',
    'mutual_connection_ratio',
    'spam_score',
    'account_creation_year'
]

# Root route (optional)
@app.route('/')
def home():
    return "Welcome to the Fake Social Media Account Detection API!"

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        input_data = request.json
        
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Ensure the columns match the training features
        input_df = input_df.reindex(columns=FEATURES, fill_value=0)
        
        # Make predictions
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]  # Probability of being fake
        
        # Return the result as JSON
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
