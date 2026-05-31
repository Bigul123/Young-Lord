import streamlit as st
from streamlit_option_menu import option_menu

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

/* Hide Streamlit Header */
header {
    visibility:hidden;
}

[data-testid="stHeader"] {
    display:none;
}

/* Main Background */
.stApp {
    background: linear-gradient(90deg,#00142e,#032a5c);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#001634;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Cards */
.card{
    background:#082c57;
    padding:20px;
    border-radius:15px;
    border:1px solid #d4af37;
}

/* Titles */
.gold{
    color:#d4af37;
}

/* Hero */
.hero{
    background:linear-gradient(90deg,#00142e,#032a5c);
    border:2px solid #d4af37;
    border-radius:25px;
    padding:35px;
    margin-top:10px;
    margin-bottom:20px;
}

.hero-title{
    font-size:52px;
    font-weight:700;
    color:white;
}

.hero-sub{
    color:#d4af37;
    font-size:28px;
    font-weight:600;
}

.hero-desc{
    color:white;
    font-size:20px;
}

/* Metrics */
[data-testid="metric-container"]{
    background:#082c57;
    border-radius:15px;
    padding:15px;
    border:1px solid #d4af37;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:#082c57 !important;
    color:white !important;
}

/* Buttons */
.stButton button{
    background:#d4af37;
    color:black;
    border:none;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.image("images/logo.png", width=180)

    st.markdown("## Young Lord")

    selected = option_menu(
        "Navigation",
        [
            "Home",
            "Weekly Nifty Outlook",
            "Sector Rotation",
            "Relative Strength",
            "Fundamental Analysis",
            "Current Affairs",
            "Investment Ideas",
            "Research Reports",
            "Professional Services",
            "Contact"
        ],
        icons=[
            "house",
            "graph-up",
            "arrow-repeat",
            "bar-chart",
            "briefcase",
            "newspaper",
            "lightbulb",
            "file-earmark-text",
            "gear",
            "envelope"
        ],
        default_index=0
    )

# -------------------------------------------------
# HERO BANNER
# -------------------------------------------------

st.image("images/banner.png", use_container_width=True)

st.markdown("""
<div class="hero">
<div class="hero-title">
Young Lord Market View
</div>

<div class="hero-sub">
Research • Analyze • Automate
</div>

<br>

<div class="hero-desc">
Professional Market Research & Trading Technology Portal
</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

st.markdown("## 📊 Market Pulse Dashboard")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "NIFTY Trend",
        "Bullish",
        "+2.3%"
    )

with c2:
    st.metric(
        "Market Sentiment",
        "Positive",
        "+15%"
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

st.divider()

# -------------------------------------------------
# RESEARCH CATEGORIES
# -------------------------------------------------

st.markdown("## 📚 Research Categories")

c1,c2,c3 = st.columns(3)

with c1:
    st.info("📈 Weekly Nifty Outlook")
    st.info("🔄 Sector Rotation")
    st.info("📊 Relative Strength")

with c2:
    st.info("🏢 Fundamental Analysis")
    st.info("📰 Current Affairs")
    st.info("💡 Investment Ideas")

with c3:
    st.info("📑 Research Reports")
    st.info("⚙ Professional Services")
    st.info("📬 Contact")

# -------------------------------------------------
# SERVICES
# -------------------------------------------------

st.markdown("## ⚙ Professional Services")

st.success("""
We also offer end-to-end Strategy Development Services:

✅ Python Coding

✅ Pine Script Development

✅ API Integration

✅ Research & Backtesting

✅ Algo Trading Solutions

✅ Dashboard Development

✅ Custom Product Development

Tailored to your trading and automation requirements.
""")

# -------------------------------------------------
# REPORT ARCHIVE
# -------------------------------------------------

st.markdown("## 📂 Report Archive")

report = st.selectbox(
    "Select Report",
    [
        "Weekly Nifty Outlook",
        "Sector Rotation Analysis",
        "Relative Strength Analysis",
        "Fundamental Analysis",
        "Investment Ideas"
    ]
)

st.info(f"Selected Report: {report}")

st.button("📥 Download Report")

# -------------------------------------------------
# LIVE MARKET WIDGETS
# -------------------------------------------------

st.markdown("## 📈 Live Market Widgets")

st.info("""
TradingView widgets will be added in the next upgrade.
""")

# -------------------------------------------------
# NEWSLETTER
# -------------------------------------------------

st.markdown("## 📧 Newsletter")

email = st.text_input(
    "Enter Email Address"
)

st.button("Subscribe")

# -------------------------------------------------
# CONTACT
# -------------------------------------------------

st.markdown("## 📞 Contact")

name = st.text_input("Name")

message = st.text_area("Message")

st.button("Send Inquiry")

st.success("""
WhatsApp Integration Coming Soon
""")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "© Young Lord Market View | Research • Analyze • Automate"
)
