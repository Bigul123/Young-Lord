
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Young Lord Market View", page_icon="🟡", layout="wide")

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#07111f,#0d1b2a,#14213d);
}
.hero{
background: linear-gradient(135deg,#02101f,#102a56);
padding:60px;
border-radius:25px;
border:2px solid #d4af37;
box-shadow:0 0 25px rgba(212,175,55,.35);
}
.gold-logo{
width:90px;height:90px;border-radius:50%;
background:linear-gradient(135deg,#ffd700,#d4af37);
display:flex;align-items:center;justify-content:center;
font-size:34px;font-weight:bold;color:#08111f;
}
.card{
padding:20px;border-radius:15px;
background:#11243d;
border:1px solid #d4af37;
margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🟡 YL")
page = st.sidebar.radio("Navigation",[
"Home","Weekly Nifty Outlook","Sector Rotation Analysis",
"Relative Strength & Rotation","Fundamental Analysis",
"Macro & Current Affairs","Investment Ideas",
"Stock Research Reports","Report Downloads",
"Professional Services","Performance Tracker",
"Newsletter","Contact","About"
])

if page=="Home":
    st.markdown("""
    <div class='hero'>
    <h1 style='color:white;font-size:60px;'>🟡 YOUNG LORD MARKET VIEW</h1>
    <h2 style='color:#d4af37;'>Research • Analyze • Automate</h2>
    <p style='color:white;font-size:22px;'>
    Professional Market Research & Trading Technology Portal
    </p>
    <p style='color:#d4af37;'>
    🐂 Bull Market • 📈 Charts • 🌆 Market Skyline
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Market Pulse Dashboard")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("NIFTY Trend","Bullish")
    c2.metric("Market Sentiment","Positive")
    c3.metric("Leading Sector","Capital Goods")
    c4.metric("Risk Level","Moderate")

    st.markdown("## 📚 Research Categories")
    a,b,c=st.columns(3)
    a.info("📈 Weekly Nifty Outlook")
    a.info("🔄 Sector Rotation Analysis")
    a.info("📊 Relative Strength & Rotation")
    b.info("💰 Fundamental Analysis")
    b.info("🌍 Macro & Current Affairs")
    b.info("⭐ Investment Ideas")
    c.info("📄 Stock Research Reports")
    c.info("📥 Report Download Center")
    c.info("⚙ Professional Services")

    st.markdown("## 🏆 Featured Research")
    st.success("Dixon Technologies")
    st.success("Cummins India")
    st.success("EMS Sector Outlook")
    st.success("Weekly Nifty Outlook")

    st.markdown("## 📈 Live Market Widgets")
    st.info("Embed TradingView widgets here later.")

elif page=="Report Downloads":
    st.title("📥 Report Download Center")
    reports = Path("reports")
    if reports.exists():
        pdfs=list(reports.glob("*.pdf"))
        for pdf in pdfs:
            with open(pdf,"rb") as f:
                st.download_button(
                    f"📄 Download {pdf.name}",f.read(),pdf.name
                )
    else:
        st.warning("Create reports folder and upload PDFs.")

elif page=="Professional Services":
    st.title("⚙ Professional Services")
    st.markdown("""
### Strategy Development
✓ Quant Research
✓ Trading Systems

### Python Development
✓ Market Scanners
✓ Dashboards
✓ Automation

### Pine Script Development
✓ Indicators
✓ Strategies
✓ Alerts

### API Integration
✓ Zerodha
✓ Bigul
✓ XTS
✓ Custom APIs

### Research & Backtesting
✓ Historical Testing
✓ Validation

### Custom Product Development
✓ Research Portals
✓ Trading Platforms
✓ Analytics Solutions
""")

elif page=="Performance Tracker":
    st.title("🏆 Research Performance")
    st.metric("Success Rate","75%")
    st.metric("Average Return","14.2%")
    st.metric("Ideas Published","24")

elif page=="Newsletter":
    st.title("📧 Newsletter Signup")
    st.text_input("Email Address")
    st.button("Subscribe")

elif page=="Contact":
    st.title("📞 Contact Us")

    st.text_input("Name")
    st.text_input("Email")
    st.text_area("Message")
    st.button("Send Inquiry")

    st.markdown("""
### Quick Contact

📧 contact@younglordresearch.com

📱 +91 XXXXXXXXXX

💬 WhatsApp Inquiry Available

💼 LinkedIn Coming Soon
""")

else:
    st.title(page)
    st.info(f"Content section: {page}")
