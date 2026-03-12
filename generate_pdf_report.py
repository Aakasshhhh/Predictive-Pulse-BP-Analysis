from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime

# Create PDF document
pdf_filename = 'PROJECT_DOCUMENTATION.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                        rightMargin=0.75*inch,
                        leftMargin=0.75*inch,
                        topMargin=0.75*inch,
                        bottomMargin=0.75*inch)

# Container for PDF elements
elements = []

# Get standard styles
styles = getSampleStyleSheet()

# Create custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#DC143C'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#666666'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique'
)

heading1_style = ParagraphStyle(
    'CustomHeading1',
    parent=styles['Heading1'],
    fontSize=14,
    textColor=colors.HexColor('#2C3E50'),
    spaceAfter=6,
    spaceBefore=6,
    fontName='Helvetica-Bold'
)

heading2_style = ParagraphStyle(
    'CustomHeading2',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=colors.HexColor('#34495E'),
    spaceAfter=4,
    spaceBefore=4,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    fontName='Helvetica'
)

# Title and Subtitle
elements.append(Paragraph('🫀 Predictive Pulse – Blood Pressure Prediction System', title_style))
elements.append(Paragraph('Comprehensive Project Documentation', subtitle_style))
elements.append(Spacer(1, 0.2*inch))

# Table of Contents
elements.append(Paragraph('📋 Table of Contents', heading1_style))
toc_items = [
    '• Project Overview',
    '• Features',
    '• Technologies Used',
    '• Project Structure',
    '• Installation',
    '• Usage',
    '• Data Analysis',
    '• Model Training',
    '• Web Application',
    '• Contributing',
    '• License'
]
for item in toc_items:
    elements.append(Paragraph(item, body_style))
elements.append(Spacer(1, 0.3*inch))

# Project Overview
elements.append(PageBreak())
elements.append(Paragraph('📌 Project Overview', heading1_style))
overview_text = """Predictive Pulse is an intelligent machine learning-based web application designed to predict a patient's blood pressure category using various health-related features. The system analyzes patient information and classifies blood pressure into four stages:
<br/><br/>
<b>• Normal Blood Pressure (Low Risk)</b><br/>
<b>• Stage 1 Hypertension (Moderate Risk)</b><br/>
<b>• Stage 2 Hypertension (High Risk)</b><br/>
<b>• Hypertensive Crisis (Critical Risk)</b><br/>
<br/>
The application aims to assist in early detection of hypertension risk, helping healthcare professionals and patients make informed decisions about their cardiovascular health."""
elements.append(Paragraph(overview_text, body_style))
elements.append(Spacer(1, 0.2*inch))

# Features
elements.append(Paragraph('🎯 Features', heading1_style))
features = [
    '<b>Machine Learning Prediction:</b> Utilizes Logistic Regression model trained on patient health data',
    '<b>Web-Based Interface:</b> User-friendly Flask web application for easy access',
    '<b>Comprehensive Health Assessment:</b> Considers multiple health factors including age, gender, family history, symptoms, and vital signs',
    '<b>Risk Classification:</b> Provides clear risk assessment with actionable insights',
    '<b>Data Visualization:</b> Exploratory data analysis with matplotlib and seaborn',
    '<b>Real-time Prediction:</b> Instant results based on user input'
]
for feature in features:
    elements.append(Paragraph('• ' + feature, body_style))
elements.append(Spacer(1, 0.2*inch))

# Technologies Used
elements.append(Paragraph('🛠 Technologies Used', heading1_style))

