import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))


# Function to make predictions
def predict(features):
    prediction = model.predict(features)
    return prediction


def main():
    # Title of the app
    st.title("Mental Health Prediction App")

    # Set background image
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('C:/Users/admin/Downloads/mental health.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Subtitle
    st.write("This app predicts mental health based on provided features.")

    # Add a button to show input fields for features
    if st.button("Enter Features"):
        # Add input fields for features
        age = st.number_input("Age", min_value=18, max_value=60, step=1, value=25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        self_employed = st.radio("Are you self-employed?", ["Yes", "No"])
        family_history = st.radio("Do you have a family history of mental health conditions?", ["Yes", "No"])
        treatment = st.radio("Have you sought treatment for a mental health condition?", ["Yes", "No"])
        work_interfere = st.selectbox(
            "If you have a mental health condition, do you feel that it interferes with your work?",
            ["Often", "Sometimes", "Rarely", "Never"])
        no_employees = st.selectbox("How many employees does your company or organization have?",
                                    ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"])
        remote_work = st.radio("Do you work remotely (outside of an office) at least 50% of the time?",
                               ["Yes", "No"])
        tech_company = st.radio("Is your employer primarily a tech company/organization?",
                                ["Yes", "No"])
        benefits = st.radio("Does your employer provide mental health benefits?",
                            ["Yes", "No", "Not sure"])
        care_options = st.selectbox("Do you know the options for mental health care your employer provides?",
                                    ["Yes", "No", "Not sure"])
        wellness_program = st.radio(
            "Has your employer ever discussed mental health as part of an employee wellness program?",
            ["Yes", "No", "Don't know"])
        seek_help = st.radio(
            "Does your employer provide resources to learn more about mental health issues and how to seek help?",
            ["Yes", "No", "Don't know"])
        anonymity = st.radio(
            "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?",
            ["Yes", "No", "Don't know"])
        leave = st.selectbox("How easy is it for you to take medical leave for a mental health condition?",
                             ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
        mental_health_consequence = st.radio(
            "Do you think that discussing a mental health issue with your employer would have negative consequences?",
            ["Yes", "No", "Maybe"])
        phys_health_consequence = st.radio(
            "Do you think that discussing a physical health issue with your employer would have negative consequences?",
            ["Yes", "No", "Maybe"])
        coworkers = st.radio("Would you be willing to discuss a mental health issue with your coworkers?",
                             ["Yes", "No", "Maybe"])
        supervisor = st.radio("Would you be willing to discuss a mental health issue with your direct supervisor(s)?",
                              ["Yes", "No", "Maybe"])
        mental_health_interview = st.radio(
            "Would you bring up a mental health issue with a potential employer in an interview?",
            ["Yes", "No", "Maybe"])
        phys_health_interview = st.radio(
            "Would you bring up a physical health issue with a potential employer in an interview?",
            ["Yes", "No", "Maybe"])
        mental_vs_physical = st.radio(
            "Do you feel that your employer takes mental health as seriously as physical health?",
            ["Yes", "No", "Don't know"])
        obs_consequence = st.radio(
            "Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?",
            ["Yes", "No"])

        # Add more input fields for other features as needed

        # Make prediction button
        if st.button("Predict"):
            # Convert input into feature array
            features = [[age, gender, self_employed, family_history, treatment, work_interfere, no_employees,
                         remote_work, tech_company, benefits, care_options, wellness_program, seek_help,
                         anonymity, leave, mental_health_consequence, phys_health_consequence, coworkers,
                         supervisor, mental_health_interview, phys_health_interview, mental_vs_physical,
                         obs_consequence]]  # Add more features here

            # Make predictions
            prediction = predict(features)

            # Display prediction
            st.write(f"Prediction: {prediction}")


if __name__ == '__main__':
    main()