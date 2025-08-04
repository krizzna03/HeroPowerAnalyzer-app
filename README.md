# 🦸‍♂️ Power Tier Analyzer

A machine learning-powered application that classifies Marvel characters into **power tiers** (like *Metahuman*, *Powerhouse*, *Herald*, etc.) based on their feats, popularity, and comic appearances.

> ✅ Successfully deployed | 🔥 ML + Marvel Universe + Deployment

---

## 📊 Project Summary

This project demonstrates:
- Data preprocessing and cleaning from a custom Marvel dataset
- Feature-based classification using Scikit-learn models
- Deployment via Streamlit/Flask (based on what you used)
- A clean, user-friendly interface for predictions

---

## 🧠 Features Used
The model predicts the `Power_Tier` using:
- `Feat_Score_1_to_10`: Numeric rating of character feats
- `Fan_Rating_1_to_10`: Average fan popularity
- `Comic_Appearances_Approx`: Total comic appearances

---

## 📂 Dataset Overview

| Character       | Feat Score | Fan Rating | Comic Appearances | Power Tier |
|----------------|------------|------------|-------------------|------------|
| Captain America| 3.0        | 9.2        | 11000             | Metahuman  |
| Iron Man       | 6.0        | 9.5        | 10500             | Powerhouse |
| Thor           | 8.0        | 9.3        | 8000              | Herald     |
| Spider-Man     | 4.0        | 9.8        | 12500             | Metahuman  |

---

## 🛠️ Tech Stack

- **Language**: Python 3.10
- **Libraries**: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- **Model**: Random Forest Classifier / Logistic Regression *(update based on your code)*
- **Deployment**: Streamlit / Flask *(please confirm)*
- **Hosting**: Streamlit Cloud / Render / Hugging Face *(please confirm)*

---

## 🖥️ How to Run the App Locally

```bash
git clone https://github.com/yourusername/power-tier-analyzer.git
cd power-tier-analyzer

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
streamlit run app.py
