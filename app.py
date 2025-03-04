import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))


st.title("SMS Spam Detection application")
st.write('This is a Machine Learning application to classify sms as spam or ham.')
user_input= st.text_area("Enter SMS to classify",height=150)

if st.button("Classify"):
    if user_input:
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        result = model.predict(vectorized_data)
        if result[0]==0:
            st.write("This SMS is not spam.")
        else:
            st.write("This SMS is spam.")
    else:
        st.write("Please type email to classify")
