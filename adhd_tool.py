import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ADHD Pharmacotherapy Tool", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6fb;
}
.card {
    padding: 20px;
    border-radius: 14px;
    background-color: blue;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
.footer-box {
    background-color: #eef3f8;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}
h1 {
    text-align: center;
    color: #1f4e79;
}
</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.markdown("""
<div style='
background: linear-gradient(90deg, #1f4e79, #4fa3d1);
padding: 20px;
border-radius: 12px;
text-align: center;
color: white;
font-size: 28px;
font-weight: bold;
box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
'>
ADHD Pharmacotherapy Decision-Support Tool
</div>
""", unsafe_allow_html=True)

st.caption("Applicable for young adults (18–24 years) | Exploratory clinical framework")

st.info("This tool is based on pilot research using the ADHD ASRS v1.1 screening scale. It provides exploratory risk stratification and does NOT constitute a clinical diagnosis.")

st.markdown("---")

# ---------------- LAYOUT ----------------
col1, col2, col3 = st.columns([1,1,1])

# ---------------- INPUT PANEL ----------------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Patient Profile")

    mood = st.checkbox("Frequent Mood Swings")
    suicidal = st.checkbox("Suicidal Ideation")
    hallucination = st.checkbox("Hallucination Experiences")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SCORING ----------------
score = 0
if mood:
    score += 3
if suicidal:
    score += 2
if hallucination:
    score += 2

# ---------------- RISK LOGIC ----------------
if hallucination:
    risk = "HIGH"
    color = "#d9534f"
elif score >= 5:
    risk = "HIGH"
    color = "#d9534f"
elif score >= 3:
    risk = "MODERATE"
    color = "#f0ad4e"
else:
    risk = "LOW"
    color = "#5cb85c"

# ---------------- RISK PANEL ----------------
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Risk Assessment")

    st.metric("Score", score)
    st.progress(score / 7)

    st.markdown(f"<h3 style='color:{color};'>Risk Level: {risk}</h3>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DRUG PANEL ----------------
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Pharmacological Considerations")

    if hallucination:
        st.error("⚠️ Psychotic features present")
        st.write("Avoid stimulant therapy")
        st.write("Preferred: Atomoxetine / Guanfacine")

    elif suicidal:
        st.warning("⚠️ High-risk psychiatric profile")
        st.write("Use stimulants with caution")
        st.write("Consider non-stimulants")

    elif mood:
        st.info("⚠️ Emotional dysregulation")
        st.write("Monitor stimulant response carefully")

    else:
        st.success("✅ Low-risk profile")
        st.write("Standard stimulant therapy (Methylphenidate)")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CLINICAL INTERPRETATION ----------------
st.markdown("---")
with st.expander("Clinical Interpretation"):
    if mood:
        st.write("Mood instability may affect stimulant tolerability.")
    if suicidal:
        st.write("Suicidal ideation requires careful safety monitoring.")
    if hallucination:
        st.write("Psychotic symptoms may worsen with stimulant therapy.")

# ---------------- TREATMENT PATHWAY ----------------
st.markdown("---")
st.subheader("Treatment Pathway")

st.markdown("""
<div style='display:flex; gap:15px;'>

<div style='flex:1; background-color:#d4edda; padding:15px; border-radius:10px;'>
<b style='color:#155724;'>LOW RISK</b><br>
• Start stimulant therapy<br>
• Example: Methylphenidate<br>
</div>

<div style='flex:1; background-color:#fff3cd; padding:15px; border-radius:10px;'>
<b style='color:#856404;'>MODERATE RISK</b><br>
• Cautious stimulant use<br>
• Consider non-stimulant<br>
• Monitor closely<br>
</div>

<div style='flex:1; background-color:#f8d7da; padding:15px; border-radius:10px;'>
<b style='color:#721c24;'>HIGH RISK</b><br>
• Avoid stimulants<br>
• Prefer non-stimulants<br>
• Psychiatric supervision required<br>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
**Step 1: Initial Therapy**
- Low Risk → Stimulant (Methylphenidate)  
- Moderate Risk → Cautious stimulant / Non-stimulant  
- High Risk → Prefer Non-stimulant  

**Step 2: Reassessment**
- Evaluate clinical response  
- Adjust dose or switch drug class  

**Step 3: Complex Cases**
- Specialist referral  
- Combination therapy under supervision  
""")

# ---------------- SUMMARY ----------------
st.markdown("---")
st.subheader("Patient Summary")

st.write(f"Risk Level: {risk}")
st.write(f"Score: {score}")

if risk == "HIGH":
    st.write("Recommendation: Prefer non-stimulant therapy")
elif risk == "MODERATE":
    st.write("Recommendation: Individualized treatment approach")
else:
    st.write("Recommendation: Standard stimulant therapy")

# ---------------- RESEARCH TEAM ----------------
st.markdown("---")
st.markdown("### 👨‍🔬 Research Team")

st.markdown("""
<div class='footer-box'>

<b>Research Team Name:</b> PhD  <br>
<b>Research Student:</b> Samson K. Wilson <br>
<b>Clinical Expert (Psychiatrist):</b> Dr. Srinivas Singisetti <br>
<b>Research Supervisor:</b> Dr. Amit Kundu

</div>
""", unsafe_allow_html=True)

# ---------------- DISCLAIMER ----------------
st.markdown("---")
st.warning("This is an exploratory decision-support tool and does NOT replace clinical judgment or diagnosis.")
