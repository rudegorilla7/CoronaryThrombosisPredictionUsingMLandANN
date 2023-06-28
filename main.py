"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st
from streamlit_option_menu import option_menu

# Import necessary functions from web_functions
from webFunction import load_data

# Import pages
from tabs import home, data1, predict, healthyLife
# Configure the app
st.set_page_config(
    page_title='Hygieia',
    page_icon='heart',
    layout='wide',
    initial_sidebar_state='auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data1,
    "Prediction": predict,
    "Ways for Healthier Lifestyle": healthyLife

}

# Create a sidebar
with st.sidebar:
   selected=option_menu(
       menu_title="Main Menu",
       options=["Home","Data Info","Prediction","Ways for Healthier Lifestyle"]
   )

# Add title to sidear
#st.sidebar.title("Navigation")

# Create radio option to select the page


# Loading the dataset.
df, X, y = load_data()

if selected=="Home":
    Tabs[selected].app()
if selected=="Data Info":
    Tabs[selected].app(df)
if selected=="Prediction":
    Tabs[selected].app(df,X,y)
if selected=="Ways for Healthier Lifestyle":
    Tabs[selected].app()
# Call the app funciton of selected page to run

