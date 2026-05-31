import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

header,[data-testid="stHeader"]{
display:none !important;
}

#MainMenu{
visibility:hidden;
}

.stApp{
background:linear-gradient(
90deg,
#00142e,
#032a5c
);
}

section[data-testid="stSidebar"]{
background:linear-gradient(
180deg,
#00142e,
#001d42,
#00142e
);
}

section[data-testid="stSidebar"] *{
color:white !important;
}

.hero-card{
background:#03244d;
border:2px solid #d4af37;
border-radius:25px;
padding:35px;
margin-top:20px;
margin-bottom:20px;
}

.hero-title{
font-size:clamp(36px,5vw,60px);
font-weight:800;
color:white;
}

.hero-sub{
font-size:clamp(20px,3vw,32px);
font-weight:700;
color:#FFD54F;
}

.hero-desc{
font-size:20px;
color:white;
}

h1,h2,h3{
color:#FFD54F !important;
font-weight:700 !important;
}

[data-testid="metric-container"]{
background:#082c57;
border:1px solid #d4af37;
border-radius:15px;
padding:15px;
}

img{
max-width:100%;
height:auto;
}

@media (max-width:768px){

.hero-title{
font-size:32px;
}

.hero-sub{
font-size:20px;
}

.hero-desc{
font-size:15px;
}

}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.image(
        "images/logo.png",
        use_container_width=True
    )

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

st.image(
    "images/banner.png",
    use_container_width=True
)

st.markdown("""
<div class="hero-card">

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
# ==================================================
# MARKET PULSE DASHBOARD
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📊 Market Pulse Dashboard
</h2>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

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

c3, c4 = st.columns(2)

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

# ==================================================
# RESEARCH CATEGORIES
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📚 Research Categories
</h2>
""", unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.info("📈 Weekly Nifty Outlook")
    st.info("🔄 Sector Rotation Analysis")
    st.info("📊 Relative Strength Analysis")

with r2:
    st.info("💰 Fundamental Analysis")
    st.info("🌍 Macro & Current Affairs")
    st.info("⭐ Investment Ideas")

with r3:
    st.info("📄 Research Reports")
    st.info("📥 Report Downloads")
    st.info("📝 Market Commentary")

st.divider()

# ==================================================
# PROFESSIONAL SERVICES
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
⚙ Professional Services
</h2>
""", unsafe_allow_html=True)

st.success("""
Young Lord Market View provides end-to-end quantitative trading,
research and automation solutions.

✅ Python Development

✅ TradingView Pine Script Development

✅ Strategy Development

✅ API Integration

✅ Research & Backtesting

✅ Stock Scanners

✅ Dashboard Development

✅ Algo Trading Solutions

✅ Google Sheets Automation

✅ Custom Product Development

Tailored to your trading and automation requirements.
""")

st.divider()

# ==================================================
# REPORT ARCHIVE
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📂 Report Archive
</h2>
""", unsafe_allow_html=True)

report_category = st.selectbox(
    "Select Research Category",
    [
        "Weekly Nifty Outlook",
        "Sector Rotation Analysis",
        "Relative Strength Analysis",
        "Fundamental Analysis",
        "Macro & Current Affairs",
        "Investment Ideas"
    ]
)

st.info(f"Selected: {report_category}")

search_report = st.text_input(
    "🔎 Search Reports"
)

st.button("📥 Download Selected Report")

st.divider()

# ==================================================
# LIVE MARKET CENTER
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📈 Live Market Widgets
</h2>
""", unsafe_allow_html=True)

st.info("""
Upcoming Live Widgets:

• NIFTY

• BANKNIFTY

• NIFTY 500

• Market Heatmap

• Sector Performance

• TradingView Charts
""")

st.divider()

# ==================================================
# NEWSLETTER
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📧 Newsletter
</h2>
""", unsafe_allow_html=True)

newsletter_email = st.text_input(
    "Enter Email Address"
)

if st.button("Subscribe"):
    st.success(
        "Thank you for subscribing."
    )

st.divider()

# ==================================================
# CONTACT
# ==================================================

st.markdown("""
<h2 style='color:#FFD54F;'>
📞 Contact
</h2>
""", unsafe_allow_html=True)

contact_name = st.text_input(
    "Name"
)

contact_email = st.text_input(
    "Email"
)

contact_message = st.text_area(
    "Message"
)

if st.button("Send Inquiry"):
    st.success(
        "Inquiry submitted successfully."
    )

st.markdown("""
### Quick Contact

📧 contact@younglordresearch.com

📱 +91 XXXXXXXXXX

💬 WhatsApp Support

💼 LinkedIn Coming Soon
""")

st.divider()

# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<center>

<h3 style="color:#FFD54F;">
Young Lord Market View
</h3>

<p style="color:white;">
Research • Analyze • Automate
</p>

<p style="color:white;">
Professional Market Research &
Trading Technology Solutions
</p>

</center>
""", unsafe_allow_html=True)
