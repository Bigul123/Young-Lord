import streamlit as st

st.set_page_config(
    page_title="Nitin Market Research",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Nitin Market Research")

st.markdown("""
## Welcome

Professional Equity Market Research Portal

### Available Reports

- Weekly Nifty Outlook
- Sector Rotation Analysis
- RRG Analysis
- Stock Research Reports
- Investment Ideas
- Market Commentary

---
""")

st.header("Latest Market View")

st.info("""
This portal publishes equity research reports,
sector rotation analysis, stock recommendations,
and market outlook reports.
""")

st.header("About")

st.write("""
Research focused on:

- NIFTY Analysis
- Sector Rotation
- Relative Strength
- RRG Analysis
- Stock Selection
- Technical & Positional Trading
""")
