
                                             Fake Social Media Account Detection

This project aims to detect fake social media accounts by analyzing user profiles and activity patterns. Using machine learning techniques, the system predicts whether a given account is fake or legitimate based on features such as account age, profile completeness, engagement rates, and more.

Table of Contents
Features
Technologies Used
Dataset
Installation
Usage
API Endpoints
Deployment
Contributing
License
Features
Account Age Analysis : Detects anomalies in account creation dates.
Profile Completeness : Evaluates whether users have default profile pictures, missing descriptions, etc.
Engagement Metrics : Analyzes retweet-to-like ratios, average posts per day, and clustering coefficients.
Machine Learning Models : Utilizes advanced algorithms like XGBoost, LightGBM, and CatBoost for accurate predictions.
Scalable API : Built with Flask for easy integration into web applications.
Technologies Used
Programming Language : Python
Machine Learning Libraries : Scikit-learn, XGBoost, LightGBM, CatBoost
Web Framework : Flask
Data Processing : Pandas, NumPy
Visualization : Matplotlib, Seaborn
Deployment : Render (or other platforms like Heroku, AWS, etc.)
Dataset:
The model is trained on a dataset containing features extracted from real and fake social media accounts. The dataset includes:

User Profile Information : statuses_count, followers_count, friends_count, etc.
Temporal Features : account_age, created_at.
Engagement Metrics : retweet_to_like_ratio, engagement_rate.
Behavioral Indicators : duplicate_posts, mutual_connections.
You can find the dataset used for this project in the data/ directory:-  fake_twitter_accounts_final.csv
Installation
Prerequisites
•	Python 3.8 or higher
•	Git
Steps:
1.	Clone the repository
i)	git clone : https://github.com/AyushYadav76/Fake_Social_Media_Account_Detection
ii)	cd fake-social-media-account-detection
2)	Install dependencies
i)	pip install -r requirements.txt
3)	Download the pre-trained model:
•	Ensure the model.pkl file is present in the root directory. If not, you can train the model using the provided script
i)	python train_model.py

4)	Run the Flask app locally:
i)	python app.py
5)	Access the API at http://127.0.0.1:5000.

Usage
•	Testing Locally
•	You can test the API locally using curl or Postman.
•	Example Request with curl:
(1)	curl -X POST http://127.0.0.1:5000/predict \
(2)	-H "Content-Type: application/json" \
(3)	-d '{
(4)	  "account_age": 1000,
(5)	  "bio_length": 50,
(6)	  "profile_picture_present": 1,
(7)	  "default_profile_image": 0,
(8)	  "average_posts_per_day": 5.2,
(9)	  "retweet_to_like_ratio": 0.8,
(10)	  "engagement_rate": 0.6,
(11)	  "peak_activity_hour": 14,
(12)	  "clustering_coefficient": 0.4,
(13)	  "mutual_connection_ratio": 0.3,
(14)	  "spam_score": 0.1,
(15)	  "account_creation_year": 2015
(16)	}'
•	Example Response:
o	{
o	  "prediction": 0,
o	  "probability": 0.4005
o	}

API Endpoints
•	/predict (POST)
•	Description : Predicts whether a given account is fake or legitimate.
•	Request Body : JSON object with features like account_age, bio_length, etc.
•	Response : JSON object containing the prediction and probability.


Deployment
The app can be deployed to cloud platforms like Render , Heroku , or AWS . Follow these steps:
1.	Push your code to GitHub.
2.	Connect your GitHub repository to the deployment platform.
3.	Add environment variables if needed (e.g., paths to the model file).
4.	Deploy and access the public URL.
For example, on Render :
•	Go to Render and create a new Web Service.
•	Link your GitHub repository and specify the build command (pip install -r requirements.txt) and start command (python app.py).
Contributing
We welcome contributions! To contribute:

Fork the repository.
1)	Create a new branch (git checkout -b feature/your-feature).
2)	Commit your changes (git commit -m "Add feature")
3)	Push to the branch (git push origin feature/your-feature).
4)	Open a pull request.

License
This project is licensed under the MIT License . See the LICENSE file for details.

Acknowledgments
•	Inspiration and datasets were sourced from publicly available research on social media fraud detection.
•	Special thanks to the open-source community for their support and tools.

