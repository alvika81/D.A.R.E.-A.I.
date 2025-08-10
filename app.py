import streamlit as st
import openai

openai.api_key = "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"

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
score = 0
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

st.header("💬 Chat with Drug Awareness Bot")
user_input = st.text_input("Ask me anything about drug safety:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful drug awareness assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write("**Bot:**", response.choices[0].message["content"])

st.header("📞 Helpline Numbers")
st.write("- India: 1800-11-0031 (Narcotics Control Bureau)")
