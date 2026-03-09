# 🫀 Predictive Pulse – Blood Pressure Prediction System

## � Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Data Analysis](#-data-analysis)
- [Model Training](#-model-training)
- [Web Application](#-web-application)
- [Contributing](#-contributing)
- [License](#-license)

## 📌 Project Overview

Predictive Pulse is an intelligent machine learning-based web application designed to predict a patient's blood pressure category using various health-related features. The system analyzes patient information and classifies blood pressure into four stages:

- **Normal Blood Pressure** (Low Risk)
- **Stage 1 Hypertension** (Moderate Risk)
- **Stage 2 Hypertension** (High Risk)
- **Hypertensive Crisis** (Critical Risk)

The application aims to assist in early detection of hypertension risk, helping healthcare professionals and patients make informed decisions about their cardiovascular health.

## 🎯 Features

- **Machine Learning Prediction**: Utilizes Logistic Regression model trained on patient health data
- **Web-Based Interface**: User-friendly Flask web application for easy access
- **Comprehensive Health Assessment**: Considers multiple health factors including age, gender, family history, symptoms, and vital signs
- **Risk Classification**: Provides clear risk assessment with actionable insights
- **Data Visualization**: Exploratory data analysis with matplotlib and seaborn
- **Real-time Prediction**: Instant results based on user input

## 🛠 Technologies Used

### Backend
- **Python 3.x**
- **Flask** - Web framework for the application
- **Scikit-learn** - Machine learning library for model training and prediction
- **Joblib** - Model serialization and loading

### Data Processing & Analysis
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization

### Frontend
- **HTML5** - Web page structure
- **CSS3** - Styling and layout

### Development Tools
- **Jupyter Notebook** - Interactive data analysis and visualization

## 📂 Project Structure

```
Predictive-Pulse-BP-Analysis/
│
├── app.py                          # Main Flask application
├── Eda.ipynb                       # Exploratory Data Analysis notebook
├── index.html                      # Static HTML page (if used)
├── README.md                       # Project documentation
│
├── Data/
│   ├── clean_patient_data.csv      # Processed dataset
│   ├── patient_data .csv           # Raw dataset
│   └── src data cleaning.py        # Data cleaning script (duplicate of app.py)
│
├── model/
│   └── modelbuild.py               # Model training script
│
├── static/
│   └── style.css                   # CSS styling for the web app
│
└── templates/
    └── index.html                  # Main web page template
```

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Predictive-Pulse-BP-Analysis.git
   cd Predictive-Pulse-BP-Analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, install the following packages manually:
   ```bash
   pip install flask scikit-learn pandas numpy matplotlib seaborn joblib
   ```

4. **Ensure model file is present**
   - The trained model `logreg_model.pkl` should be in the root directory
   - If missing, run the model training script: `python model/modelbuild.py`

## 🚀 Usage

### Running the Web Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to**
   ```
   http://127.0.0.1:5000/
   ```

3. **Enter patient information** in the web form including:
   - Age
   - Gender
   - Family history of hypertension
   - Current medication status
   - Symptoms (breath shortness, vision changes, nose bleeding)
   - Blood pressure readings (systolic/diastolic)
   - Lifestyle factors (diet, medical care)

4. **Get instant prediction** of blood pressure category and risk level

### Running Data Analysis

1. **Open the Jupyter notebook**
   ```bash
   jupyter notebook Eda.ipynb
   ```

2. **Execute cells** to perform exploratory data analysis and visualize the dataset

## 📊 Data Analysis

The project includes comprehensive exploratory data analysis in `Eda.ipynb`:

- **Data Loading**: Import and examine the clean patient dataset
- **Statistical Summary**: Descriptive statistics of all features
- **Data Visualization**:
  - Distribution plots for numerical features
  - Correlation analysis between variables
  - Categorical feature analysis
- **Data Quality Assessment**: Check for missing values, duplicates, and outliers

### Dataset Features
- Age
- Gender
- Family History
- Medication Status
- Symptom Severity
- Respiratory Symptoms
- Vision Changes
- Nose Bleeding
- Diagnosis Timeline
- Blood Pressure Measurements
- Dietary Habits
- Medical Care Access

## 🧠 Model Training

### Model Building Process (`model/modelbuild.py`)

1. **Data Loading**: Import cleaned patient data
2. **Preprocessing**: Handle missing values and data cleaning
3. **Feature Selection**: Select relevant health indicators
4. **Train-Test Split**: 80-20 split with random state for reproducibility
5. **Model Selection**: Logistic Regression with max_iter=1000
6. **Training**: Fit model on training data
7. **Evaluation**:
   - Accuracy score
   - Classification report
   - Confusion matrix
8. **Model Saving**: Serialize trained model using joblib

### Model Performance
- **Algorithm**: Logistic Regression
- **Accuracy**: [Insert accuracy from training]
- **Target Classes**: 4 blood pressure categories (0-3)

## 🌐 Web Application

### Flask App Structure (`app.py`)

- **Routes**:
  - `/`: Home page with prediction form
  - `/predict`: POST endpoint for prediction requests

- **Features**:
  - Form data validation
  - Model prediction integration
  - Error handling
  - Result rendering with risk assessment

### User Interface (`templates/index.html`, `static/style.css`)

- **Responsive Design**: Works on desktop and mobile devices
- **Intuitive Form**: Easy-to-fill health assessment questionnaire
- **Clear Results**: Prominent display of prediction and risk level
- **Professional Styling**: Clean, medical-themed design

## 🤝 Contributing

We welcome contributions to improve Predictive Pulse! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -am 'Add new feature'`
5. **Push to the branch**: `git push origin feature-name`
6. **Submit a Pull Request**

### Areas for Improvement
- Add more machine learning algorithms
- Implement cross-validation
- Add more comprehensive data validation
- Improve UI/UX design
- Add user authentication
- Implement data persistence

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions, suggestions, or collaboration opportunities:
- **Project Maintainers**: [Your Name/Team]
- **GitHub Issues**: [Create an issue](https://github.com/your-username/Predictive-Pulse-BP-Analysis/issues)

---

**Disclaimer**: This application is for educational and informational purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

pip install -r requirements.txt

Run the Flask app

python app.py

---

## 📈 Model Performance

The Logistic Regression model is trained on the processed dataset and evaluated using accuracy metrics.

---

## 🚀 Future Improvements

* Add more medical features
* Improve model accuracy using advanced algorithms
* Deploy the application online
* Add patient dashboard

---

## 👨‍💻 Author
Akash Verma
Shivant Kumar Sahu
Himanshu Aryan
Anjali Kumari
