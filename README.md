# 🔥 ML Mini Project: Algerian Forest Fire Classification

This mini-project builds an end-to-end machine learning pipeline to predict forest fires based on meteorological data from Algeria. It includes data preprocessing, feature engineering, model training using a Random Forest Classifier, and performance evaluation.

## 📁 Dataset Description

- **Source**: UCI Machine Learning Repository (Algerian Forest Fires Dataset)
- **Instances**: 244 samples
- **Regions**: Bejaia and Sidi Bel-abbes (122 each)
- **Period**: June 2012 – September 2012
- **Target**: `Classes` (fire or not fire)

## ⚙️ Features Used

- Temperature
- RH (Relative Humidity)
- WS (Wind Speed)
- Rain
- FFMC, DMC, DC, ISI (Fire Weather Indices)
- Region (Encoded)
- Classes (1 = fire, 0 = not fire)

## 📂 Project Structure

- `dataset_cleaning.ipynb`: Handles EDA, data cleaning, encoding, and feature scaling.
- `model_training.ipynb`: Trains and evaluates the Random Forest model.
- `Algerian_forest_fires_dataset.csv`: The dataset file.
- `README.md`: This documentation.

## 📊 Model Used

- **Algorithm**: Random Forest Classifier
- **Library**: scikit-learn
- **Metrics**: Accuracy Score, Confusion Matrix, Classification Report


