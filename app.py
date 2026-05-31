import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Young Lord Market View",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD IMAGES
# =========================================================

logo = Image.open("images/logo.png")
banner = Image.open("images/banner.png")

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* ================================
MAIN APP
================================ */

.stApp {
    background: linear-gradient(
        135deg,
        #001B44 0%,
        #002E73 50%,
        #001B44 100%
    );
}

/* Remove top white gap */

header {
    visibility:hidden;
}

[data-testid="stToolbar"]{
    visibility:hidden;
}

[data-testid="stDecoration"]{
    visibility:hidden;
}

/* ================================
SIDEBAR
================================ */

section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #001437,
        #001F54,
        #002E73
    );
    border-right: 2px solid #FFD54F;
}

/* Sidebar text */

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Logo */

.sidebar-logo{
    text-align:center;
    margin-bottom:15px;
}

/* Sidebar title */

.sidebar-title{
    color:#FFD54F;
    font-size:32px;
    font-weight:800;
    text-align:center;
    margin-bottom:25px;
}

/* Navigation Card */

.nav-card{
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0px 4px 25px rgba(0,0,0,0.25);
}

/* ================================
BANNER
================================ */

.banner-img{
    border-radius:20px;
    overflow:hidden;
    border:4px solid white;
    box-shadow:0px 0px 35px rgba(255,213,79,.25);
}

/* ================================
HERO CARD
================================ */

.hero-box{
    background:#002A66;
    border:2px solid #FFD54F;
    border-radius:32px;
    padding:40px;
    margin-top:25px;
    margin-bottom:25px;
    box-shadow:0px 0px 25px rgba(255,213,79,.20);
}

.hero-title{
    color:white;
    font-size:64px;
    font-weight:900;
    line-height:1.1;
}

.hero-sub{
    color:#FFD54F;
    font-size:32px;
    font-weight:700;
}

.hero-text{
    color:white;
    font-size:24px;
}

/* ================================
SECTION TITLES
================================ */

.section-title{
    color:#FFD54F;
    font-size:46px;
    font-weight:800;
    margin-top:25px;
    margin-bottom:20px;
}

/* ================================
METRIC CARDS
================================ */

[data-testid="metric-container"]{
    background: rgba(255,255,255,0.06);
    border:1px solid rgba(255,213,79,.35);
    border-radius:18px;
    padding:20px;
}

[data-testid="stMetricLabel"]{
    color:white !important;
    font-size:18px !important;
    font-weight:600 !important;
}

[data-testid="stMetricValue"]{
    color:#FFD54F !important;
    font-size:42px !important;
    font-weight:900 !important;
}

[data-testid="stMetricDelta"]{
    color:#00FF88 !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* ================================
MOBILE
================================ */

@media (max-width:768px){

.hero-title{
    font-size:34px;
}

.hero-sub{
    font-size:22px;
}

.hero-text{
    font-size:18px;
}

.section-title{
    font-size:30px;
}

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.image(
        logo,
        use_container_width=True
    )

    st.markdown(
        "<div class='sidebar-title'>Young Lord</div>",
        unsafe_allow_html=True
    )

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
            "telephone"
        ],
        menu_icon="chat-left-text",
        default_index=0,
        styles={
            "container": {
                "padding": "10px",
                "background-color": "#FFFFFF",
                "border-radius": "18px"
            },
            "icon": {
                "color": "#001F54",
                "font-size": "20px"
            },
            "nav-link": {
                "font-size": "18px",
                "color": "#001F54",
                "padding": "12px",
                "margin": "5px"
            },
            "nav-link-selected": {
                "background-color": "#FF4B4B",
                "color": "white",
                "font-weight": "700"
            }
        }
    )

# =========================================================
# BANNER
# =========================================================

st.image(
    banner,
    use_container_width=True
)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class='hero-box'>

<div class='hero-title'>
Young Lord Market View
</div>

<br>

<div class='hero-sub'>
Research • Analyze • Automate
</div>

<br>

<div class='hero-text'>
Professional Market Research & Trading Technology Portal
</div>

