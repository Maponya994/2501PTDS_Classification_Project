import streamlit as st
import pickle

# Load the saved model and vectorizer
model = pickle.load(open('best_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Title for the app
st.title("News Category Classifier")

st.write("This app predicts the category of a news article using machine learning.")
st.write("Models used: Logistic Regression, Naive Bayes, Random Forest")

# User input
user_input = st.text_area("Enter a news article below:")

# Predict button
if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]
        st.success(f"The predicted category is: **{prediction}**")
