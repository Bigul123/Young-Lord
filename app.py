import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# =====================================================
# SETTINGS
# =====================================================

NIFTY_TREND = "Bullish"
MARKET_SENTIMENT = "Positive"
LEADING_SECTOR = "Capital Goods"
RISK_LEVEL = "Moderate"

WHATSAPP_NUMBER = "919999999999"
CONTACT_EMAIL = "contact@younglordresearch.com"

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="auto"
)

# =====================================================
# LOAD IMAGES
# =====================================================

logo = Image.open("images/logo.png")
banner = Image.open("images/banner.png")

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(
135deg,
#001B44 0%,
#002E73 50%,
#001B44 100%
);
}

h1,h2,h3,h4,h5,h6{
color:#FFD54F !important;
}

p,li,label,span{
color:white !important;
}

section[data-testid="stSidebar"]{
background:linear-gradient(
180deg,
#00142E,
#001F54,
#002E73
);
border-right:2px solid #FFD54F;
}

section[data-testid="stSidebar"] *{
color:white !important;
}

.hero-box{
background:#002A66;
border:2px solid #FFD54F;
border-radius:25px;
padding:40px;
margin-top:20px;
margin-bottom:20px;
}

.hero-title{
font-size:60px;
font-weight:900;
color:white;
}

.hero-sub{
font-size:28px;
font-weight:700;
color:#FFD54F;
}

.hero-desc{
font-size:22px;
color:white;
}

.section-title{
font-size:42px;
font-weight:800;
color:#FFD54F;
margin-top:20px;
margin-bottom:20px;
}

.custom-card{
background:#0B4F6C;
padding:18px;
border-radius:15px;
border-left:5px solid #FFD54F;
margin-bottom:12px;
color:white;
font-size:18px;
font-weight:600;
}

[data-testid="metric-container"]{
background:#073B4C;
border:1px solid #FFD54F;
border-radius:15px;
padding:15px;
}

[data-testid="stMetricLabel"]{
color:white !important;
font-size:18px !important;
}

[data-testid="stMetricValue"]{
color:#FFD54F !important;
font-size:40px !important;
font-weight:800 !important;
}

[data-testid="stMetricDelta"]{
color:#00FF88 !important;
}

@media (max-width:768px){

.hero-title{
font-size:36px;
}

.hero-sub{
font-size:22px;
}

.hero-desc{
font-size:16px;
}

[data-testid="stSidebar"]{
min-width:300px !important;
}

}

