st.markdown("""
<style>

/* =====================================================
MAIN BACKGROUND
===================================================== */

.stApp{
background:linear-gradient(
135deg,
#001B44 0%,
#002E73 50%,
#001B44 100%
);
}

/* =====================================================
HEADER
===================================================== */

header{
background:transparent !important;
}

[data-testid="stToolbar"]{
visibility:hidden;
}

[data-testid="stDecoration"]{
visibility:hidden;
}

/* =====================================================
TEXT VISIBILITY FIX
===================================================== */

p,
li,
span,
div{
color:white;
}

label{
color:white !important;
}

.stMarkdown{
color:white !important;
}

h1,h2,h3,h4,h5,h6{
color:#FFD54F !important;
}

/* =====================================================
SIDEBAR
===================================================== */

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

/* =====================================================
HERO
===================================================== */

.hero-box{
background:#002A66;
border:2px solid #FFD54F;
border-radius:28px;
padding:40px;
margin-top:20px;
margin-bottom:25px;
box-shadow:0px 0px 20px rgba(255,213,79,.20);
}

.hero-title{
font-size:clamp(36px,5vw,64px);
font-weight:900;
color:white;
}

.hero-sub{
font-size:clamp(20px,3vw,32px);
font-weight:700;
color:#FFD54F;
}

.hero-desc{
font-size:clamp(16px,2vw,22px);
color:white;
}

/* =====================================================
SECTION HEADINGS
===================================================== */

.section-title{
font-size:clamp(28px,3vw,46px);
font-weight:800;
color:#FFD54F;
margin-top:20px;
margin-bottom:20px;
}

/* =====================================================
METRICS
===================================================== */

[data-testid="metric-container"]{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,213,79,.35);
border-radius:18px;
padding:18px;
}

[data-testid="stMetricLabel"]{
color:white !important;
font-size:18px !important;
font-weight:700 !important;
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

/* =====================================================
CUSTOM CARDS
===================================================== */

.custom-card{
background:#0B4F6C;
padding:18px;
border-radius:14px;
margin-bottom:12px;
border-left:5px solid #FFD54F;
color:white;
font-size:18px;
font-weight:600;
}

/* =====================================================
INPUTS
===================================================== */

input,
textarea{
color:white !important;
}

/* =====================================================
SELECT BOX
===================================================== */

.stSelectbox div[data-baseweb="select"]{
background:#073B4C !important;
color:white !important;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton button{
background:#FFD54F;
color:black;
font-weight:700;
border:none;
border-radius:10px;
}

.stButton button:hover{
background:white;
color:black;
}

/* =====================================================
MOBILE RESPONSIVE FIX
===================================================== */

@media (max-width:768px){

.hero-title{
font-size:34px;
}

.hero-sub{
font-size:22px;
}

.hero-desc{
font-size:16px;
}

.section-title{
font-size:30px;
}

/* Sidebar Width */

[data-testid="stSidebar"]{
min-width:300px !important;
}

/* Better spacing */

.stSelectbox{
margin-bottom:20px;
}

/* Metrics stack nicely */

[data-testid="metric-container"]{
margin-bottom:10px;
}

}

</style>
""", unsafe_allow_html=True)
# =====================================================
# MARKET PULSE DASHBOARD
# =====================================================

st.markdown(
    "<div class='section-title'>📊 Market Pulse Dashboard</div>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "NIFTY Trend",
        NIFTY_TREND,
        "+2.3%"
    )

with c2:
    st.metric(
        "Market Sentiment",
        MARKET_SENTIMENT,
        "+15%"
    )

c3, c4 = st.columns(2)

with c3:
    st.metric(
        "Leading Sector",
        LEADING_SECTOR
    )