</div>
""", unsafe_allow_html=True)
# =========================================================
# MARKET PULSE DASHBOARD
# =========================================================

st.markdown(
    "<div class='section-title'>📊 Market Pulse Dashboard</div>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "NIFTY Trend",
        "Bullish",
        "+2.3%"
    )

with col2:
    st.metric(
        "Market Sentiment",
        "Positive",
        "+15%"
    )

with col3:
    st.metric(
        "Leading Sector",
        "Capital Goods"
    )

with col4:
    st.metric(
        "Risk Level",
        "Moderate"
    )

st.divider()

# =========================================================
# RESEARCH CATEGORIES
# =========================================================

st.markdown(
    "<div class='section-title'>📚 Research Categories</div>",
    unsafe_allow_html=True
)

r1, r2, r3 = st.columns(3)

with r1:

    st.info("📈 Weekly Nifty Outlook")
    st.info("🔄 Sector Rotation Analysis")
    st.info("📊 Relative Strength Analysis")

with r2:

    st.info("🏢 Fundamental Analysis")
    st.info("📰 Macro & Current Affairs")
    st.info("📂 Stock Research Reports")

with r3:

    st.info("💡 Investment Ideas")
    st.info("⚙ Professional Services")
    st.info("📥 Report Downloads")

st.divider()

# =========================================================
# PROFESSIONAL SERVICES
# =========================================================

st.markdown(
    "<div class='section-title'>⚙ Professional Services</div>",
    unsafe_allow_html=True
)

st.success("""
We also offer end-to-end Strategy Development Services
tailored for traders, investors, analysts and institutions.
""")

svc1, svc2 = st.columns(2)

with svc1:

    st.markdown("""
### Development Services

✅ Python Development

✅ Pine Script Development

✅ TradingView Automation

✅ Broker API Integration

✅ Algo Trading Solutions

✅ Dashboard Development

✅ Google Sheets Automation
""")

with svc2:

    st.markdown("""
### Research & Analytics

✅ Equity Research

✅ Backtesting Frameworks

✅ Strategy Validation

✅ Relative Strength Analysis

✅ Sector Rotation Models

✅ Quantitative Research

✅ Custom Product Development
""")

st.markdown("""
<div style="
background:#073B4C;
padding:20px;
border-radius:15px;
border:1px solid #FFD54F;
margin-top:15px;
">

<h3 style="color:#FFD54F;">
Custom Trading Technology Solutions
</h3>

<p style="color:white;font-size:18px;">
We build custom scanners, dashboards,
research portals, strategy engines,
API integrations, automated reporting systems,
and institutional-grade market analysis tools.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# =========================================================
# REPORT ARCHIVE
# =========================================================

st.markdown(
    "<div class='section-title'>📁 Report Archive</div>",
    unsafe_allow_html=True
)

search_report = st.text_input(
    "🔍 Search Reports",
    placeholder="Search by stock, sector, theme, or report name..."
)

report_category = st.selectbox(
    "Filter Category",
    [
        "All Reports",
        "Weekly Nifty Outlook",
        "Sector Rotation",
        "Relative Strength",
        "Fundamental Analysis",
        "Current Affairs",
        "Investment Ideas"
    ]
)

st.markdown("### Available Reports")

report_col1, report_col2 = st.columns(2)

with report_col1:

    st.success("📈 Weekly Nifty Outlook")
    st.success("🏭 EMS Sector Outlook")
    st.success("⚡ Capital Goods Outlook")
    st.success("📊 Relative Strength Analysis")

with report_col2:

    st.success("🏢 Dixon Technologies")
    st.success("⚙ Cummins India")
    st.success("🏦 Banking Sector Outlook")
    st.success("💡 Investment Opportunities")

st.info(
    "PDF reports uploaded inside the reports folder will appear here in future upgrades."
)

st.divider()

# =========================================================
# FEATURED RESEARCH
# =========================================================

st.markdown(
    "<div class='section-title'>🏆 Featured Research</div>",
    unsafe_allow_html=True
)

feature1, feature2 = st.columns(2)

with feature1:

    st.markdown("""
    <div style="
    background:#073B4C;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #FFD54F;
    ">
    <h3 style="color:#FFD54F;">
    Dixon Technologies
    </h3>
    <p style="color:white;">
    EMS leadership, strong earnings momentum,
    improving relative strength and sector tailwinds.
    </p>
    </div>
    """, unsafe_allow_html=True)

