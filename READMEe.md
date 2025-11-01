# News Classification Project

This project classifies news articles into categories using machine learning.  
It was created as part of the 2501PTDS Data Science cohort.

## About the Project
We built a text classification model using Python and scikit-learn.  
The goal was to classify news articles into categories such as:
- Business  
- Technology  
- Education  
- Entertainment  
- Sports  

## Models Used
- Logistic Regression  
- Naive Bayes  
- Random Forest  

After testing the models, **Logistic Regression** performed best with about **98% accuracy**.  
We saved the best model and the TF-IDF vectorizer for future use in a Streamlit web app.

## Files in this Repository
- `Classification_project_Maponya.ipynb` — main notebook  
- `best_model.pkl` — saved best model  
- `vectorizer.pkl` — TF-IDF vectorizer  
- `Data/` — folder with processed data  

## How to Run
1. Open the notebook in Google Colab or Jupyter Notebook.  
2. Run the cells from top to bottom.  
3. To test the saved model, load the `.pkl` files and predict new articles.

---

**Author:** Maponya Masitenyane  
**Date:** November 2025
