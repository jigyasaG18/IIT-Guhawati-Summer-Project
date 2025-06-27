# Add this at the very top
import streamlit as st
import base64
import joblib
import pandas as pd
import streamlit.components.v1 as components
import random

# Set up responsive layout
st.set_page_config(page_title="DV Risk & Support", layout="wide", initial_sidebar_state="expanded")

# Load ML model and scaler
model = joblib.load("domestic_violence_model.pkl")
scaler = joblib.load("scaler.pkl")

# Cache police station data
@st.cache_data
def load_police_stations():
    df = pd.read_csv("dataset/Police_Stations_India.csv")
    df["Phone Number"] = df["Phone Number"].astype(str)
    return df

df_police_stations = load_police_stations()

# Custom mobile-friendly styling
st.markdown("""
<style>
body {
    margin: 0;
    padding: 0;
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3, h4, h5 {
    font-size: 5vw;
}
@media (min-width: 768px) {
    h1 {
        font-size: 40px !important;
    }
    h3 {
        font-size: 24px !important;
    }
}
.block-container {
    padding: 1rem 1.5rem;
}
button[kind="primary"] {
    padding: 0.75em 1.25em;
    font-size: 1rem;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("bg.png")
st.sidebar.header("🆘 Emergency Options")
if st.sidebar.button("🚨 SOS Emergency Help"):
    st.session_state.page = "help"
if st.sidebar.button("🔍 Risk Assessment"):
    st.session_state.page = "risk_assessment"
if st.sidebar.button("🚪 Quick Exit"):
    st.session_state.page = "quick_exit"
if st.sidebar.button("📍 Nearby Resources"):
    st.session_state.page = "nearby_resources"
if st.sidebar.button("📖 Hear Her Stories"):
    st.session_state.page = "hear_her_stories"

# Header
st.markdown("<h1 style='text-align:center;'>🛡️ EMPOWER SAKHI 🛡️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Your All-Time Support for Domestic Violence Risk & Safety</h3>", unsafe_allow_html=True)

# --- Add your existing functions here like risk_assessment_form(), hear_her_stories(), etc. ---
# Paste your `risk_assessment_form()` and `hear_her_stories()` functions without modification
# They're already quite mobile-friendly thanks to Streamlit's components.

# Page Routing
if "page" in st.session_state:
    if st.session_state.page == "help":
        # Emergency Help Page
        st.error("🚨 **Emergency Alert!** 🚨")
        st.markdown("### Emergency Helplines")
        st.markdown("""
        - 📞 **Call 112** (National Emergency)
        - 📞 **Call 1091** (Women Helpline)
        - 📞 **Call 181** (Women Power)
        - 📞 **Call 100** (Police)
        """)
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmd2c3R1ZHYzczYyYzRhYmFoZTNucDkwZjlxbnlrbjExenM1b210YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oMS7ZYPF1jtfV48Lxr/giphy.gif", use_container_width=True)

    elif st.session_state.page == "risk_assessment":
        risk_assessment_form()

    elif st.session_state.page == "nearby_resources":
        st.subheader("Enter Your Location")
        location_input = st.text_input("City and/or State (e.g., Mumbai, Maharashtra)")
        if location_input:
            parts = location_input.split(",")
            city = parts[0].strip().lower()
            state = parts[1].strip().lower() if len(parts) == 2 else None
            mask = df_police_stations["State"].str.lower().str.strip() == state if state else df_police_stations["City"].str.lower().str.contains(city)
            results = df_police_stations[mask]
            if not results.empty:
                st.success("📍 Showing results:")
                st.dataframe(results[["Police Station Name", "City", "State", "Email", "Phone Number"]])
            else:
                st.warning("⚠️ No matching police stations found.")

    elif st.session_state.page == "quick_exit":
        st.subheader("⚠️ Emergency Situation - Stay Calm")
        st.markdown("#### English Steps")
        english_steps = [
            "1. Stay calm.",
            "2. Call 112 or 1091.",
            "3. Go to safety.",
            "4. Avoid confrontation.",
            "5. Inform someone.",
            "6. Record evidence.",
            "7. Seek shelter.",
            "8. Be aware.",
            "9. Report to police.",
            "10. Contact helplines."
        ]
        for step in english_steps:
            st.markdown(f"- {step}")
        st.markdown("#### Hindi Steps")
        hindi_steps = [
            "1. शांत रहें।",
            "2. 112 या 1091 पर कॉल करें।",
            "3. सुरक्षित स्थान पर जाएं।",
            "4. विवाद से बचें।",
            "5. किसी को बताएं।",
            "6. सबूत लें।",
            "7. शरण लें।",
            "8. सतर्क रहें।",
            "9. पुलिस को बताएं।",
            "10. हेल्पलाइन से संपर्क करें।"
        ]
        for step in hindi_steps:
            st.markdown(f"- {step}")

    elif st.session_state.page == "hear_her_stories":
        hear_her_stories()
else:
    st.markdown("<h4 style='text-align: center;'>Please select an option from the sidebar.</h4>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenF6ODQ0a2ZsMnV3Y3pxczEydmh0eGFrczNyb2M4dnFiaTQ3Z3hzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gmG4bIu3mmM60WJckp/giphy.gif' style='width: 100%; height: auto;' /></div>",
                unsafe_allow_html=True)
