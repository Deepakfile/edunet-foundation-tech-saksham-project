import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import google.generativeai as genai
import requests
import json



st.set_page_config(page_title="Prediction of Disease Outbreaks By A.D.K",
                   layout="wide",
                   page_icon="🩺")

working_dir = os.path.dirname(os.path.abspath(__file__))


try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Error: Model files (.sav) not found. Please ensure they are in the same directory.")
    st.stop()


with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'AI Health Assistant 🤖'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'robot'],
                           default_index=0)


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction by Dr. A.D.K')

    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('No. of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    all_inputs_present = all([Pregnancies, Glucose, BloodPressure, SkinThickness,
                              Insulin, BMI, DiabetesPedigreeFunction, Age])

    if st.button('Diabetes Test Result'):
        if not all_inputs_present:
            st.warning("Please enter all required values for prediction.")
        else:
            try:
                user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure,
                                                 SkinThickness, Insulin, BMI,
                                                 DiabetesPedigreeFunction, Age]]
                diab_prediction = diabetes_model.predict([user_input])
                diab_diagnosis = ' The person is diabetic' if diab_prediction[0] == 1 else ' The person is not diabetic'
            except ValueError:
                diab_diagnosis = ' Error: Please ensure all inputs are valid numbers.'
    st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction by Dr. A.D.K')

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex (1=male, 0=female)')
    with col3: cp = st.text_input('Chest Pain types (0-3)')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)')
    with col1: restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    with col2: thalach = st.text_input('Maximum Heart Rate achieved')
    with col3: exang = st.text_input('Exercise Induced Angina (1=Yes, 0=No)')
    with col1: oldpeak = st.text_input('ST depression induced by exercise')
    with col2: slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3: ca = st.text_input('Major vessels colored by flourosopy (0-3)')
    with col1: thal = st.text_input('Thal: 0=normal; 1=fixed defect; 2=reversable defect')

    heart_diagnosis = ''
    all_inputs_present = all([age, sex, cp, trestbps, chol, fbs, restecg,
                              thalach, exang, oldpeak, slope, ca, thal])

    if st.button('Heart Disease Test Result'):
        if not all_inputs_present:
            st.warning("Please enter all required values for prediction.")
        else:
            try:
                user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs,
                                                 restecg, thalach, exang, oldpeak,
                                                 slope, ca, thal]]
                heart_prediction = heart_disease_model.predict([user_input])
                heart_diagnosis = ' The person has heart disease' if heart_prediction[0] == 1 else ' The person does not have any heart disease'
            except ValueError:
                heart_diagnosis = ' Error: Please ensure all inputs are valid numbers.'
    st.success(heart_diagnosis)


if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction by Dr. A.D.K")

    col1, col2, col3, col4, col5 = st.columns(5)
    fields = ['Fo', 'Fhi', 'Flo', 'Jitter%', 'JitterAbs', 'RAP', 'PPQ', 'DDP',
              'Shimmer', 'Shimmer_dB', 'APQ3', 'APQ5', 'APQ', 'DDA',
              'NHR', 'HNR', 'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE']
    values = []

    for i, f in enumerate(fields):
        with [col1, col2, col3, col4, col5][i % 5]:
            values.append(st.text_input(f))

    parkinsons_diagnosis = ''
    all_inputs_present = all(values)

    if st.button("Parkinson's Test Result"):
        if not all_inputs_present:
            st.warning("Please enter all required values for prediction.")
        else:
            try:
                user_input = [float(x) for x in values]
                parkinsons_prediction = parkinsons_model.predict([user_input])
                parkinsons_diagnosis = " The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else " The person does not have Parkinson's disease"
            except ValueError:
                parkinsons_diagnosis = ' Error: Please ensure all inputs are valid numbers.'
    st.success(parkinsons_diagnosis)






from openai import OpenAI
import streamlit as st
if "reply" not in st.session_state:
    st.session_state.reply = ""


if selected == "AI Health Assistant 🤖":
    st.title("🤖 Dr. A.D.K - AI Health & Diet Advisor.")
    st.write("Ask anything related to health, diseases, diet, or lifestyle.")
    st.code("Sugar wale ko kya khana chahiye?\nHeart patient ke liye best diet kya hai?")

    question = st.text_input("Apna sawal likhiye (Health related only):")

    if st.button("Ask Dr. A.D.K"):
        if question.strip() == "":
            st.warning(" Pehle apna sawal likhiye.")
        else:
            try:
                # Using OpenRouter’s OpenAI-compatible API client
                client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",  
                    api_key=st.secrets["OPENROUTER_API_KEY"]
                )

                prompt = f"""
                You are Dr. A.D.K, a professional AI medical assistant.
                You can only answer questions related to health, diseases, diet, or lifestyle.
                If the user asks about anything outside these topics
                (like coding, politics, movies, or history),
                politely reply: "I'm sorry, I am Dr. A.D.K, and I can only answer health-related questions."
                Always reply in the same language that the user used.

                Question: {question}
                """

                with st.spinner("🤖 Dr. A.D.K soch rahe hain..."):
                    response = client.chat.completions.create(
                        model="minimax/minimax-m2",  
                        messages=[{"role": "user", "content": prompt}]
                    )

                    st.session_state.reply = response.choices[0].message.content.strip()

            except Exception as e:
                st.session_state.reply = f"Unexpected Error: {e}"

    if st.session_state.reply:
        st.success(st.session_state.reply)

            










