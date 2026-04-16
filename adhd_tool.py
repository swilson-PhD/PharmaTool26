import streamlit as st

st.title("ADHD Tool")

mood = st.checkbox("Mood Swings")
suicidal = st.checkbox("Suicidal Thoughts")
hallucination = st.checkbox("Hallucinations")

score = 0

if mood:
    score += 3
if suicidal:
    score += 2
if hallucination:
    score += 2

st.write("Score:", score)

if hallucination:
    st.write("Avoid stimulants, use non-stimulants")
elif suicidal:
    st.write("Use caution, consider non-stimulants")
elif mood:
    st.write("Monitor stimulant response")
else:
    st.write("Standard treatment may be used")

st.warning("This is not a prescribing tool")