with c4:
    st.metric(
        "Risk Level",
        RISK_LEVEL
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

    st.markdown("""
    <div class='custom-card'>
    📈 Weekly Nifty Outlook
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🔄 Sector Rotation Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    ⚡ Relative Strength Analysis
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='custom-card'>
    💰 Fundamental Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🌍 Current Affairs
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    💡 Investment Ideas
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='custom-card'>
    📄 Research Reports
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📥 Report Downloads
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📊 Market Commentary
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# PROFESSIONAL SERVICES
# =====================================================

st.markdown(
    "<div class='section-title'>⚙ Professional Services</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
border:1px solid #FFD54F;
margin-bottom:20px;
">

<h3 style="color:#FFD54F;">
End-to-End Trading Technology Solutions
</h3>

<p style="color:white;font-size:18px;">
We provide professional research,
automation and development services
tailored to traders, investors and institutions.
</p>

</div>
""", unsafe_allow_html=True)

svc1, svc2 = st.columns(2)

with svc1:

    st.markdown("""
    <div class='custom-card'>
    🐍 Python Development
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📈 Pine Script Development
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🔌 API Integration
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🤖 Algo Trading Solutions
    </div>
    """, unsafe_allow_html=True)

with svc2:

    st.markdown("""
    <div class='custom-card'>
    📊 Research & Backtesting
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📉 Market Scanners
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🖥 Dashboard Development
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    ⚙ Custom Product Development
    </div>
    """, unsafe_allow_html=True)

st.divider()
# =====================================================
# REPORT ARCHIVE
# =====================================================

st.markdown(
    "<div class='section-title'>📂 Report Archive</div>",
    unsafe_allow_html=True
)

report_search = st.text_input(
    "🔍 Search Research Reports",
    placeholder="Search by report name, sector or theme..."
)

report_category = st.selectbox(
    "Research Category",
    [
        "All Reports",
        "Weekly Nifty Outlook",
        "Sector Rotation",
        "Relative Strength",
        "Fundamental Analysis",
        "Current Affairs",
        "Investment Ideas",
        "Research Reports"
    ]
)

st.markdown("""
<div style="
background:#073B4C;
padding:20px;
border-radius:15px;
border:1px solid #FFD54F;
margin-top:10px;
">

<h3 style="color:#FFD54F;">
Research Library
</h3>

<p style="color:white;">
Upload PDF reports into the reports folder.
Future versions will automatically display them here.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("### Available Research")

r1, r2 = st.columns(2)

with r1:

    st.markdown("""
    <div class='custom-card'>
    📈 Weekly Nifty Outlook
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    🔄 Sector Rotation Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    ⚡ Relative Strength Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    💰 Fundamental Analysis
    </div>
    """, unsafe_allow_html=True)

with r2:

    st.markdown("""
    <div class='custom-card'>
    🌍 Current Affairs
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    💡 Investment Ideas
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📄 Stock Research Reports
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='custom-card'>
    📊 Market Commentary
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# FEATURED RESEARCH
# =====================================================

st.markdown(
    "<div class='section-title'>🏆 Featured Research</div>",
    unsafe_allow_html=True
)

fr1, fr2 = st.columns(2)

with fr1:

    st.markdown("""
    <div style="
    background:#073B4C;
    padding:20px;
    border-radius:15px;
    border:1px solid #FFD54F;
    margin-bottom:15px;
    ">

    <h3 style="color:#FFD54F;">
    Weekly Nifty Outlook
    </h3>

    <p style="color:white;">
    Market trend, support, resistance,
    positional view and probability analysis.
    </p>

    </div>
    """, unsafe_allow_html=True)

with fr2:

    st.markdown("""
    <div style="
    background:#073B4C;
    padding:20px;
    border-radius:15px;
    border:1px solid #FFD54F;
    margin-bottom:15px;
    ">

    <h3 style="color:#FFD54F;">
    Sector Rotation Analysis
    </h3>

    <p style="color:white;">
    Sector leadership,
    relative strength
    and rotation framework.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# LIVE MARKET CENTER
# =====================================================

st.markdown(
    "<div class='section-title'>📈 Live Market Widgets</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
border:1px solid #FFD54F;
">

<h3 style="color:#FFD54F;">
TradingView Integration
</h3>

<p style="color:white;">
Upcoming live market dashboard:
</p>

<ul style="color:white;">

<li>NIFTY Live Chart</li>

<li>BANKNIFTY Live Chart</li>

<li>Market Heatmap</li>

<li>Sector Performance Dashboard</li>

<li>Relative Strength Dashboard</li>

<li>Global Market Snapshot</li>

<li>FII / DII Activity</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# MARKET INSIGHT
# =====================================================

st.markdown(
    "<div class='section-title'>📊 Market Insight</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
border:1px solid #FFD54F;
">

<p style="color:white;font-size:18px;">

Current Market Trend:
<b>{NIFTY_TREND}</b>

<br><br>

Market Sentiment:
<b>{MARKET_SENTIMENT}</b>

<br><br>

Leading Sector:
<b>{LEADING_SECTOR}</b>

<br><br>

Risk Level:
<b>{RISK_LEVEL}</b>

</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# =====================================================
# NEWSLETTER
# =====================================================

st.markdown(
    "<div class='section-title'>📧 Newsletter</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
border:1px solid #FFD54F;
margin-bottom:20px;
">

<h3 style="color:#FFD54F;">
Young Lord Research Newsletter
</h3>

<p style="color:white;font-size:18px;">
Receive:

• Weekly Nifty Outlook

• Sector Rotation Updates

• Relative Strength Analysis

• Investment Ideas

• Market Commentary

directly in your inbox.
</p>

</div>
""", unsafe_allow_html=True)

newsletter_email = st.text_input(
    "Email Address",
    placeholder="yourname@email.com"
)

if st.button("📩 Subscribe"):
    st.success("Subscription request received.")

st.divider()

# =====================================================
# CONTACT US
# =====================================================

st.markdown(
    "<div class='section-title'>📞 Contact Us</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
border:1px solid #FFD54F;
margin-bottom:20px;
">

<h3 style="color:#FFD54F;">
Let's Build Something Together
</h3>

<p style="color:white;font-size:18px;">
Need custom trading technology,
research automation,
dashboard development,
API integration,
or strategy development?

Get in touch.
</p>

</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    contact_name = st.text_input(
        "Full Name"
    )

    contact_email = st.text_input(
        "Email Address"
    )

with c2:

    contact_phone = st.text_input(
        "Phone Number"
    )

    contact_subject = st.text_input(
        "Subject"
    )

contact_message = st.text_area(
    "Project Requirement",
    height=150
)

if st.button("📨 Submit Inquiry"):
    st.success(
        "Thank you. Your inquiry has been submitted."
    )

st.divider()

# =====================================================
# WHATSAPP
# =====================================================

st.markdown(
    "<div class='section-title'>💬 WhatsApp Support</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">

<div style="
background:#25D366;
padding:18px;
border-radius:15px;
text-align:center;
font-size:22px;
font-weight:700;
color:white;
margin-bottom:20px;
">

💬 Chat on WhatsApp

</div>

</a>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# PERFORMANCE TRACKER
# =====================================================

st.markdown(
    "<div class='section-title'>🏆 Performance Tracker</div>",
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Reports Published",
        "150+"
    )

with p2:
    st.metric(
        "Strategies Built",
        "50+"
    )

with p3:
    st.metric(
        "Projects Delivered",
        "30+"
    )

with p4:
    st.metric(
        "Subscribers",
        "500+"
    )

st.divider()

# =====================================================
# ABOUT
# =====================================================

st.markdown(
    "<div class='section-title'>🟡 About Young Lord Market View</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#073B4C;
padding:25px;
border-radius:18px;
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

✔ Current Affairs

✔ Investment Ideas

✔ Stock Research Reports

✔ Strategy Development

✔ Trading Automation

✔ Quantitative Research

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div style="
text-align:center;
padding:40px;
">

<h2 style="
color:#FFD54F;
font-weight:800;
">
Young Lord Market View
</h2>

<p style="
color:white;
font-size:20px;
">
Research • Analyze • Automate
</p>

<p style="
color:white;
font-size:16px;
">
Professional Market Research,
Trading Technology &
Automation Solutions
</p>

<hr>

<p style="
color:#cccccc;
font-size:14px;
">
© 2026 Young Lord Market View
All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)
