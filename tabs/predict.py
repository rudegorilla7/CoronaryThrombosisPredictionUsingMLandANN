import streamlit as st

# Import necessary functions from web_functions
#from webFunction import predict
from webFunction import predict


def app(df, X, y):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">ARTIFICIAL NEURAL NETWORK</b> for Coronary Thrombosis Prediction.
            </p>
        """, unsafe_allow_html=True)

    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    age = st.slider("Age", int(df["age"].min()), int(df["age"].max()))
    male = st.slider("Sex", int(df["male"].min()), int(df["male"].max()))
    currentSmoker = st.slider("CurrentSmoker", int(df["currentSmoker"].min()), int(df["currentSmoker"].max()))
    cigsPerDay = st.slider("Cigarettes per Day", int(df["cigsPerDay"].min()), int(df["cigsPerDay"].max()))
    BPMeds = st.slider("BPMeds", float(df["BPMeds"].min()), float(df["BPMeds"].max()))
    prevalentStroke = st.slider("prevalentStroke", int(df["prevalentStroke"].min()), int(df["prevalentStroke"].max()))
    prevalentHyp = st.slider("prevalentHyp", int(df["prevalentHyp"].min()), int(df["prevalentHyp"].max()))
    diabetes = st.slider("diabetes", int(df["diabetes"].min()), int(df["diabetes"].max()))
    totChol = st.slider("totChol in mg/Dl", int(df["totChol"].min()), int(df["totChol"].max()))
    sysBP = st.slider("sysBP in mm Hg", int(df["sysBP"].min()), int(df["sysBP"].max()))
    diaBP = st.slider("diaBP in mm Hg", int(df["diaBP"].min()), int(df["diaBP"].max()))
    BMI = st.slider("BMI", int(df["BMI"].min()), int(df["BMI"].max()))
    heartRate = st.slider("heartRate in beats per Minute", int(df["heartRate"].min()),int(df["heartRate"].max()))
    glucose = st.slider("glucose in mg/Dl", int(df["glucose"].min()), int(df["glucose"].max()))

    # Create a list to store all the features
    features = [male,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        #score = score + 0.06
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get CORONARY THROMBOSIS!!")
        else:
            st.success("The person is relatively safe from CORONARY THROMBOSIS")

        # Print teh score of the model
        st.write("The model used has an accuracy of ", round((score * 100), 2), "% and can be trusted.")
        st.write("But it is always better to check up with your doctor.")

