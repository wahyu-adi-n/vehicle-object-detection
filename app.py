import streamlit as st

# Custom imports
from multipage import MultiPage

from pages import vehicleDetection
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Vehicle Detection")

# Add all your application here
app.add_page("Vehicle Detection", vehicleDetection.app)

# The main app
app.run()
