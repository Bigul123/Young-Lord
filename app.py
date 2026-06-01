# =====================================================
# YOUNG LORD MARKET VIEW V5
# PART 1
# IMPORTS + SETTINGS + GOOGLE SETUP
# =====================================================

import streamlit as st
import pandas as pd
import gspread
from PIL import Image
from streamlit_option_menu import option_menu

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

import io
from datetime import datetime

# =====================================================
# EDITABLE VARIABLES
# =====================================================

# -------------------------
# BRANDING
# -------------------------

COMPANY_NAME = "Young Lord Market View"

TAGLINE = "Research • Analyze • Automate"

COMPANY_DESCRIPTION = (
    "Professional Market Research & Trading Technology Portal"
)

# -------------------------
# CONTACT DETAILS
# -------------------------

CONTACT_EMAIL = "contact@younglordresearch.com"

SUPPORT_EMAIL = "support@younglordresearch.com"

PHONE_NUMBER = "+91 99999 99999"

WHATSAPP_NUMBER = "919999999999"

CONTACT_ADDRESS = "Ujjain, Madhya Pradesh, India"

# -------------------------
# SOCIAL MEDIA
# -------------------------

LINKEDIN_URL = ""

TWITTER_URL = ""

TELEGRAM_URL = ""

YOUTUBE_URL = ""

INSTAGRAM_URL = ""

# -------------------------
# ADMIN
# -------------------------

ADMIN_PASSWORD = "younglord2026"

# -------------------------
# GOOGLE DRIVE
# -------------------------

GOOGLE_DRIVE_FOLDER_ID = (
    "1ah1qjx7iaSn98ig-_LFMz19jVeezUBP9"
)

# -------------------------
# GOOGLE SHEET
# -------------------------

GOOGLE_SHEET_ID = (
    "1Cua2ID50Auw1pzlPls4lRSybu-Zuq50eHSUQFULvdYo"
)

REPORTS_SHEET = "Reports"

LEADS_SHEET = "Leads"

NEWSLETTER_SHEET = "Newsletter"

# -------------------------
# MARKET PULSE
# -------------------------

NIFTY_TREND = "Bullish"

MARKET_SENTIMENT = "Positive"

LEADING_SECTOR = "Capital Goods"

RISK_LEVEL = "Moderate"

# -------------------------
# REPORT CATEGORIES
# -------------------------

REPORT_CATEGORIES = [

    "Weekly Nifty Outlook",

    "Sector Rotation",

    "Relative Strength",

    "Fundamental Analysis",

    "Current Affairs",

    "Investment Ideas",

    "Research Reports",

    "Professional Services"

]

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title=COMPANY_NAME,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD IMAGES
# =====================================================

logo = Image.open("images/logo.png")

banner = Image.open("images/banner.png")

DEFAULT_THUMBNAIL = (
    "thumbnails/default_report.png"
)

# =====================================================
# GOOGLE AUTH
# =====================================================

@st.cache_resource
def connect_google():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes
    )

    gc = gspread.authorize(creds)

    drive_service = build(
        "drive",
        "v3",
        credentials=creds
    )

    return gc, drive_service


gc, drive_service = connect_google()

# =====================================================
# OPEN GOOGLE SHEET
# =====================================================

@st.cache_resource
def open_workbook():

    return gc.open_by_key(
        GOOGLE_SHEET_ID
    )

workbook = open_workbook()

# =====================================================
# WORKSHEETS
# =====================================================

reports_ws = workbook.worksheet(
    REPORTS_SHEET
)

leads_ws = workbook.worksheet(
    LEADS_SHEET
)

newsletter_ws = workbook.worksheet(
    NEWSLETTER_SHEET
)

# =====================================================
# HELPERS
# =====================================================

def add_lead(
    name,
    email,
    phone,
    subject,
    message
):

    leads_ws.append_row([
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        name,
        email,
        phone,
        subject,
        message
    ])

def add_newsletter_email(
    email
):

    newsletter_ws.append_row([
        email,
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    ])

# =====================================================
# END PART 1
# =====================================================
# =====================================================
# V5 PART 2
# PROFESSIONAL CSS + SIDEBAR + TICKER TAPE
# =====================================================

