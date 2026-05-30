import streamlit as st

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Young Lord Market View")

st.markdown("""
## Welcome

Professional Equity Market Research Portal

### Available Reports

- Weekly Nifty Outlook
- Sector Rotation Analysis
- Relative Strength Analysis
- Stock Research Reports
- Fundamental Analysis
- Current Affairs
- Investment Ideas
- Market Commentary

---
""")

st.header("Latest Market View")

st.info("""
This portal publishes equity research reports,
sector rotation analysis, stock recommendations,
fundamental research, current affairs,
and market outlook reports.
""")

st.header("About")

st.write("""
Research focused on:

- NIFTY Analysis
- Sector Rotation
- Relative Strength Analysis
- Fundamental Analysis
- Current Affairs
- Stock Selection
- Technical & Positional Trading
""")
