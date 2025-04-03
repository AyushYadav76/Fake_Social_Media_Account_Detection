import pandas as pd
from sklearn.preprocessing import StandardScaler

# Define a function to preprocess user input
def preprocess_user_input(user_input):
    """
    Converts raw user input into the format required by the model.
    :param user_input: Dictionary containing user-provided data.
    :return: Processed feature vector.
    """
    # Define the features expected by the model
    features = [
        'account_age', 'bio_length', 'profile_picture_present', 'default_profile_image',
        'average_posts_per_day', 'peak_activity_hour', 'account_creation_year',
        'friends_to_followers_ratio', 'spam_score'
    ]

    # Create a DataFrame from the user input
    df = pd.DataFrame([user_input])

    # Add derived features
    df['account_age'] = (pd.Timestamp('2015-02-14') - pd.to_datetime(df['created_at'])).dt.days
    df['bio_length'] = df['description'].apply(lambda x: len(str(x)))
    df['profile_picture_present'] = df['default_profile_image'].apply(lambda x: 0 if x == 1 else 1)
    df['average_posts_per_day'] = df['statuses_count'] / (df['account_age'] + 1)
    df['peak_activity_hour'] = df['hour_of_day']  # Assuming this is provided in user input
    df['account_creation_year'] = pd.to_datetime(df['created_at']).dt.year
    df['friends_to_followers_ratio'] = df['friends_count'] / (df['followers_count'] + 1)
    df['spam_score'] = df['duplicate_posts'] / (df['total_posts'] + 1)


    # Select only the required features
    X = df[features]

    # Scale the features using StandardScaler
    # Load the trained scaler
    scaler = joblib.load('scaler (1).pkl')  # Load the pre-fitted scaler
    X_scaled = scaler.transform(X)  # Use transform, not fit_transform


    return X_scaled

import joblib

# Load the trained model
model = joblib.load('model.pkl')

def predict_fake_account(user_input):
    """
    Predicts whether an account is fake or not based on user input.
    :param user_input: Dictionary containing user-provided data.
    :return: Prediction result (0 for real, 1 for fake).
    """
    # Preprocess the user input
    X_scaled = preprocess_user_input(user_input)
    
    # Make a prediction using the trained model
    prediction = model.predict(X_scaled)
    probability = model.predict_proba(X_scaled)[0][1]  # Probability of being fake
    
    return {
        'prediction': int(prediction[0]),
        'probability': float(probability)
    }


from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    """
    Renders the homepage with a form for user input.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        user_input = {
            'created_at': request.form['created_at'],
            'description': request.form['description'],
            'statuses_count': int(request.form['statuses_count']),
            'followers_count': int(request.form['followers_count']),
            'friends_count': int(request.form['friends_count']),
            'duplicate_posts': int(request.form['duplicate_posts']),
            'total_posts': int(request.form['total_posts']),
            'default_profile_image': int(request.form['default_profile_image']),
            'hour_of_day': int(request.form['hour_of_day'])
        }

        # Preprocess the input and make a prediction
        result = predict_fake_account(user_input)

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