st.markdown("""
<style>

/* =====================================================
   GLOBAL APP
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
   REMOVE STREAMLIT HEADER
===================================================== */

header{
visibility:hidden;
height:0rem;
}

[data-testid="stHeader"]{
background:transparent !important;
height:0px !important;
}

.main .block-container{
padding-top:0rem !important;
margin-top:-2rem !important;
}

/* =====================================================
   TEXT COLORS
===================================================== */

h1,h2,h3,h4,h5,h6{
color:#FFD54F !important;
font-weight:800 !important;
}

p,label,span,li{
color:white !important;
}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{
background:linear-gradient(
180deg,
#00142E 0%,
#001F54 50%,
#002E73 100%
);
border-right:2px solid #FFD54F;
}

section[data-testid="stSidebar"] *{
color:white !important;
}

[data-testid="stSidebarNav"]{
display:none;
}

/* =====================================================
   DROPDOWNS
===================================================== */

.stSelectbox div[data-baseweb="select"] > div{
background:#001F54 !important;
color:white !important;
border:1px solid #FFD54F !important;
}

.stSelectbox *{
color:white !important;
}

/* =====================================================
   INPUTS
===================================================== */

.stTextInput input,
.stTextArea textarea{
background:#001F54 !important;
color:white !important;
border:1px solid #FFD54F !important;
}

/* =====================================================
   BUTTONS
===================================================== */

.stButton button{
background:#FFD54F !important;
color:#001B44 !important;
font-weight:700 !important;
border:none !important;
border-radius:10px !important;
}

/* =====================================================
   HERO
===================================================== */

.hero-box{
background:#002A66;
border:2px solid #FFD54F;
border-radius:25px;
padding:40px;
margin-top:10px;
margin-bottom:25px;
}

.hero-title{
font-size:64px;
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

/* =====================================================
   SECTION TITLES
===================================================== */

.section-title{
font-size:42px;
font-weight:900;
color:#FFD54F;
margin-top:15px;
margin-bottom:20px;
}

/* =====================================================
   CUSTOM CARDS
===================================================== */

.custom-card{
background:#0B4F6C;
padding:18px;
border-radius:16px;
border-left:5px solid #FFD54F;
margin-bottom:12px;
font-size:18px;
font-weight:600;
color:white;
}

/* =====================================================
   METRICS
===================================================== */

[data-testid="metric-container"]{
background:#073B4C !important;
border:1px solid #FFD54F !important;
border-radius:18px !important;
padding:18px !important;
}

[data-testid="stMetricLabel"]{
color:white !important;
font-size:20px !important;
font-weight:700 !important;
}

[data-testid="stMetricValue"]{
color:#FFD54F !important;
font-size:42px !important;
font-weight:900 !important;
}

[data-testid="stMetricDelta"]{
color:#00FF88 !important;
font-weight:700 !important;
}

/* =====================================================
   REPORT CARDS
===================================================== */

.report-card{
background:#002A66;
border:1px solid #FFD54F;
border-radius:16px;
padding:15px;
margin-bottom:20px;
}

/* =====================================================
   FLOATING WHATSAPP
===================================================== */

.whatsapp-float{
position:fixed;
bottom:20px;
right:20px;
z-index:9999;
}

.whatsapp-float a{
background:#25D366;
padding:15px 18px;
border-radius:50px;
text-decoration:none;
font-weight:700;
color:white;
box-shadow:0 0 15px rgba(0,0,0,0.3);
}

/* =====================================================
   MOBILE
===================================================== */

@media (max-width:768px){

.hero-title{
font-size:34px;
}

.hero-sub{
font-size:20px;
}

.hero-desc{
font-size:16px;
}

.section-title{
font-size:28px;
}

[data-testid="stSidebar"]{
min-width:280px !important;
max-width:280px !important;
}

[data-testid="metric-container"]{
margin-bottom:10px !important;
}

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# FLOATING WHATSAPP BUTTON
# =====================================================

st.markdown(
    f"""
    <div class="whatsapp-float">
        <a href="https://wa.me/{WHATSAPP_NUMBER}"
           target="_blank">
           💬 WhatsApp
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        logo,
        width=300
    )

    st.markdown(
        f"## {COMPANY_NAME}"
    )

    st.markdown(
        f"**{TAGLINE}**"
    )

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Research Reports",
            "Professional Services",
            "Admin Panel",
            "Contact"
        ],
        icons=[
            "house",
            "file-earmark-text",
            "gear",
            "shield-lock",
            "telephone"
        ],
        default_index=0
    )

