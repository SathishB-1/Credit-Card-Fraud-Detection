## Credit Card Fraud Detection

## Overview:

This project aims to build a machine learning model to detect fraudulent credit card transactions using a Random Forest Classifier. The model is trained on a dataset containing historical transaction data, including both fraudulent and legitimate transactions.
The dataset consists of various features related to the transactions, and the goal is to predict whether a transaction is fraudulent or non-fraudulent.

## Dataset:

[drive link](https://drive.google.com/drive/folders/1DoLuRjhZgkwkHIEQ45upWYp2Y31TIdA4?usp=sharing)

The dataset used for training and testing the model includes the following columns:

cc_num: Credit card number (dropped for privacy reasons).

first, last, street, dob: Personal details (dropped for privacy).

trans_date_trans_time: Date and time of transaction (dropped).

trans_num: Transaction number (dropped).

is_fraud: Target variable indicating if the transaction is fraudulent (1 for fraud, 0 for non-fraud).

## Dataset Files:

fraudTrain.csv: The training dataset.

fraudTest.csv: The testing dataset.

## Steps Involved:

## 1. Data Preprocessing:
Drop irrelevant columns (such as personal information and transaction details).

Handle missing values by removing rows with NaN values.

Encode categorical features using one-hot encoding.

Scale the features using StandardScaler.

## 2. Modeling
Model: Random Forest Classifier

Class Weights: The model is trained with class_weight='balanced' to address class imbalance in fraud detection.

Evaluation Metrics: The model is evaluated using accuracy and the classification report.

## 3. Model Evaluation
The model's performance is evaluated using the accuracy score and classification report, which includes precision, recall, and F1-score.

## Installation and Usage

## 1. Clone the Repository
git clone https://github.com/yourusername/credit-card-fraud-detection.git

cd credit-card-fraud-detection

## 2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate  # For Windows

## 3. Install Dependencies
pip install -r requirements.txt

## Evaluation Metrics:

Precision: The fraction of relevant instances among the retrieved instances.

Recall: The fraction of relevant instances that have been retrieved.

F1-Score: The harmonic mean of precision and recall.

Accuracy: The fraction of correctly predicted instances.

## Benefits:

 1. Prevents Financial Loss:
Detects fraud early to stop unauthorized transactions before they cause damage.

2. Saves Money:
Reduces the costs of handling fraud and chargebacks for banks.

3. Better Customer Trust:
Ensures customers feel secure knowing their transactions are protected.

4. Automates Fraud Detection:
Speeds up the process and reduces human error by automatically detecting fraud.

5. Adapts to New Fraud Patterns:
The model can be retrained to keep up with new types of fraud.

6. Improves Accuracy:
Handles the common issue of fraud being rare in datasets, ensuring better predictions.

7. Real-Time Fraud Detection:
Flags fraud immediately, preventing losses in real-time.

8. Supports Security Standards:
Helps ensure compliance with industry regulations like PCI DSS.

## User Interface

![image alt](https://github.com/SathishB-1/Credit-Card-Fraud-Detection/blob/2bc4c5fc01ca7d5706a32a916ec32db3b84b5bfb/UI-1.png)
![image alt](https://github.com/SathishB-1/Credit-Card-Fraud-Detection/blob/72cfe05dc0bdb84c0a3509496fabac5362f1919b/UI-2.png)
