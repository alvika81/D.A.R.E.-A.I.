import streamlit as st
import requests

HF_API_KEY = st.secrets["huggingface"]["token"]

st.set_page_config(page_title="Drug Awareness App", layout="wide")
st.title("💊 Drug Awareness & Support")

st.header("Common Drugs & Their Effects")
drugs = {
    "Cocaine": "A powerful stimulant that can cause addiction, heart problems, and anxiety.",
    "Heroin": "An opioid that is highly addictive and can cause respiratory failure.",
    "LSD": "A hallucinogen that can cause altered thoughts and dangerous behavior.",
    "Methamphetamine": "A stimulant that can damage the brain and cause paranoia."
}
for drug, info in drugs.items():
    st.subheader(drug)
    st.write(info)

st.header("📝 Self-Assessment Quiz")
q1 = st.radio("Do you or someone you know use drugs regularly?", ["yes", "no"])
q2 = st.radio("Have you felt the need to cut down?", ["yes", "no"])
q3 = st.radio("Have others expressed concern about your usage?", ["yes", "no"])

if st.button("Check Risk Level"):
    score = sum([q1 == "yes", q2 == "yes", q3 == "yes"])
    if score >= 2:
        st.error("⚠️ High risk: Please seek help immediately.")
    elif score == 1:
        st.warning("⚠️ Moderate risk: Monitor and consider talking to a counselor.")
    else:
        st.success("✅ Low risk: Stay informed and healthy.")

st.header("🤖 Chat with Drug Awareness Bot")
user_input = st.text_input("Ask me anything about drug safety:")

if user_input:
    try:
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {"inputs": f"Answer this drug awareness question clearly:\n{user_input}"}

        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            bot_reply = result[0]["generated_text"].strip()
        elif "error" in result:
            bot_reply = f"⚠️ API Error: {result['error']}"
        else:
            bot_reply = "Sorry, I couldn't generate a response. Please try again."

        st.write("**🤖 Bot:**", bot_reply)

    except Exception as e:
        st.error(f"Error: {str(e)}")
        
st.header("📞 Helpline Numbers")
st.write("- **India:** 1800-11-0031 (Narcotics Control Bureau)")