elements.append(Paragraph('Backend', heading2_style))
backend_tech = [
    '<b>Python 3.x</b> - Programming language',
    '<b>Flask</b> - Web framework for the application',
    '<b>Scikit-learn</b> - Machine learning library for model training and prediction',
    '<b>Joblib</b> - Model serialization and loading'
]
for tech in backend_tech:
    elements.append(Paragraph('• ' + tech, body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('Data Processing & Analysis', heading2_style))
data_tech = [
    '<b>Pandas</b> - Data manipulation and analysis',
    '<b>NumPy</b> - Numerical computing',
    '<b>Matplotlib</b> - Data visualization',
    '<b>Seaborn</b> - Statistical data visualization'
]
for tech in data_tech:
    elements.append(Paragraph('• ' + tech, body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('Frontend', heading2_style))
frontend_tech = [
    '<b>HTML5</b> - Web page structure',
    '<b>CSS3</b> - Styling and layout'
]
for tech in frontend_tech:
    elements.append(Paragraph('• ' + tech, body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('Development Tools', heading2_style))
dev_tech = ['<b>Jupyter Notebook</b> - Interactive data analysis and visualization']
for tech in dev_tech:
    elements.append(Paragraph('• ' + tech, body_style))
elements.append(Spacer(1, 0.2*inch))

# Project Structure
elements.append(PageBreak())
elements.append(Paragraph('📂 Project Structure', heading1_style))
project_structure = """Predictive-Pulse-BP-Analysis/<br/>
│<br/>
├── app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Main Flask application<br/>
├── Eda.ipynb &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Exploratory Data Analysis notebook<br/>
├── Data/<br/>
│   ├── clean_patient_data.csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Processed dataset<br/>
│   ├── patient_data .csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Raw dataset<br/>
│   └── src data cleaning.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Data cleaning script<br/>
├── model/<br/>
│   └── modelbuild.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Model training script<br/>
├── static/<br/>
│   └── style.css &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # CSS styling<br/>
└── templates/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;└── index.html &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Main web page template"""
elements.append(Paragraph(project_structure, ParagraphStyle('Code', parent=styles['Normal'], 
                                                             fontName='Courier', fontSize=8, 
                                                             textColor=colors.HexColor('#333333'))))
elements.append(Spacer(1, 0.2*inch))

# Installation
elements.append(PageBreak())
elements.append(Paragraph('⚙️ Installation', heading1_style))

elements.append(Paragraph('Prerequisites', heading2_style))
elements.append(Paragraph('• Python 3.7 or higher', body_style))
elements.append(Paragraph('• pip package manager', body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('Step-by-Step Installation', heading2_style))
elements.append(Paragraph('1. Clone the repository', body_style))
elements.append(Paragraph('git clone https://github.com/your-username/Predictive-Pulse-BP-Analysis.git<br/>cd Predictive-Pulse-BP-Analysis', body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('2. Create a virtual environment', body_style))
elements.append(Paragraph('python -m venv venv<br/>source venv/bin/activate  # On Windows: venv\\Scripts\\activate', body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('3. Install required packages', body_style))
elements.append(Paragraph('pip install -r requirements.txt<br/><br/>If requirements.txt does not exist, install packages manually:<br/>pip install flask scikit-learn pandas numpy matplotlib seaborn joblib', body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('4. Ensure model file is present', body_style))
elements.append(Paragraph('• The trained model logreg_model.pkl should be in the root directory<br/>• If missing, run: python model/modelbuild.py', body_style))
elements.append(Spacer(1, 0.2*inch))

# Usage
elements.append(Paragraph('🚀 Usage', heading1_style))

elements.append(Paragraph('Running the Web Application', heading2_style))
elements.append(Paragraph('1. Start the Flask application<br/>python app.py', body_style))
elements.append(Spacer(1, 0.05*inch))

elements.append(Paragraph('2. Open your web browser and navigate to<br/>http://127.0.0.1:5000/', body_style))
elements.append(Spacer(1, 0.05*inch))

elements.append(Paragraph('3. Enter patient information in the web form including:', body_style))
patient_info = [
    'Age',
    'Gender',
    'Family history of hypertension',
    'Current medication status',
    'Symptoms (breath shortness, vision changes, nose bleeding)',
    'Blood pressure readings (systolic/diastolic)',
    'Lifestyle factors (diet, medical care)'
]
for info in patient_info:
    elements.append(Paragraph('• ' + info, body_style))
elements.append(Spacer(1, 0.05*inch))

elements.append(Paragraph('4. Get instant prediction of blood pressure category and risk level', body_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph('Running Data Analysis', heading2_style))
elements.append(Paragraph('1. Open the Jupyter notebook<br/>jupyter notebook Eda.ipynb', body_style))
elements.append(Spacer(1, 0.05*inch))

elements.append(Paragraph('2. Execute cells to perform exploratory data analysis and visualize the dataset', body_style))
elements.append(Spacer(1, 0.2*inch))

# Data Analysis
elements.append(PageBreak())
elements.append(Paragraph('📊 Data Analysis', heading1_style))
elements.append(Paragraph('The project includes comprehensive exploratory data analysis in Eda.ipynb:', body_style))
elements.append(Spacer(1, 0.05*inch))

data_analysis_points = [
    '<b>Data Loading:</b> Import and examine the clean patient dataset',
    '<b>Statistical Summary:</b> Descriptive statistics of all features',
    '<b>Data Visualization:</b> Distribution plots, correlation analysis, categorical feature analysis',
    '<b>Data Quality Assessment:</b> Check for missing values, duplicates, and outliers'
]
for point in data_analysis_points:
    elements.append(Paragraph('• ' + point, body_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph('Dataset Features', heading2_style))
dataset_features = [
    'Age', 'Gender', 'Family History', 'Medication Status',
    'Symptom Severity', 'Respiratory Symptoms', 'Vision Changes',
    'Nose Bleeding', 'Diagnosis Timeline', 'Blood Pressure Measurements',
    'Dietary Habits', 'Medical Care Access'
]
for feature in dataset_features:
    elements.append(Paragraph('• ' + feature, body_style))
elements.append(Spacer(1, 0.2*inch))

# Model Training
elements.append(Paragraph('🧠 Model Training', heading1_style))

elements.append(Paragraph('Model Building Process (model/modelbuild.py)', heading2_style))
model_process = [
    'Data Loading: Import cleaned patient data',
    'Preprocessing: Handle missing values and data cleaning',
    'Feature Selection: Select relevant health indicators',
    'Train-Test Split: 80-20 split with random state for reproducibility',
    'Model Selection: Logistic Regression with max_iter=1000',
    'Training: Fit model on training data',
    'Evaluation: Accuracy score, Classification report, Confusion matrix',
    'Model Saving: Serialize trained model using joblib'
]
for i, step in enumerate(model_process, 1):
    elements.append(Paragraph(f'{i}. {step}', body_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph('Model Performance', heading2_style))
elements.append(Paragraph('• Algorithm: Logistic Regression', body_style))
elements.append(Paragraph('• Target Classes: 4 blood pressure categories (0-3)', body_style))
elements.append(Spacer(1, 0.2*inch))

# Web Application
elements.append(PageBreak())
elements.append(Paragraph('🌐 Web Application', heading1_style))

elements.append(Paragraph('Flask App Structure (app.py)', heading2_style))
elements.append(Paragraph('Routes:', body_style))
elements.append(Paragraph('• /: Home page with prediction form', body_style))
elements.append(Paragraph('• /predict: POST endpoint for prediction requests', body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph('Features:', body_style))
web_features = [
    'Form data validation',
    'Model prediction integration',
    'Error handling',
    'Result rendering with risk assessment'
]
for feature in web_features:
    elements.append(Paragraph('• ' + feature, body_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph('User Interface (templates/index.html, static/style.css)', heading2_style))
ui_features = [
    '<b>Responsive Design:</b> Works on desktop and mobile devices',
    '<b>Intuitive Form:</b> Easy-to-fill health assessment questionnaire',
    '<b>Clear Results:</b> Prominent display of prediction and risk level',
    '<b>Professional Styling:</b> Clean, medical-themed design'
]
for feature in ui_features:
    elements.append(Paragraph('• ' + feature, body_style))
elements.append(Spacer(1, 0.2*inch))

# Contributing
elements.append(Paragraph('🤝 Contributing', heading1_style))
elements.append(Paragraph('We welcome contributions to improve Predictive Pulse! Here\'s how you can help:', body_style))
elements.append(Spacer(1, 0.05*inch))

contributing_steps = [
    'Fork the repository',
    'Create a feature branch: git checkout -b feature-name',
    'Make your changes and test thoroughly',
    'Commit your changes: git commit -am \'Add new feature\'',
    'Push to the branch: git push origin feature-name',
    'Submit a Pull Request'
]
for i, step in enumerate(contributing_steps, 1):
    elements.append(Paragraph(f'{i}. {step}', body_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph('Areas for Improvement', heading2_style))
improvements = [
    'Add more machine learning algorithms',
    'Implement cross-validation',
    'Add more comprehensive data validation',
    'Improve UI/UX design',
    'Add user authentication',
    'Implement data persistence'
]
for improvement in improvements:
    elements.append(Paragraph('• ' + improvement, body_style))
elements.append(Spacer(1, 0.2*inch))

# Future Improvements
elements.append(PageBreak())
elements.append(Paragraph('🚀 Future Improvements', heading1_style))
future_items = [
    'Add more medical features',
    'Improve model accuracy using advanced algorithms',
    'Deploy the application online',
    'Add patient dashboard'
]
for item in future_items:
    elements.append(Paragraph('• ' + item, body_style))
elements.append(Spacer(1, 0.2*inch))

# License
elements.append(Paragraph('📄 License', heading1_style))
elements.append(Paragraph('This project is licensed under the MIT License - see the LICENSE file for details.', body_style))
elements.append(Spacer(1, 0.2*inch))

# Contact
elements.append(Paragraph('📞 Contact', heading1_style))
elements.append(Paragraph('For questions, suggestions, or collaboration opportunities:', body_style))
contact_info = [
    'Project Maintainers: Akash Verma, Shivant Kumar Sahu, Himanshu Aryan, Anjali Kumari',
    'GitHub Issues: Create an issue at the repository'
]
for info in contact_info:
    elements.append(Paragraph('• ' + info, body_style))
elements.append(Spacer(1, 0.2*inch))

# Disclaimer
elements.append(Paragraph('⚠️ Disclaimer', heading1_style))
disclaimer_text = 'This application is for educational and informational purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.'
elements.append(Paragraph(disclaimer_text, body_style))

# Footer
elements.append(Spacer(1, 0.3*inch))
footer_text = f'<i>Document Generated on {datetime.now().strftime("%B %d, %Y")}</i>'
footer = Paragraph(footer_text, ParagraphStyle('FooterStyle', parent=styles['Normal'], 
                                               fontSize=9, alignment=TA_CENTER, 
                                               textColor=colors.HexColor('#999999')))
elements.append(footer)

# Build PDF
doc.build(elements)
print(f'✅ Professional PDF document created successfully: {pdf_filename}')
