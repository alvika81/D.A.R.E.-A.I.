Import streamlit as st
Import openai
Openai.api_key = "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"

St.set_page_config(page_title="Drug Awareness App", layout="wide")
St.title("💊 Drug Awareness & Support")

St.header("Common Drugs & Their Effects")
Drugs = {
    "Cocaine": "A powerful stimulant that can cause addiction, heart problems, and anxiety.",
    "Heroin": "An opioid that is highly addictive and can cause respiratory failure.",
    "LSD": "A hallucinogen that can cause altered thoughts and dangerous behavior.",
    "Methamphetamine": "A stimulant that can damage the brain and cause paranoia."
}
For drug, info in drugs.items():
St.subheader(drug)
St.write(info)
St.header("📝 Self-Assessment Quiz")
Score = 0
Q1 = st.radio("Do you or someone you know use drugs regularly?", ["Yes", "No"])
Q2 = st.radio("Have you felt the need to cut down?", ["Yes", "No"])
Q3 = st.radio("Have others expressed concern about your usage?", ["Yes", "No"])
If st.button("Check Risk Level"):
    Score = sum([q1 == "Yes", q2 == "Yes", q3 == "Yes"])
    If score >= 2:
St.error("High Risk: Please seek help immediately.")
Elif score == 1:
St.warning("Moderate Risk: Monitor and consider talking to a counselor.")
    Else:
St.success("Low Risk: Stay informed and healthy.")
St.header("💬 Chat with Drug Awareness Bot")
User_input = st.text_input("Ask me anything about drug safety:")
If user_input:
    Response = openai.ChatCompletion.create(
        Model="gpt-3.5-turbo",
        Messages=[
            {"role": "system", "content": "You are a helpful drug awareness assistant."},
            {"role": "user", "content": user_input}
 ]
St.write("**Bot:**", response.choices[0].message.content)
St.header("📞 Helpline Numbers")
St.write("- India: 1800-11-0031 (Narcotics Control Bureau)")
