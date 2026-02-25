
# 📱 Fake Instagram Account Detection using Machine Learning

## 📌 Overview

Fake Instagram accounts are widely used for spam, scams, fake engagement, and spreading misinformation.
This project uses Machine Learning algorithms to classify Instagram accounts as **Real** or **Fake** based on profile-level features.
The system analyzes account characteristics and predicts authenticity using binary classification models.

Dataset used in this project is from Kaggle: [https://www.kaggle.com/datasets/rezaunderfit/instagram-fake-and-real-accounts-dataset](https://www.kaggle.com/datasets/rezaunderfit/instagram-fake-and-real-accounts-dataset) ([遇见数据集][1])

## 🎯 Objective

To develop a predictive machine learning model that accurately detects fake Instagram accounts and helps improve social media security.


## 📊 Dataset Information

* **Source:** Kaggle – Instagram Fake and Real Accounts Dataset ([遇见数据集][1])
* **Number of Records:** *Mention actual number*
* **Target Variable:**

  * `0` → Real Account
  * `1` → Fake Account
* **Features Used:**

  * Profile picture presence
  * Username length and numeric content
  * Bio (description) length
  * Number of posts
  * Number of followers
  * Number of accounts followed (following)
  * External URL presence
  * Profile privacy status
  * Followers–following ratio
  * Other profile activity metrics


## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Environment:** Jupyter Notebook / VS Code

---

## ⚙️ Project Workflow

1. **Data Collection**
2. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical features
   * Feature scaling
3. **Exploratory Data Analysis (EDA)**
4. **Feature Engineering**
5. **Model Training**
6. **Model Evaluation**
7. **Prediction**

---

## 🤖 Machine Learning Models Used

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)

*(Add any additional models you tried)*

---

## 📈 Evaluation Metrics

The following metrics were used to assess model performance:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**

*(Include your actual results in a table if available)*

---

## 📊 Results

The model trained on the dataset achieved high performance in classifying real and fake Instagram accounts.
Random Forest (or whichever model performed best) demonstrated the strongest accuracy and balance between metrics.

*(Replace with your actual model performance numbers here)*

Example:

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 88%      | 85%       | 90%    | 87%      |
| Random Forest       | **92%**  | 90%       | 93%    | 91%      |
| SVM                 | 90%      | 88%       | 92%    | 90%      |

---

## 🚀 How to Run the Project

```bash
git clone https://github.com/your-username/fake-instagram-detection.git
cd fake-instagram-detection
pip install -r requirements.txt
jupyter notebook
```

Run the notebook to see data exploration, model training, and predictions.

---

## 💡 Key Learnings

* Worked with real social media profile data to solve a binary classification problem.
* Applied data preprocessing and feature engineering techniques.
* Gained hands-on experience with machine learning model training and evaluation.
* Learned how to interpret and compare different performance metrics.
