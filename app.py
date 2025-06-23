import base64
import joblib
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import random

# Set up the page configuration
st.set_page_config(page_title="DV Risk & Support", layout="centered", initial_sidebar_state="expanded")
# Custom CSS to set background color to black

# Load ML model and scaler
model = joblib.load("domestic_violence_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load and cache police station data
@st.cache_data
def load_police_stations():
    df = pd.read_csv("dataset/Police_Stations_India.csv")
    df["Phone Number"] = df["Phone Number"].astype(str)  # Ensure phone numbers are strings
    return df

df_police_stations = load_police_stations()

st.sidebar.image("bg.png")

# RISK ASSESSMENT FORM
def risk_assessment_form():
    st.header("👩 Risk Assessment Form")

    age = st.slider("Age", 18, 50, 30)

    # Updated education levels
    education_levels = [
        "None", "Primary", "Lower Secondary", "Upper Secondary",
        "Diploma/Technical", "Undergraduate", "Postgraduate"
    ]
    education_probs = [0.05, 0.2, 0.25, 0.25, 0.1, 0.1, 0.05]
    education = st.selectbox("Education", education_levels)

    income = st.selectbox("Monthly Income", ["<5000", "5000-10000", "10000-20000", ">20000"])
    marital_status = st.selectbox("Marital Status", ["Married", "Unmarried", "Divorced", "Widowed"])
    children = st.number_input("Number of Children", 0, 10, 0)
    has_partner = st.selectbox("Do you currently have a partner?", ["Yes", "No"])
    partner_alcoholic = st.selectbox("Partner alcoholic?", ["Yes", "No"])
    has_support = st.selectbox("Has support system?", ["Yes", "No"])
    past_violence = st.selectbox("Past violence?", ["Yes", "No"])
    mental_issues = st.selectbox("Mental health concerns?", ["Yes", "No"])
    employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed", "Part-time", "Student", "Homemaker"])
    housing_situation = st.selectbox("Housing Situation", ["Own", "Rent", "Shelter", "Homeless", "With relatives"])
    disability = st.selectbox("Disability?", ["Yes", "No"])
    self_substance_abuse = st.selectbox("Substance Abuse?", ["Yes", "No"])
    previous_reports = st.number_input("Previous Reports", 0, 5, 0)

    # Encode features as integers
    encode_map = {
        "None": 0, "Primary": 1, "Lower Secondary": 2, "Upper Secondary": 3,
        "Diploma/Technical": 4, "Undergraduate": 5, "Postgraduate": 6,
        "<5000": 0, "5000-10000": 1, "10000-20000": 2, ">20000": 3,
        "Married": 0, "Unmarried": 1, "Divorced": 2, "Widowed": 3,
        "Yes": 1, "No": 0,
        "Employed": 0, "Unemployed": 1, "Part-time": 2, "Student": 3, "Homemaker": 4,
        "Own": 0, "Rent": 1, "Shelter": 2, "Homeless": 3, "With relatives": 4
    }

    input_data = pd.DataFrame([{
        "age": age,
        "education": encode_map[education],
        "income": encode_map[income],
        "marital_status": encode_map[marital_status],
        "number_of_children": children,
        "has_partner": encode_map[has_partner],
        "partner_alcoholic": encode_map[partner_alcoholic],
        "has_support_system": encode_map[has_support],
        "past_violence": encode_map[past_violence],
        "mental_health_issues": encode_map[mental_issues],
        "employment_status": encode_map[employment_status],
        "housing_situation": encode_map[housing_situation],
        "disability": encode_map[disability],
        "self_substance_abuse": encode_map[self_substance_abuse],
        "previous_reports": previous_reports
    }])

    input_scaled = scaler.transform(input_data)

    if st.button("🔍 Assess Risk"):
        prediction = model.predict(input_scaled)[0]
        risk_score = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            st.error("⚠️ High risk of domestic violence.")
        else:
            st.success("✅ Low risk of domestic violence.")

        st.metric("Risk Score", f"{risk_score * 100:.1f}%")

#Hear her stories for women section of app
def hear_her_stories():
    st.subheader("📖 Hear Her Stories")

    st.markdown("Real, anonymous words from brave women — just like you. Let their voices remind you: **you are not alone.**")

    stories = [
    "💬 'I thought I couldn't live without him. But I learned to live for me. Today, I smile without fear.'",
    "💬 'I was silenced for years. Speaking up was the first breath I truly took.'",
    "💬 'Leaving was hard. Healing was harder. But I did both. And so will you.'",
    "💬 'I still remember the pain. But now, I hold space for my strength too.'",
    "💬 'No woman deserves fear. No child should witness it. I broke the cycle.'",
    "💬 'Every scar I carry tells a story — not of weakness, but of survival.'",
    "💬 'The moment I walked out the door, I took my life back.'",
    "💬 'My bruises faded, but my courage remained.'",
    "💬 'He tried to break me. Instead, he built a warrior.'",
    "💬 'I stopped asking why it happened and started focusing on how I heal.'",
    "💬 'I am not what happened to me. I am what I choose to become.'",
    "💬 'You don’t need permission to be free.'",
    "💬 'Her strength was not loud. It was silent, steady, and unshakable.'",
    "💬 'I found pieces of myself I thought I lost forever.'",
    "💬 'Hope is the quiet voice that whispers: you can try again tomorrow.'",
    "💬 'I left. I healed. I rose.'",
    "💬 'Pain is part of my story, but so is power.'",
    "💬 'There’s life after fear. I’m living proof.'",
    "💬 'You are allowed to leave any story that doesn’t make you feel safe.'",
    "💬 'I stopped shrinking to make room for someone who never saw me.'",
    "💬 'She remembered who she was — and the game changed.'",
    "💬 'Love shouldn’t hurt. And I now know what real love feels like — peace.'",
    "💬 'I broke the silence. And in doing so, I found my voice.'",
    "💬 'My past doesn’t define me. My resilience does.'",
    "💬 'You are more than what you've survived.'",
    "💬 'Healing is not linear — but it is possible.'",
    "💬 'I am the woman I once prayed I could become.'",
    "💬 'Being safe is not selfish — it is sacred.'",
    "💬 'The first night I slept in peace, I knew I had made the right choice.'",
    "💬 'He lost control. I gained my freedom.'",
    "💬 'Abuse thrives in silence. I choose to speak.'",
    "💬 'I was never broken. Just buried under pain. And now, I bloom.'",
    "💬 'Strength is crying, and still waking up the next day.'",
    "💬 'The most radical thing I did was believe I deserved better.'",
    "💬 'Healing is hard. But staying hurt was harder.'",
    "💬 'Not all wounds are visible, but all healing is valid.'",
    "💬 'No more walking on eggshells. I walk in strength now.'",
    "💬 'I’m proud of how far I’ve come — even if no one else sees it.'",
    "💬 'The chains are gone. And so is the shame.'",
    "💬 'I don’t need to be perfect to be worthy of love and safety.'",
    "💬 'I am not dramatic. I am a survivor.'",
    "💬 'Safety is not a luxury. It’s a right.'",
    "💬 'My story isn’t over. It’s just beginning.'",
    "💬 'The most powerful word I learned was: No.'",
    "💬 'He tried to silence me. But I write my own ending now.'",
    "💬 'My tears watered the seeds of my strength.'",
    "💬 'You are not alone. You are never alone.'",
    "💬 'Every time I said “enough,” I meant it a little louder.'",
    "💬 'Some days I stumble, but I never go back.'",
    "💬 'She wore her freedom like a crown.'",
    "💬 'Even in my darkest hour, I was finding my way back to the light.'",
    "💬 'One day, this pain will become someone else’s hope — through me.'"
]

    if st.button("🔄 Show Me a Story"):
        story = random.choice(stories)
        st.markdown(f"""
        <div style='
            font-size: 18px;
            padding: 15px;
            background-color: #f0f0f5;
            border-left: 4px solid #e91e63;
            border-radius: 6px;
            color: black;
            margin-top: 10px;
        '>
            {story}
        </div>
        <style>
        @media (prefers-color-scheme: dark) {{
            div[style*="background-color: #f0f0f5"] {{
                background-color: #2a2a2a !important;
                color: #f5f5f5 !important;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("💡 *Want to share your voice anonymously? Email us your story at empowersakhi@mail.com to inspire others.*")

# HEADER
st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold;'>🛡️ EMPOWER SAKHI 🛡️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-style: italic;'>Your All-Time Support for Domestic Violence Risk & Safety</h3>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.header("🆘 Emergency Options")
    if st.button("🚨 SOS Emergency Help"):
        st.session_state.page = "help"
    if st.button("🔍 Risk Assessment"):
        st.session_state.page = "risk_assessment"
    if st.button("🚪 Quick Exit"):
        st.session_state.page = "quick_exit"
    if st.button("📍 Nearby Resources"):
        st.session_state.page = "nearby_resources"
    if st.sidebar.button("📖 Hear Her Stories"):
        st.session_state.page = "hear_her_stories"

# PAGE HANDLER
if "page" in st.session_state:
    if st.session_state.page == "help":
        st.error("🚨 **Emergency Alert!** 🚨")

        st.markdown("### **Emergency Helplines**")
        st.markdown("""
        - **📞 Call 112** (National Emergency Number)
        - **📞 Call 1091** (Women Helpline)
        - **📞 Call 181** (Women Power Helpline)
        - **📞 Call 100** (Police Helpline)
        """)

        st.markdown("---")

        st.markdown("### **Safety Tips**")
        st.markdown("""
        - **Stay Calm**: Take a deep breath and try to stay composed.
        - **Seek Shelter**: Go to a safe place if possible. A neighbor, friend's house, or public space may help.
        - **Avoid Confrontation**: Do not engage in any argument or physical confrontation with the abuser.
        - **Use Technology**: If safe, send a text or use social media to alert someone you trust.
        - **Document Evidence**: If possible, take photos or videos of any injuries or damage.
        - **Trust Your Instincts**: Always listen to your gut feelings, and act quickly if you feel unsafe.
        """)

        st.markdown("---")

        st.markdown("### **Additional Resources**")
        st.markdown("""
        - [**Women Shelters List (India)**](https://spuwac.in/shelterhomesw.html)
        - [**File Complaint Online**](https://ncwapps.nic.in/onlinecomplaintsv2/)
        - [**Legal Aid and Support**](https://nalsa.gov.in/)
        """)

        st.markdown("### **Remember**: **You are not alone. Help is available. Reach out immediately!**")

        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmd2c3R1ZHYzczYyYzRhYmFoZTNucDkwZjlxbnlrbjExenM1b210YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oMS7ZYPF1jtfV48Lxr/giphy.gif", use_container_width=True)

    elif st.session_state.page == "risk_assessment":
        risk_assessment_form()

    elif st.session_state.page == "nearby_resources":
        st.subheader("Enter Your Location")
        location_input = st.text_input("Enter your city and/or state (e.g., South Delhi, Delhi)")

        if location_input:
            parts = location_input.split(",")
            city = parts[0].strip().lower()
            state = parts[1].strip().lower() if len(parts) == 2 else None

            if state:
                mask = df_police_stations["State"].str.lower().str.strip() == state
            else:
                mask = df_police_stations["City"].str.lower().str.contains(city)

            results = df_police_stations[mask]

            st.write(f"Searching for: {location_input}")

            if not results.empty:
                st.success("📍 Showing results:")
                st.dataframe(results[["Police Station Name", "City", "State", "Email", "Phone Number"]])
            else:
                st.warning("⚠️ No matching police stations found.")

    elif st.session_state.page == "quick_exit":
        st.subheader("⚠️ **Emergency Situation - Stay Calm!**")

        st.markdown("### **Emergency Steps (English)**")
        english_steps = [
            "1. **Stay Calm.** Take a deep breath and stay composed.",
            "2. **Call for Help.** Dial 112 or 1091 immediately.",
            "3. **Run to Safety.** Leave the location if possible.",
            "4. **Avoid Confrontation.** Don’t argue or fight back.",
            "5. **Inform Someone.** Tell a friend or family member.",
            "6. **Document Evidence.** Safely record proof.",
            "7. **Seek Shelter.** Go to a safe space nearby.",
            "8. **Stay Aware.** Be mindful of surroundings.",
            "9. **Report to Police.** As soon as you can.",
            "10. **Get Support.** Contact helplines for help."
        ]
        for step in english_steps:
            st.markdown(f"- {step}")

        st.markdown("### **आपातकालीन कदम (Hindi)**")
        hindi_steps = [
            "1. **शांत रहें।** घबराएं नहीं, गहरी सांस लें।",
            "2. **मदद के लिए कॉल करें।** तुरंत 112 या 1091 पर कॉल करें।",
            "3. **सुरक्षित स्थान पर जाएं।** यदि संभव हो तो स्थान छोड़ें।",
            "4. **विवाद से बचें।** बहस न करें।",
            "5. **विश्वसनीय व्यक्ति को बताएं।** किसी करीबी को जानकारी दें।",
            "6. **सबूत संकलित करें।** यदि सुरक्षित हो तो फोटो या वीडियो लें।",
            "7. **शरण लें।** किसी भरोसेमंद जगह जाएं।",
            "8. **सतर्क रहें।** आसपास का ध्यान रखें।",
            "9. **पुलिस को बताएं।** जल्द से जल्द रिपोर्ट करें।",
            "10. **सहायता प्राप्त करें।** हेल्पलाइन से संपर्क करें।"
        ]
        for step in hindi_steps:
            st.markdown(f"- {step}")

    elif st.session_state.page == "hear_her_stories":
        hear_her_stories()

else:
    st.markdown(
        "<h4 style='text-align: center;'>Please select an option from the sidebar.</h4>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='display: flex; justify-content: center;'>"
        "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenF6ODQ0a2ZsMnV3Y3pxczEydmh0eGFrczNyb2M4dnFiaTQ3Z3hzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gmG4bIu3mmM60WJckp/giphy.gif' style='width: 100%; height: auto;' />"
        "</div>", 
        unsafe_allow_html=True
    )