</style>
""", unsafe_allow_html=True)
# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        logo,
        width=260
    )

    st.markdown("## Young Lord")

    selected = option_menu(
        menu_title="Navigation",
        options=[
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
            "telephone"
        ],
        menu_icon="cast",
        default_index=0
    )

# =====================================================
# MOBILE QUICK MENU
# =====================================================

st.selectbox(
    "Quick Navigation",
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
    ]
)

# =====================================================
# BANNER
# =====================================================

st.image(
    banner,
    use_container_width=True
)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-box">

<div class="hero-title">
Young Lord Market View
</div>

<br>

<div class="hero-sub">
Research • Analyze • Automate
</div>

<br>

<div class="hero-desc">
Professional Market Research & Trading Technology Portal
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# MARKET PULSE DASHBOARD
# =====================================================

st.markdown(
    "<div class='section-title'>📊 Market Pulse Dashboard</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="NIFTY Trend",
        value=NIFTY_TREND,
        delta="+2.3%"
    )

with col2:
    st.metric(
        label="Market Sentiment",
        value=MARKET_SENTIMENT,
        delta="+15%"
    )

col3, col4 = st.columns(2)

with col3:
    st.metric(
        label="Leading Sector",
        value=LEADING_SECTOR
    )

with col4:
    st.metric(
        label="Risk Level",
        value=RISK_LEVEL
    )

st.divider()
# =====================================================
# RESEARCH CATEGORIES
# =====================================================

st.markdown(
    "<div class='section-title'>📚 Research Categories</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        "<div class='custom-card'>📈 Weekly Nifty Outlook</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>🔄 Sector Rotation Analysis</div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        "<div class='custom-card'>📊 Relative Strength Analysis</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>🏦 Fundamental Analysis</div>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        "<div class='custom-card'>📰 Current Affairs</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>💡 Investment Ideas</div>",
        unsafe_allow_html=True
    )

st.divider()

# =====================================================
# PROFESSIONAL SERVICES
# =====================================================

st.markdown(
    "<div class='section-title'>⚙ Professional Services</div>",
    unsafe_allow_html=True
)

st.info(
    "We offer end-to-end Strategy Development Services, including Python Coding, Pine Script Development, API Integration, Research & Backtesting, Trading Automation, Dashboard Development, and Custom Product Development."
)

svc1, svc2 = st.columns(2)

with svc1:

    st.markdown(
        "<div class='custom-card'>✅ Python Development</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Pine Script Development</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ TradingView Automation</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Broker API Integration</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Algo Trading Solutions</div>",
        unsafe_allow_html=True
    )

with svc2:

    st.markdown(
        "<div class='custom-card'>✅ Equity Research</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Backtesting Frameworks</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Relative Strength Analysis</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Sector Rotation Models</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='custom-card'>✅ Custom Product Development</div>",
        unsafe_allow_html=True
    )

st.divider()

# =====================================================
# REPORT ARCHIVE
# =====================================================

st.markdown(
    "<div class='section-title'>📁 Report Archive</div>",
    unsafe_allow_html=True
)

report_category = st.selectbox(
    "Select Report Category",
    [
        "Weekly Nifty Outlook",
        "Sector Rotation Reports",
        "Relative Strength Reports",
        "Fundamental Analysis",
        "Current Affairs",
        "Investment Ideas"
    ]
)

st.markdown(
    f"<div class='custom-card'>Selected Category: {report_category}</div>",
    unsafe_allow_html=True
)

st.success(
    "Upload PDF reports inside the reports folder. Future versions will automatically display downloadable report archives here."
)

st.divider()
# =====================================================
# LIVE MARKET WIDGETS
# =====================================================

st.markdown(
    "<div class='section-title'>📈 Live Market Widgets</div>",
    unsafe_allow_html=True
)

st.info(
    "TradingView live widgets will be integrated in the next upgrade."
)

widget_col1, widget_col2 = st.columns(2)

with widget_col1:
    st.markdown(
        "<div class='custom-card'>📊 NIFTY 50 Live Widget (Coming Soon)</div>",
        unsafe_allow_html=True
    )

with widget_col2:
    st.markdown(
        "<div class='custom-card'>🏦 BANKNIFTY Live Widget (Coming Soon)</div>",
        unsafe_allow_html=True
    )

st.divider()

# =====================================================
# NEWSLETTER
# =====================================================

st.markdown(
    "<div class='section-title'>📧 Newsletter</div>",
    unsafe_allow_html=True
)

newsletter_email = st.text_input(
    "Enter your email to receive research updates"
)

if st.button("Subscribe"):
    st.success(
        f"Thank you! Newsletter subscription received for: {newsletter_email}"
    )

st.divider()

# =====================================================
# CONTACT
# =====================================================

st.markdown(
    "<div class='section-title'>📞 Contact</div>",
    unsafe_allow_html=True
)

contact_col1, contact_col2 = st.columns(2)

with contact_col1:

    st.markdown(
        f"""
        <div class='custom-card'>
        📧 Email<br><br>
        {CONTACT_EMAIL}
        </div>
        """,
        unsafe_allow_html=True
    )

with contact_col2:

    st.markdown(
        f"""
        <div class='custom-card'>
        📱 WhatsApp<br><br>
        +{WHATSAPP_NUMBER}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("### Send Inquiry")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Submit Inquiry"):
    st.success(
        "Thank you. Your inquiry has been received."
    )

st.divider()

# =====================================================
# WHATSAPP BUTTON
# =====================================================

whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}"

st.markdown(
    f"""
    <a href="{whatsapp_url}" target="_blank">
        <button style="
            background:#25D366;
            color:white;
            border:none;
            padding:14px 28px;
            border-radius:10px;
            font-size:18px;
            font-weight:700;
            cursor:pointer;">
            💬 WhatsApp Inquiry
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
    <center>

    <h4 style='color:#FFD54F;'>
    Young Lord Market View
    </h4>

    <p style='color:white;'>
    Research • Analyze • Automate
    </p>

    <p style='color:#B8C7E0;'>
    Equity Research | Sector Rotation | Relative Strength |
    Trading Technology | Strategy Development
    </p>

    <p style='color:#8EA9D6;'>
    © 2026 Young Lord Market View. All Rights Reserved.
    </p>

    </center>
    """,
    unsafe_allow_html=True
)
