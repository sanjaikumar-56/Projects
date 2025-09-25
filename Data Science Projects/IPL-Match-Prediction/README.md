# IPL Match Prediction Project

## 📋 Project Overview
This project aims to predict the winner of Indian Premier League (IPL) cricket matches using machine learning algorithms. The model analyzes historical match data to forecast match outcomes based on various features like team composition, toss decisions, venue, and past performance.

## 🎯 Objectives
- Predict IPL match winners using historical data (2008-2019)
- Compare multiple machine learning algorithms
- Identify key factors influencing match outcomes
- Build a deployable prediction model

## 📊 Dataset
- **Source**: IPL match data from 2008 to 2019
- **Records**: 756 matches with 18 features
- **Key Features**: Teams, venue, toss decisions, player performances, match results

## 🛠️ Technical Implementation

### Data Preprocessing
- Handled missing values and data inconsistencies
- Encoded categorical variables (teams, venues, cities)
- Feature engineering and normalization
- Removed irrelevant columns (umpires, player_of_match)

### Models Implemented
- Logistic Regression
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Decision Trees
- Random Forest
- XGBoost

### Key Steps
1. **Data Loading & Exploration**
2. **Data Cleaning & Feature Engineering**
3. **Model Training & Evaluation**
4. **Hyperparameter Tuning**
5. **Model Selection & Serialization**

## 📈 Results
The Random Forest classifier achieved the best performance with:
- **Accuracy**: [X]%
- **Precision**: [Y]%
- **Recall**: [Z]%

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install -r requirements.txt