# =====================================================
# TRADINGVIEW TICKER TAPE
# =====================================================

st.components.v1.html(
"""
<script type="module"
src="https://widgets.tradingview-widget.com/w/en/tv-ticker-tape.js">
</script>

<tv-ticker-tape
symbols="NSE:NIFTY,NSE:BANKNIFTY,NSE:SBIN,NSE:ICICIBANK,NSE:HDFCBANK,NSE:TCS,NSE:INFY"
show-hover
theme="dark">
</tv-ticker-tape>
""",
height=60
)

# =====================================================
# BANNER
# =====================================================

st.image(
    banner,
    use_container_width=True
)

# =====================================================
# HERO
# =====================================================

st.markdown(
f"""
<div class="hero-box">

<div class="hero-title">
{COMPANY_NAME}
</div>

<br>

<div class="hero-sub">
{TAGLINE}
</div>

<br>

<div class="hero-desc">
{COMPANY_DESCRIPTION}
</div>

</div>
""",
unsafe_allow_html=True
)

# =====================================================
# END PART 2
# =====================================================
# =====================================================
# V5 PART 3
# MARKET PULSE + REPORT ARCHIVE
# =====================================================

# =====================================================
# MARKET PULSE
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
# TRADINGVIEW MARKET OVERVIEW
# =====================================================

st.markdown(
    "<div class='section-title'>📈 Live Market Overview</div>",
    unsafe_allow_html=True
)

st.components.v1.html(
"""
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>

<script type="text/javascript"
src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js"
async>
{
"colorTheme":"dark",
"dateRange":"12M",
"locale":"en",
"isTransparent":false,
"showFloatingTooltip":true,
"width":"100%",
"height":"700",
"showSymbolLogo":true,
"showChart":true,

"tabs":[

{
"title":"Indices",
"symbols":[
{"s":"NSE:NIFTY"},
{"s":"NSE:BANKNIFTY"}
]
},

{
"title":"Banking",
"symbols":[
{"s":"NSE:HDFCBANK"},
{"s":"NSE:ICICIBANK"},
{"s":"NSE:SBIN"},
{"s":"NSE:AXISBANK"}
]
},

{
"title":"IT",
"symbols":[
{"s":"NSE:TCS"},
{"s":"NSE:INFY"},
{"s":"NSE:WIPRO"}
]
},

{
"title":"Auto",
"symbols":[
{"s":"NSE:MARUTI"},
{"s":"NSE:TATAMOTORS"},
{"s":"NSE:M&M"}
]
},

{
"title":"FMCG",
"symbols":[
{"s":"NSE:ITC"},
{"s":"NSE:HINDUNILVR"},
{"s":"NSE:NESTLEIND"}
]
},

{
"title":"Energy",
"symbols":[
{"s":"NSE:RELIANCE"},
{"s":"NSE:ONGC"},
{"s":"NSE:POWERGRID"}
]
}

]
}
</script>
</div>
""",
height=750
)

st.divider()

# =====================================================
# RESEARCH CATEGORIES
# =====================================================

st.markdown(
    "<div class='section-title'>📚 Research Categories</div>",
    unsafe_allow_html=True
)

cols = st.columns(4)

