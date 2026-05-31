import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        90deg,
        #02152d 0%,
        #062b52 50%,
        #02152d 100%
    );
    color:white;
}

h1,h2,h3 {
    color:white !important;
}

[data-testid="stSidebar"] {
    background-color:#081a33;
}

.gold {
    color:#f4c542;
}

.hero {
    padding:30px;
    border-radius:20px;
    background:rgba(0,0,0,0.25);
    border:2px solid #f4c542;
}

.metric-card {
    background:#0c2447;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

.service-card {
    background:#0c2447;
    padding:20px;
    border-radius:15px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD IMAGES
# =========================

logo = Image.open("images/logo.png")
banner = Image.open("images/banner.png")

# =========================
# SIDEBAR
# =========================

st.sidebar.image(logo, width=120)

st.sidebar.title("Young Lord")

st.sidebar.markdown("""
### Navigation

- Home
- Weekly Nifty Outlook
- Sector Rotation
- Relative Strength
- Fundamental Analysis
- Current Affairs
- Investment Ideas
- Research Reports
- Professional Services
- Contact
""")

# =========================
# HERO
# =========================

st.image(
    banner,
    use_container_width=True
)

st.markdown("""
<div class="hero">

<h1>Young Lord Market View</h1>

<h3 class="gold">
Research • Analyze • Automate
</h3>

<p>
Professional Market Research &
Trading Technology Portal
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# MARKET DASHBOARD
# =========================

st.markdown("## 📊 Market Pulse Dashboard")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "NIFTY Trend",
        "Bullish"
    )

with c2:
    st.metric(
        "Market Sentiment",
        "Positive"
    )

with c3:
    st.metric(
        "Leading Sector",
        "Capital Goods"
    )

with c4:
    st.metric(
        "Risk Level",
        "Moderate"
    )

# =========================
# RESEARCH CATEGORIES
# =========================

st.markdown("## 📚 Research Categories")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("Weekly Nifty Outlook")
    st.info("Sector Rotation Analysis")

with col2:
    st.info("Relative Strength Analysis")
    st.info("Fundamental Analysis")

with col3:
    st.info("Current Affairs")
    st.info("Investment Ideas")

# =========================
# SERVICES
# =========================

st.markdown("## ⚙️ Professional Services")

st.success("""
We offer end-to-end Strategy Development Services including:

✅ Python Development

✅ Pine Script Development

✅ TradingView Automation

✅ API Integration

✅ Research & Backtesting

✅ Stock Scanners

✅ Dashboard Development

✅ Algo Trading Solutions

✅ Custom Product Development
""")

# =========================
# REPORT ARCHIVE
# =========================

st.markdown("## 📁 Report Archive")

st.button("Weekly Nifty Outlook")

st.button("Sector Rotation Report")

st.button("Fundamental Research")

st.button("Market Commentary")

# =========================
# LIVE MARKET
# =========================

st.markdown("## 📈 Live Market Widgets")

st.info(
    "TradingView widgets will be added in the next upgrade."
)

# =========================
# NEWSLETTER
# =========================

st.markdown("## 📧 Newsletter")

email = st.text_input(
    "Enter Email"
)

if st.button("Subscribe"):
    st.success(
        "Subscription received."
    )

# =========================
# CONTACT
# =========================

st.markdown("## 📞 Contact")

name = st.text_input("Name")

message = st.text_area(
    "Message"
)

if st.button("Send Inquiry"):
    st.success(
        "Inquiry submitted."
    )

# =========================
# WHATSAPP
# =========================

st.markdown("""
<a href="https://wa.me/919999999999"
target="_blank">

<button style="
background:#25D366;
color:white;
padding:15px;
border:none;
border-radius:10px;
font-size:18px;
font-weight:bold;">

WhatsApp Inquiry

</button>

</a>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "© Young Lord Market View | Professional Equity Market Research Portal"
)
