# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts California house prices using Machine Learning algorithms. It includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment through a Streamlit web application.

The objective is to build an end-to-end regression model capable of predicting house prices based on housing features.

---
Demo
<img width="1920" height="849" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/35bf22dd-9005-444a-8684-d0ee3783abfc" />
<img width="1920" height="945" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/a97f28be-ffad-474c-8451-ccac035e41c4" />
## 🚀 Features

- Exploratory Data Analysis (EDA)
- Data Visualization
- Data Preprocessing
- Multiple Machine Learning Models
- Model Evaluation
- Random Forest Regression
- Model Serialization using Joblib
- Interactive Streamlit Web Application

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## 📊 Dataset

This project uses the **California Housing Dataset** provided by Scikit-learn.

Features include:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

Target:

- House Price

---

## 🤖 Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

The **Random Forest Regressor** achieved the best performance and was selected for deployment.

## 📂 Project Structure

```
house-price-prediction/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── images/
│   └── app_screenshot.png
│
└── notebooks/
    └── House_Price_Prediction.ipynb
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

Move into the project folder:

```bash
cd house-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Model Workflow

1. Load Dataset
2. Perform Exploratory Data Analysis
3. Preprocess Data
4. Split Training and Testing Data
5. Train Multiple Models
6. Evaluate Performance
7. Save Best Model
8. Deploy using Streamlit

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Model Deployment on Cloud
- Docker Containerization
- User Authentication
- Real-time Data Integration

---

## 👨‍💻 Author

**Mohd Abdul Razzaq**

Machine Learning & AI Enthusiast

GitHub: https://github.com/arazzaq-forgit

LinkedIn: https://linkedin.com/in/mohd-abdul-razzaq
