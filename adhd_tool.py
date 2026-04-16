import streamlit as st

st.set_page_config(layout="wide")

st.title("ADHD Pharmacotherapy Tool")
st.markdown("Clinical Decision-Support Framework")

st.markdown("---")

# Layout
col1, col2, col3 = st.columns(3)

# INPUT
with col1:
    st.subheader("Patient Profile")

    mood = st.checkbox("Mood Swings")
    suicidal = st.checkbox("Suicidal Thoughts")
    hallucination = st.checkbox("Hallucinations")

# SCORING
score = 0

if mood:
    score += 3
if suicidal:
    score += 2
if hallucination:
    score += 2

# RISK
if hallucination:
    risk = "HIGH"
    color = "red"
elif score >= 5:
    risk = "HIGH"
    color = "red"
elif score >= 3:
    risk = "MODERATE"
    color = "orange"
else:
    risk = "LOW"
    color = "green"

# RISK DISPLAY
with col2:
    st.subheader("Risk Assessment")

    st.metric("Score", score)
    st.markdown(f"<h2 style='color:{color};'>Risk: {risk}</h2>", unsafe_allow_html=True)

# DRUG OUTPUT
with col3:
    st.subheader("Pharmacological Considerations")

    if hallucination:
        st.error("Psychotic features present")
        st.write("Avoid stimulants")
        st.write("Use Atomoxetine / Guanfacine")

    elif suicidal:
        st.warning("High-risk psychiatric profile")
        st.write("Use stimulants cautiously")
        st.write("Consider non-stimulants")

    elif mood:
        st.info("Emotional dysregulation")
        st.write("Monitor stimulant response")

    else:
        st.success("Low-risk profile")
        st.write("Standard stimulant therapy (Methylphenidate)")

st.markdown("---")
st.warning("This tool is exploratory and not a prescribing system.")
