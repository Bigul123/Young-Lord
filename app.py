import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="🟡",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#07111f,#0d1b2a,#14213d);
}
.hero {
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(90deg,#0d1b2a,#1b263b);
    border: 1px solid #d4af37;
}
.metric-box {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #d4af37;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🟡 YL")
menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Weekly Nifty Outlook",
        "Sector Rotation Analysis",
        "Relative Strength & Rotation",
        "Fundamental Analysis",
        "Macro & Current Affairs",
        "Investment Ideas",
        "Stock Research Reports",
        "Report Downloads",
        "Professional Services",
        "Contact",
        "About"
    ]
)

if menu == "Home":
    st.markdown("""
    <div class="hero">
    <h1>🟡 Young Lord Market View</h1>
    <h3>Research • Analyze • Automate</h3>
    <p>Professional Market Research & Trading Technology Portal</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Market Pulse Dashboard")

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("NIFTY Trend","Bullish")
    c2.metric("Market Sentiment","Positive")
    c3.metric("Leading Sector","Capital Goods")
    c4.metric("Risk Level","Moderate")

    st.markdown("---")
    st.markdown("## Research Categories")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.info("📈 Weekly Nifty Outlook")
        st.info("🔄 Sector Rotation Analysis")
        st.info("📊 Relative Strength & Rotation")

    with col2:
        st.info("💰 Fundamental Analysis")
        st.info("🌍 Macro & Current Affairs")
        st.info("⭐ Investment Ideas")

    with col3:
        st.info("📄 Stock Research Reports")
        st.info("📥 Report Download Center")
        st.info("⚙ Professional Services")

    st.markdown("## 📚 Featured Research")

    st.success("Weekly Nifty Outlook")
    st.success("Sector Rotation Report")
    st.success("Dixon Technologies")
    st.success("Cummins India")
    st.success("EMS Sector Outlook")

elif menu == "Report Downloads":
    st.title("📥 Report Download Center")

    reports = Path("reports")

    if reports.exists():
        pdfs = list(reports.glob("*.pdf"))

        if pdfs:
            for pdf in pdfs:
                with open(pdf, "rb") as f:
                    st.download_button(
                        f"📄 Download {pdf.name}",
                        data=f,
                        file_name=pdf.name
                    )
        else:
            st.warning("No PDF reports found.")
    else:
        st.warning("Create a reports folder and upload PDFs.")

elif menu == "Professional Services":
    st.title("⚙ Professional Services")

    st.markdown("""
### End-to-End Trading & Research Solutions

✓ Python Strategy Development

✓ TradingView Pine Script Development

✓ Broker API Integration

✓ Research & Backtesting

✓ Algo Trading Solutions

✓ Dashboard Development

✓ Market Scanners

✓ Google Sheets Automation

✓ Custom Product Development

✓ Workflow Automation
""")

elif menu == "Contact":
    st.title("📞 Contact Us")

    st.markdown("""
### Interested in a Custom Solution?

📧 Email

contact@younglordresearch.com

📱 WhatsApp

+91 XXXXXXXXXX

📢 Telegram

Coming Soon

💼 LinkedIn

Coming Soon
""")

elif menu == "About":
    st.title("About Young Lord Market View")

    st.markdown("""
Research • Analyze • Automate

Professional Market Research & Trading Technology Solutions.

Coverage:

- Weekly Nifty Outlook
- Sector Rotation Analysis
- Relative Strength & Rotation
- Fundamental Analysis
- Macro & Current Affairs
- Investment Ideas
- Stock Research Reports
""")

else:
    st.title(menu)
    st.info(f"Content for '{menu}' will be added here.")
