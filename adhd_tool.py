import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ADHD Tool", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6fb;
}
.card {
    padding: 20px;
    border-radius: 14px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #1f4e79;
}
.footer-box {
    background-color: #eef3f8;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
<div style='
background: linear-gradient(90deg, #1f4e79, #4fa3d1);
padding: 18px;
border-radius: 12px;
text-align: center;
color: white;
font-size: 28px;
font-weight: bold;
'>
ADHD Pharmacotherapy Decision-Support Tool
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- APPLICABILITY ----------------
st.markdown("""
<div style='
background-color:#800000;
padding:12px;
border-radius:10px;
text-align:center;
color:white;
font-weight:bold;
'>
Applicable for young adults (18–24 years) screening positive for ADHD symptoms
</div>
""", unsafe_allow_html=True)

# ---------------- DISCLAIMER ----------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style='
background-color:#f4a261;
padding:12px;
border-radius:10px;
text-align:center;
color:black;
'>
This tool is based on pilot research using the ADHD ASRS v1.1 screening scale. 
It provides exploratory risk stratification and does NOT constitute a clinical diagnosis.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- LAYOUT ----------------
col1, col2, col3 = st.columns(3)

# ---------------- INPUT ----------------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧾 Patient Profile")

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

# ---------------- RISK ----------------
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
    st.subheader("📊 Risk Assessment")

    st.metric("Score", score)
    st.progress(score / 7)

    st.markdown(f"<h3 style='color:{color};'>Risk Level: {risk}</h3>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DRUG PANEL ----------------
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💊 Pharmacological Considerations")

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

# ---------------- TREATMENT PATHWAY ----------------
st.markdown("---")
st.subheader("🧭 Treatment Pathway")

st.markdown("""
<div style='display:flex; gap:20px;'>

<div style='flex:1; background:linear-gradient(135deg,#d4edda,#a8e6cf);
padding:18px; border-radius:12px;'>

<h4 style='color:#155724;'>✅ LOW RISK</h4>
<p style='color:#155724;'>
• Start stimulant therapy<br>
• Preferred: Methylphenidate<br>
• Routine monitoring
</p>
</div>

<div style='flex:1; background:linear-gradient(135deg,#fff3cd,#ffeaa7);
padding:18px; border-radius:12px;'>

<h4 style='color:#856404;'>⚠️ MODERATE RISK</h4>
<p style='color:#856404;'>
• Cautious stimulant use<br>
• Consider non-stimulants<br>
• Close monitoring
</p>
</div>

<div style='flex:1; background:linear-gradient(135deg,#f8d7da,#f5b7b1);
padding:18px; border-radius:12px;'>

<h4 style='color:#721c24;'>🚨 HIGH RISK</h4>
<p style='color:#721c24;'>
• Avoid stimulants<br>
• Prefer non-stimulants<br>
• Psychiatric supervision
</p>
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- CLINICAL INTERPRETATION ----------------
st.markdown("---")

st.markdown("""
<div style='background-color:#e3f2fd; padding:15px; border-radius:12px;'>

<h4 style='color:#1f4e79;'>🧠 Clinical Interpretation</h4>
""", unsafe_allow_html=True)

if mood:
    st.write("• Mood instability may affect stimulant tolerability.")
if suicidal:
    st.write("• Suicidal ideation requires careful monitoring.")
if hallucination:
    st.write("• Psychotic symptoms may worsen with stimulants.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SUMMARY ----------------
st.markdown("---")

st.markdown("""
<div style='background-color:#ede7f6; padding:15px; border-radius:12px;'>

<h4 style='color:#4b2c5e;'>📄 Patient Summary</h4>
""", unsafe_allow_html=True)

st.write(f"Risk Level: {risk}")
st.write(f"Score: {score}")

if risk == "HIGH":
    st.write("Recommendation: Prefer non-stimulant therapy")
elif risk == "MODERATE":
    st.write("Recommendation: Individualized treatment approach")
else:
    st.write("Recommendation: Standard stimulant therapy")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESEARCH TEAM ----------------
st.markdown("---")

st.markdown("""
<div class='footer-box'>

<b>Research Team Name:</b> Samson K. Wilson <br>
<b>Research Student:</b> Samson K. Wilson <br>
<b>Clinical Expert (Psychiatrist):</b> Dr. Srinivas Singisetti <br>
<b>Research Supervisor:</b> Dr. Amit Kundu

</div>
""", unsafe_allow_html=True)

# ---------------- DISCLAIMER ----------------
st.markdown("---")
st.warning("This tool is exploratory and does NOT replace clinical judgment.")
