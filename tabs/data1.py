import streamlit as st
def app(df):
    ########################################What is Coronary thrombosis?#################################################################

    st.title("What is Coronary thrombosis?")
    st.markdown(
        """
         Coronary Thrombosis is a heart disease which occurs due to the formation of blood clot inside the blood vessel of the heart.
         The blood clot inside the blood vessel of the heart restricts the flow of blood within the heart which may lead to heart tissue damage or even heart attack.
         This is mostly caused because of cholesterol and fats present in artery wall.
         """)

    col1, col2=st.columns(2)
    with col1:
        st.subheader("Risk factors:-")
        st.markdown("1. High LDL Cholesterol")
        st.markdown("2. Smoking")
        st.markdown("3. Sedentary Life Style")
        st.markdown("4. Hypertension")

    with col2:
        st.image(".\images\_NoSmoking.jpeg")

    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")

    ########################################Signs and Symptoms#################################################################

    st.subheader("Signs and Symptoms")
    st.markdown(
        """
        Coronary Thrombus is **Asymptomatic**.
        It doesn't show any signs or symptoms usually until heart attack.
        """
    )

    with st.expander("possible symptoms"):

        st.markdown("-> Crushing Chest pain")
        st.markdown("-> Shortness of breath")
        st.markdown("-> Upper body discomfort ")

    st.image(".\images\symptom.jpeg")

    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.title(" ")




    ########################################Heart Attack vs Coronary Thrombosis#################################################################


    st.subheader("Heart Attack vs Coronary Thrombosis")
    st.write("Coronary Thrombosis is often confused with heart attack as many are not aware of the differences between them. Here is the difference between the two.")
    st.write("Heart attack: Heart attack refers to the death of the heart tissue due to the consequent loss of blood flow.")
    st.write("Thrombosis: It refers to blocking of blood vessels due to a thrombus.")
    st.image(".\images\Thrombosis.jpeg")

    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.title(" ")

    st.header("Here's the dataset used for training the model")
    st.dataframe(df)
