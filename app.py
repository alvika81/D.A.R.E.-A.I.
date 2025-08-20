import streamlit as st
import requests
import os

anthropic_api_key = "your_anthropic_api_key_here"

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
        st.error("High risk: Please seek help immediately.")
    elif score == 1:
        st.warning("Moderate risk: Monitor and consider talking to a counselor.")
    else:
        st.success("Low risk: Stay informed and healthy.")

st.header("🤖 Chat with Drug Awareness Bot")
user_input = st.text_input("Ask me anything about drug safety:")

if user_input:
    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": anthropic_api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 200,
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # Claude’s text is inside result["content"][0]["text"]
        st.write("**🤖 Bot:**", result["content"][0]["text"])

    except Exception as e:
        st.error(f"Error: {str(e)}")

st.header("📞 Helpline Numbers")
st.write("- India: 1800-11-0031 (Narcotics Control Bureau)")
