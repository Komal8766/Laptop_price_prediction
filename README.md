
💻 Laptop Price Prediction – Machine Learning Project

This project builds a Machine Learning model to predict the price of a laptop based on its specifications. It uses data preprocessing, feature engineering, and regression models to estimate prices with high accuracy. The project is ideal for learning end-to-end ML workflow, including EDA, modeling, and deployment.


🚀 Project Overview

The goal is to predict laptop prices using features such as:
	•	Brand
	•	Processor Type
	•	RAM & Storage
	•	GPU
	•	Operating System
	•	Screen Specifications
	•	Weight
	•	Touchscreen / IPS Display
	•	Battery Backup

A machine learning model is trained to understand how these specs influence the market price.


📂 Project Structure

📁 Laptop-Price-Prediction
│
├── data/
│   └── laptop_data.csv
│
├── notebook/
│   └── Laptop_Price_Prediction.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── app/
│   ├── app.py
│   └── streamlit
│
└── README.md



🔍 Steps Performed

1. Data Cleaning
	•	Handling missing values
	•	Converting categorical data
	•	Removing duplicates
	•	Standardizing units (e.g., weight, storage)

2. Exploratory Data Analysis (EDA)
	•	Visualizing relationships between specs & price
	•	Understanding brand-level variations
	•	Outlier detection
	•	Feature correlation mapping

3. Feature Engineering
	•	Extracting important attributes
	•	Creating combined features
	•	One-hot encoding for categorical variables
	•	Scaling numerical variables

4. Model Building

Models tested:
	•	Linear Regression
	•	Random Forest Regressor
	•	Gradient Boosting
	•	XGBoost / CatBoost / LightGBM

Selected best model based on:
	•	R² Score
	•	RMSE
	•	Cross-validation accuracy

5. Deployment (Optional)

A simple Flask web app is added to allow users to input laptop specs and get predicted price.


🧠 Technologies Used
	•	Python
	•	Pandas, NumPy
	•	Scikit-Learn
	•	Matplotlib, Seaborn
	•	Flask (for deployment)
	•	Pickle (model serialization)


📊 Model Performance

Model	R² Score	RMSE
Linear Regression	~0.75	High
Random Forest	~0.88	Lower
Gradient Boosting	~0.90	Low
XGBoost (Best)	~0.92	Lowest

(Values may vary depending on dataset.)


🖥️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/your-username/laptop-price-prediction.git
cd laptop-price-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Notebook

jupyter notebook

4️⃣ Run the Web App (if included)

python app/app.py


🎯 Key Insights
	•	Processor, RAM, and GPU significantly impact price
	•	SSD storage has higher effect than HDD
	•	Premium brands show higher baseline prices
	•	Lightweight laptops are priced higher


👨‍💻 Future Improvements
	•	Add deep learning models
	•	Deploy using Streamlit or FastAPI
	•	Integrate real-time laptop data scraping
	•	Build price recommendation system


⭐ Author

Komal Brahmadev Murkute
Machine Learning & Data Science Enthusiast