for i, category in enumerate(REPORT_CATEGORIES):

    with cols[i % 4]:

        st.markdown(
            f"""
            <div class='custom-card'>
            📘 {category}
            </div>
            """,
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

services = [

    "Python Development",
    "Pine Script Development",
    "TradingView Automation",
    "Broker API Integration",
    "Algo Trading Solutions",

    "Equity Research",
    "Backtesting Frameworks",
    "Sector Rotation Models",
    "Relative Strength Models",
    "Custom Product Development"

]

svc_col1, svc_col2 = st.columns(2)

for i, service in enumerate(services):

    if i % 2 == 0:

        with svc_col1:
            st.markdown(
                f"""
                <div class='custom-card'>
                ✅ {service}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        with svc_col2:
            st.markdown(
                f"""
                <div class='custom-card'>
                ✅ {service}
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# =====================================================
# REPORT ARCHIVE
# =====================================================

st.markdown(
    "<div class='section-title'>📁 Research Report Archive</div>",
    unsafe_allow_html=True
)

search_text = st.text_input(
    "🔍 Search Reports"
)

selected_category = st.selectbox(
    "Select Category",
    ["All"] + REPORT_CATEGORIES
)

# =====================================================
# LOAD REPORTS FROM GOOGLE SHEET
# =====================================================

try:

    reports_data = reports_ws.get_all_records()

    reports_df = pd.DataFrame(
        reports_data
    )

except:

    reports_df = pd.DataFrame()

# =====================================================
# FILTER REPORTS
# =====================================================

if not reports_df.empty:

    if search_text:

        reports_df = reports_df[
            reports_df["Title"]
            .astype(str)
            .str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    if selected_category != "All":

        reports_df = reports_df[
            reports_df["Category"]
            == selected_category
        ]

# =====================================================
# DISPLAY REPORTS
# =====================================================

if reports_df.empty:

    st.info(
        "No reports found."
    )

else:

    for _, row in reports_df.iterrows():

        card1, card2 = st.columns(
            [1,3]
        )

        with card1:

            st.image(
                DEFAULT_THUMBNAIL,
                use_container_width=True
            )

        with card2:

            st.markdown(
                f"""
                <div class='report-card'>

                <h3>{row['Title']}</h3>

                <p>
                Category:
                {row['Category']}
                </p>

                <p>
                Date:
                {row['Date']}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if str(row.get(
                "PDF_Link",
                ""
            )).strip():

                st.link_button(
                    "📄 Open Report",
                    row["PDF_Link"]
                )

st.divider()

# =====================================================
# END PART 3
# =====================================================
# =====================================================
# V5 PART 4
# ADMIN PANEL
# =====================================================

if selected == "Admin Panel":

    st.markdown(
        "<div class='section-title'>🔐 Admin Panel</div>",
        unsafe_allow_html=True
    )

    admin_password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if admin_password != ADMIN_PASSWORD:

        st.warning(
            "Admin access required."
        )

    else:

        st.success(
            "Admin Access Granted"
        )

        st.markdown("### Upload Research Report")

        report_title = st.text_input(
            "Report Title"
        )

        report_category = st.selectbox(
            "Category",
            REPORT_CATEGORIES
        )

        report_date = st.date_input(
            "Report Date"
        )

        uploaded_pdf = st.file_uploader(
            "Upload PDF",
            type=["pdf"]
        )

        uploaded_thumbnail = st.file_uploader(
            "Upload Thumbnail (Optional)",
            type=["png", "jpg", "jpeg"]
        )

        # =====================================================
        # GOOGLE DRIVE UPLOAD FUNCTION
        # =====================================================

        def upload_to_drive(
            file_bytes,
            filename,
            mime_type
        ):

            file_metadata = {
                "name": filename,
                "parents": [
                    GOOGLE_DRIVE_FOLDER_ID
                ]
            }

            media = MediaIoBaseUpload(
                io.BytesIO(file_bytes),
                mimetype=mime_type,
                resumable=True
            )

            uploaded_file = (
                drive_service.files()
                .create(
                    body=file_metadata,
                    media_body=media,
                    fields="id"
                )
                .execute()
            )

            file_id = uploaded_file["id"]

            drive_service.permissions().create(
                fileId=file_id,
                body={
                    "type":"anyone",
                    "role":"reader"
                }
            ).execute()

            file_link = (
                f"https://drive.google.com/file/d/{file_id}/view"
            )

            return file_link

        # =====================================================
        # SUBMIT REPORT
        # =====================================================

        if st.button(
            "🚀 Upload Report"
        ):

            if (
                not report_title
                or uploaded_pdf is None
            ):

                st.error(
                    "Title and PDF are required."
                )

            else:

                try:

                    # ---------------------------------
                    # PDF Upload
                    # ---------------------------------

                    pdf_link = upload_to_drive(
                        uploaded_pdf.getvalue(),
                        uploaded_pdf.name,
                        "application/pdf"
                    )

                    # ---------------------------------
                    # THUMBNAIL UPLOAD
                    # ---------------------------------

                    thumbnail_link = ""

                    if uploaded_thumbnail:

                        thumbnail_link = upload_to_drive(
                            uploaded_thumbnail.getvalue(),
                            uploaded_thumbnail.name,
                            uploaded_thumbnail.type
                        )

                    # ---------------------------------
                    # GOOGLE SHEET UPDATE
                    # ---------------------------------

                    reports_ws.append_row([

                        report_title,

                        report_category,

                        report_date.strftime(
                            "%Y-%m-%d"
                        ),

                        pdf_link,

                        thumbnail_link,

                        "Active"

                    ])

                    st.success(
                        "Report Uploaded Successfully."
                    )

                    st.balloons()

                except Exception as e:

                    st.error(
                        f"Upload Failed: {e}"
                    )

st.divider()

# =====================================================
# END PART 4
# =====================================================
# =====================================================
# V5 PART 5
# CONTACT + NEWSLETTER + FOOTER
# =====================================================

# =====================================================
# NEWSLETTER
# =====================================================

if selected != "Admin Panel":

    st.markdown(
        "<div class='section-title'>📧 Newsletter</div>",
        unsafe_allow_html=True
    )

    newsletter_email = st.text_input(
        "Enter your email to receive research updates"
    )

    if st.button(
        "Subscribe To Newsletter"
    ):

        if newsletter_email:

            try:

                add_newsletter_email(
                    newsletter_email
                )

                st.success(
                    "Successfully subscribed."
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

        else:

            st.warning(
                "Please enter email."
            )

    st.divider()

# =====================================================
# CONTACT
# =====================================================

if selected == "Contact":

    st.markdown(
        "<div class='section-title'>📞 Contact</div>",
        unsafe_allow_html=True
    )

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.markdown(
            f"""
            <div class='custom-card'>

            📧 Email

            <br><br>

            {CONTACT_EMAIL}

            <br><br>

            {SUPPORT_EMAIL}

            </div>
            """,
            unsafe_allow_html=True
        )

    with info_col2:

        st.markdown(
            f"""
            <div class='custom-card'>

            📱 WhatsApp

            <br><br>

            +{WHATSAPP_NUMBER}

            <br><br>

            {PHONE_NUMBER}

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "### Send Inquiry"
    )

    lead_name = st.text_input(
        "Name"
    )

    lead_email = st.text_input(
        "Email"
    )

    lead_phone = st.text_input(
        "Phone"
    )

    lead_subject = st.text_input(
        "Subject"
    )

    lead_message = st.text_area(
        "Message"
    )

    if st.button(
        "Submit Inquiry"
    ):

        if (
            lead_name
            and lead_email
            and lead_message
        ):

            try:

                add_lead(
                    lead_name,
                    lead_email,
                    lead_phone,
                    lead_subject,
                    lead_message
                )

                st.success(
                    "Inquiry submitted successfully."
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

        else:

            st.warning(
                "Please complete required fields."
            )

    st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    f"""
    <center>

    <h4 style='color:#FFD54F;'>

    {COMPANY_NAME}

    </h4>

    <p style='color:white;'>

    {TAGLINE}

    </p>

    <p style='color:#B8C7E0;'>

    Equity Research |
    Sector Rotation |
    Relative Strength |
    Trading Technology |
    Strategy Development

    </p>

    <p style='color:#8EA9D6;'>

    📧 {CONTACT_EMAIL}

    <br>

    📱 +{WHATSAPP_NUMBER}

    <br>

    📍 {CONTACT_ADDRESS}

    </p>

    <p style='color:#8EA9D6;'>

    © 2026 {COMPANY_NAME}

    All Rights Reserved.

    </p>

    </center>
    """,
    unsafe_allow_html=True
)

# =====================================================
# FINAL NOTES
# =====================================================

"""
V5 COMPLETE

FEATURES INCLUDED:

✅ Editable Variables

✅ Professional Sidebar

✅ Mobile Responsive Design

✅ White Space Fix

✅ Dropdown Visibility Fix

✅ TradingView Ticker Tape

✅ TradingView Market Overview

✅ Google Drive Integration

✅ Google Sheets Integration

✅ Searchable Report Archive

✅ Category Filters

✅ Admin Upload Panel

✅ PDF Upload

✅ Thumbnail Upload

✅ Contact Leads Database

✅ Newsletter Database

✅ Floating WhatsApp Button

✅ Default Thumbnail Fallback

✅ Professional Footer

"""
