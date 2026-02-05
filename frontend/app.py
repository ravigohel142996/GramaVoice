"""
GramaVoice Frontend - Streamlit Application
Professional UI for Voice-Powered Rural Service Gateway
"""
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.settings import (
    APP_NAME,
    API_HOST,
    API_PORT,
    SUPPORTED_LANGUAGES,
    SERVICE_CATEGORIES,
)

# Page configuration
st.set_page_config(
    page_title=f"{APP_NAME} - Empowering Rural Voices",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded",
)

# API Base URL
API_BASE_URL = f"http://{API_HOST}:{API_PORT}/api"

# Custom CSS for professional government-style UI
st.markdown(
    """
<style>
    /* Main theme colors - Government style */
    :root {
        --primary-color: #1e3a8a;
        --secondary-color: #fb923c;
        --success-color: #16a34a;
        --danger-color: #dc2626;
        --bg-light: #f8fafc;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Service card styling */
    .service-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .service-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .service-card h3 {
        color: #1e3a8a;
        margin-top: 0;
    }
    
    /* Stats card */
    .stats-card {
        background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stats-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    /* Response card */
    .response-card {
        background: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Microphone button */
    .mic-button {
        background: #dc2626;
        color: white;
        padding: 3rem;
        border-radius: 50%;
        font-size: 3rem;
        text-align: center;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(220, 38, 38, 0.3);
        transition: all 0.3s;
    }
    
    .mic-button:hover {
        background: #b91c1c;
        transform: scale(1.05);
    }
    
    /* Navigation tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: white;
        border-radius: 4px;
        padding: 0 2rem;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)


# Session state initialization
if "current_user" not in st.session_state:
    st.session_state.current_user = "demo_user_001"
if "query_history" not in st.session_state:
    st.session_state.query_history = []
if "last_response" not in st.session_state:
    st.session_state.last_response = None


# Header
st.markdown(
    """
<div class="main-header">
    <h1>🎤 GramaVoice</h1>
    <p>Empowering Rural Voices • AI for Bharat Initiative</p>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.markdown("### 🌐 Navigation")
    page = st.radio(
        "Select Page",
        ["Home", "Voice Demo", "Services", "Dashboard", "History", "About"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### 👤 User Profile")
    st.text(f"User ID: {st.session_state.current_user}")
    st.text("Location: रामपुर, वाराणसी")
    st.text("Language: हिन्दी")

    st.markdown("---")
    st.markdown("### 📞 Helpline")
    st.info("Call: **1800-GRAMA-HELP**")
    st.markdown("Available 24/7")


# Page routing
if page == "Home":
    # Landing page
    st.markdown("## Welcome to GramaVoice")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="service-card">
            <h3>🎙️ Voice First</h3>
            <p>Speak in your language. No typing required.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="service-card">
            <h3>🤖 AI Powered</h3>
            <p>Smart understanding of your needs.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="service-card">
            <h3>📱 Simple Access</h3>
            <p>Call anytime, anywhere.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Quick stats
    st.markdown("### 📊 Live Statistics")

    try:
        response = requests.post(
            f"{API_BASE_URL}/dashboard-data", json={"days": 30}, timeout=5
        )
        if response.status_code == 200:
            data = response.json()["data"]

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Queries", f"{data['total_queries']:,}")

            with col2:
                st.metric("Total Complaints", f"{data['total_complaints']:,}")

            with col3:
                st.metric("Resolved", f"{data['resolved_complaints']:,}")

            with col4:
                st.metric("Resolution Rate", f"{data['resolution_rate']:.1f}%")
    except:
        st.warning("Unable to load statistics. Please check if backend is running.")

    st.markdown("---")

    # How it works
    st.markdown("### 🔄 How It Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("#### 1️⃣ Call")
        st.write("Dial 1800-GRAMA-HELP")

    with col2:
        st.markdown("#### 2️⃣ Speak")
        st.write("Talk in your language")

    with col3:
        st.markdown("#### 3️⃣ AI Understands")
        st.write("Smart intent detection")

    with col4:
        st.markdown("#### 4️⃣ Get Answer")
        st.write("Voice response instantly")

elif page == "Voice Demo":
    # Voice interaction page
    st.markdown("## 🎤 Voice Interaction Demo")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Speak Your Query")

        # Language selector
        selected_language = st.selectbox(
            "Select Language",
            SUPPORTED_LANGUAGES,
            format_func=lambda x: f"{x['display']} ({x['name']})",
            key="voice_language",
        )

        # Text input (simulating voice in demo)
        st.info(
            "🎙️ **Demo Mode**: Type your query below (voice recognition will be enabled in production)"
        )
        query_text = st.text_area(
            "Enter your query",
            placeholder="Example: मेरी पेंशन कब आएगी?",
            height=100,
        )

        if st.button("🔊 Process Query", type="primary", use_container_width=True):
            if query_text:
                with st.spinner("Processing your query..."):
                    try:
                        response = requests.post(
                            f"{API_BASE_URL}/analyze",
                            json={
                                "text": query_text,
                                "language": selected_language["code"],
                                "user_id": st.session_state.current_user,
                            },
                            timeout=10,
                        )

                        if response.status_code == 200:
                            result = response.json()
                            st.session_state.last_response = result
                            st.success("✅ Query processed successfully!")
                        else:
                            st.error("Failed to process query")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        st.warning(
                            "Make sure the backend server is running: `python backend/app/main.py`"
                        )
            else:
                st.warning("Please enter a query")

    with col2:
        st.markdown("### Quick Actions")

        st.button("🎙️ Start Recording", use_container_width=True, disabled=True)
        st.button("⏹️ Stop Recording", use_container_width=True, disabled=True)
        st.button("🔄 Clear", use_container_width=True)

        st.markdown("---")
        st.markdown("#### Status")
        st.info("Ready to listen")

    # Display response
    if st.session_state.last_response:
        st.markdown("---")
        st.markdown("### 🤖 AI Response")

        result = st.session_state.last_response

        # Response card
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Detected Intent", result.get("detected_intent", "N/A"))

        with col2:
            st.metric("Service Category", result.get("service_category", "N/A"))

        with col3:
            confidence = result.get("confidence", 0)
            st.metric("Confidence", f"{confidence * 100:.1f}%")

        st.markdown("---")

        # AI Response
        st.markdown("#### 💬 Response")
        st.info(result.get("ai_response", "No response"))

        # Audio playback (simulated)
        st.markdown("#### 🔊 Audio Response")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

elif page == "Services":
    # Service access section
    st.markdown("## 📋 Government Services")

    st.markdown("### Available Services")

    # Display service cards
    cols = st.columns(3)

    for idx, service in enumerate(SERVICE_CATEGORIES):
        with cols[idx % 3]:
            st.markdown(
                f"""
            <div class="service-card">
                <h3>{service['icon']} {service['name']}</h3>
                <p>{service['description']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(f"Access {service['name']}", key=f"service_{service['id']}"):
                st.info(f"Accessing {service['name']} service...")

elif page == "Dashboard":
    # Analytics dashboard
    st.markdown("## 📊 Analytics Dashboard")

    st.markdown("### Admin View - Service Analytics")

    # Date filter
    col1, col2 = st.columns([3, 1])

    with col1:
        date_range = st.selectbox(
            "Select Time Range", ["Last 7 Days", "Last 30 Days", "Last 90 Days"]
        )

    days_map = {"Last 7 Days": 7, "Last 30 Days": 30, "Last 90 Days": 90}
    days = days_map[date_range]

    try:
        response = requests.post(
            f"{API_BASE_URL}/dashboard-data", json={"days": days}, timeout=5
        )

        if response.status_code == 200:
            data = response.json()["data"]

            # Key metrics
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(
                    f"""
                <div class="stats-card">
                    <p class="stats-number">{data['total_queries']}</p>
                    <p class="stats-label">Total Queries</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown(
                    f"""
                <div class="stats-card">
                    <p class="stats-number">{data['total_complaints']}</p>
                    <p class="stats-label">Total Complaints</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col3:
                st.markdown(
                    f"""
                <div class="stats-card">
                    <p class="stats-number">{data['resolved_complaints']}</p>
                    <p class="stats-label">Resolved</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col4:
                st.markdown(
                    f"""
                <div class="stats-card">
                    <p class="stats-number">{data['resolution_rate']:.1f}%</p>
                    <p class="stats-label">Resolution Rate</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            st.markdown("---")

            # Charts
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📈 Complaints by Category")

                if data["complaints_by_category"]:
                    df_complaints = pd.DataFrame(data["complaints_by_category"])
                    fig = px.pie(
                        df_complaints,
                        values="count",
                        names="category",
                        title="Distribution of Complaints",
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No complaint data available")

            with col2:
                st.markdown("### 📊 Queries by Service")

                if data["queries_by_service"]:
                    df_queries = pd.DataFrame(data["queries_by_service"])
                    fig = px.bar(
                        df_queries,
                        x="service",
                        y="count",
                        title="Service Usage",
                        color="count",
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No query data available")

            # Daily trend
            st.markdown("---")
            st.markdown("### 📅 Daily Query Trend")

            if data["daily_trend"]:
                df_trend = pd.DataFrame(data["daily_trend"])
                fig = px.line(
                    df_trend,
                    x="date",
                    y="count",
                    title="Queries Over Time",
                    markers=True,
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No trend data available")

        else:
            st.error("Failed to load dashboard data")
    except Exception as e:
        st.error(f"Error loading dashboard: {str(e)}")
        st.warning(
            "Make sure the backend server is running: `python backend/app/main.py`"
        )

elif page == "History":
    # User history page
    st.markdown("## 📜 Query History")

    st.markdown("### Your Recent Interactions")

    try:
        response = requests.post(
            f"{API_BASE_URL}/history",
            json={"user_id": st.session_state.current_user, "limit": 50},
            timeout=5,
        )

        if response.status_code == 200:
            history = response.json()["history"]

            if history:
                df = pd.DataFrame(history)
                st.dataframe(
                    df,
                    use_container_width=True,
                    column_config={
                        "id": "Query ID",
                        "query": "Query Text",
                        "date": "Date",
                        "service": "Service",
                        "status": "Status",
                        "resolution": "Resolution",
                    },
                )
            else:
                st.info("No query history available. Try the Voice Demo!")

                if st.button("Seed Demo Data"):
                    try:
                        seed_response = requests.post(
                            f"{API_BASE_URL}/seed-demo", timeout=5
                        )
                        if seed_response.status_code == 200:
                            st.success("Demo data created! Refresh the page.")
                        else:
                            st.error("Failed to seed data")
                    except:
                        st.error("Error seeding data")
        else:
            st.error("Failed to load history")
    except Exception as e:
        st.error(f"Error loading history: {str(e)}")
        st.warning(
            "Make sure the backend server is running: `python backend/app/main.py`"
        )

elif page == "About":
    # About page
    st.markdown("## ℹ️ About GramaVoice")

    st.markdown(
        """
    ### Voice-Powered Rural Service Gateway for India
    
    **GramaVoice** is an AI-powered platform that makes government services accessible to India's
    242 million non-literate citizens through voice interaction in their local languages.
    
    #### 🎯 Mission
    Making government services accessible to every Indian, regardless of literacy level.
    
    #### ✨ Key Features
    
    - **Multi-Language Support**: 15+ Indian languages including dialects
    - **Natural Conversation**: No menu navigation, just speak naturally
    - **Real-Time Information**: Connected to government databases
    - **Voice-Based Complaints**: File and track grievances by voice
    - **Instant Responses**: AI-powered understanding and responses
    - **24/7 Availability**: Call anytime, from anywhere
    
    #### 🛠️ Technology Stack
    
    - **Frontend**: Streamlit (Modern UI)
    - **Backend**: FastAPI (High-performance API)
    - **AI**: Amazon Bedrock, OpenAI Whisper
    - **Database**: PostgreSQL/SQLite
    - **Infrastructure**: AWS Cloud
    
    #### 📊 Impact
    
    - **1,124 users** in pilot phase
    - **81% complaint resolution rate**
    - **₹12.4 lakhs** in subsidies accessed
    - **4.2/5** user satisfaction score
    
    #### 👥 Target Users
    
    - Rural citizens with limited literacy
    - Elderly people who can't use apps
    - Farmers needing quick information
    - Women seeking government services
    
    #### 📞 Contact
    
    **Helpline**: 1800-GRAMA-HELP  
    **Available**: 24/7  
    **Support**: All major Indian languages
    
    #### 🔒 Privacy & Security
    
    - End-to-end encryption
    - Secure data storage
    - Compliance with IT Act 2000
    - No data sharing without consent
    
    ---
    
    **Built with ❤️ for Bharat**
    
    *Version 1.0.0*
    """
    )

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #64748b; padding: 2rem;">
    <p><strong>GramaVoice</strong> - Empowering Rural Voices | AI for Bharat Initiative</p>
    <p>Making government services accessible to 242 million non-literate Indians</p>
</div>
""",
    unsafe_allow_html=True,
)