with feature2:

    st.markdown("""
    <div style="
    background:#073B4C;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #FFD54F;
    ">
    <h3 style="color:#FFD54F;">
    Cummins India
    </h3>
    <p style="color:white;">
    Capital Goods leader with strong institutional
    participation and positive rotation profile.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================================================
# LIVE MARKET WIDGETS
# =========================================================

st.markdown(
    "<div class='section-title'>📈 Live Market Widgets</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:20px;
border-radius:15px;
border:1px solid #FFD54F;
">

<h3 style="color:#FFD54F;">
TradingView Integration Coming Soon
</h3>

<p style="color:white;">
This section will host:
</p>

<ul style="color:white;">
<li>NIFTY Live Chart</li>
<li>BANKNIFTY Live Chart</li>
<li>Market Heatmap</li>
<li>Sector Performance Dashboard</li>
<li>FII/DII Activity</li>
<li>Global Market Snapshot</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# NEWSLETTER
# =========================================================

st.markdown(
    "<div class='section-title'>📧 Newsletter</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:15px;
border:1px solid #FFD54F;
">
<h3 style="color:#FFD54F;">
Young Lord Research Newsletter
</h3>

<p style="color:white;">
Receive market outlook reports,
sector rotation updates,
stock research insights,
and investment ideas.
</p>
</div>
""", unsafe_allow_html=True)

email = st.text_input(
    "Email Address",
    placeholder="yourname@email.com"
)

if st.button("Subscribe"):
    st.success(
        "Newsletter subscription placeholder added successfully."
    )

st.divider()
# =========================================================
# CONTACT SECTION
# =========================================================

st.markdown(
    "<div class='section-title'>📞 Contact Us</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:15px;
border:1px solid #FFD54F;
">

<h3 style="color:#FFD54F;">
Let's Build Something Together
</h3>

<p style="color:white;">
Need a custom scanner, trading strategy,
dashboard, automation workflow,
or research platform?

Get in touch.
</p>

</div>
""", unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns(2)

with contact_col1:

    contact_name = st.text_input(
        "Full Name"
    )

    contact_email = st.text_input(
        "Email Address"
    )

with contact_col2:

    contact_phone = st.text_input(
        "Phone Number"
    )

    contact_subject = st.text_input(
        "Subject"
    )

contact_message = st.text_area(
    "Project Requirement / Message",
    height=150
)

if st.button("📨 Submit Inquiry"):
    st.success(
        "Thank you. Your inquiry has been received."
    )

st.divider()

# =========================================================
# WHATSAPP BUTTON
# =========================================================

st.markdown("""
<a href="https://wa.me/919999999999"
target="_blank">

<div style="
background:#25D366;
padding:15px;
border-radius:12px;
text-align:center;
font-size:20px;
font-weight:700;
color:white;
cursor:pointer;
margin-bottom:20px;
">

💬 WhatsApp Inquiry

</div>

</a>
""", unsafe_allow_html=True)

# =========================================================
# ABOUT YOUNG LORD
# =========================================================

st.markdown(
    "<div class='section-title'>🟡 About Young Lord Market View</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:15px;
border:1px solid #FFD54F;
">

<h3 style="color:#FFD54F;">
Research • Analyze • Automate
</h3>

<p style="color:white;font-size:18px;">

Young Lord Market View is a professional
market research and trading technology platform.

Coverage includes:

✔ Weekly Nifty Outlook

✔ Sector Rotation Analysis

✔ Relative Strength Analysis

✔ Fundamental Analysis

✔ Macro & Current Affairs

✔ Investment Ideas

✔ Stock Research Reports

✔ Strategy Development

✔ Trading Automation

✔ Quantitative Research

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# PERFORMANCE TRACKER
# =========================================================

st.markdown(
    "<div class='section-title'>🏆 Performance Tracker</div>",
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Research Reports",
        "150+"
    )

with p2:
    st.metric(
        "Strategies",
        "50+"
    )

with p3:
    st.metric(
        "Projects",
        "30+"
    )

with p4:
    st.metric(
        "Subscribers",
        "500+"
    )

st.divider()

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="
text-align:center;
padding:30px;
">

<h2 style="color:#FFD54F;">
Young Lord Market View
</h2>

<p style="color:white;font-size:18px;">
Research • Analyze • Automate
</p>

<p style="color:white;">
Professional Market Research,
Trading Technology &
Automation Solutions
</p>

<hr>

<p style="color:#cccccc;">
© 2026 Young Lord Market View
All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)
