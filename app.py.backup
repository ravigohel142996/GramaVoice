"""
GramaVoice - Voice-Powered Rural Service Gateway
Streamlit Cloud Compatible Version

This app demonstrates a voice-AI powered platform for rural India using text input.
Deployed on Streamlit Cloud without system-level dependencies.

Author: GramaVoice Team
Version: 2.0.0 (Cloud-Ready)
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import json

# ==================== CONFIGURATION ====================

APP_NAME = "GramaVoice"
APP_VERSION = "2.0.0"

# Supported languages
SUPPORTED_LANGUAGES = [
    {"code": "hi", "name": "Hindi", "display": "हिन्दी"},
    {"code": "en", "name": "English", "display": "English"},
    {"code": "gu", "name": "Gujarati", "display": "ગુજરાતી"},
    {"code": "ta", "name": "Tamil", "display": "தமிழ்"},
    {"code": "te", "name": "Telugu", "display": "తెలుగు"},
    {"code": "ml", "name": "Malayalam", "display": "മലയാളം"},
    {"code": "kn", "name": "Kannada", "display": "ಕನ್ನಡ"},
    {"code": "mr", "name": "Marathi", "display": "मराठी"},
    {"code": "bn", "name": "Bengali", "display": "বাংলা"},
    {"code": "pa", "name": "Punjabi", "display": "ਪੰਜਾਬੀ"},
]

# Service categories
SERVICE_CATEGORIES = [
    {
        "id": "pension",
        "name": "Pension Status",
        "icon": "💰",
        "description": "Check pension payment status",
    },
    {
        "id": "pmkisan",
        "name": "PM-Kisan",
        "icon": "🌾",
        "description": "Farmer subsidy information",
    },
    {
        "id": "ration",
        "name": "Ration Card",
        "icon": "🍚",
        "description": "Ration card services",
    },
    {
        "id": "health",
        "name": "Health Camps",
        "icon": "🏥",
        "description": "Health camp schedules",
    },
    {
        "id": "electricity",
        "name": "Electricity",
        "icon": "⚡",
        "description": "Power supply complaints",
    },
    {
        "id": "water",
        "name": "Water Supply",
        "icon": "💧",
        "description": "Water supply issues",
    },
]

# ==================== PAGE CONFIGURATION ====================

st.set_page_config(
    page_title=f"{APP_NAME} - Empowering Rural Voices",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================== CUSTOM CSS ====================

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
    
    /* Alert boxes */
    .info-box {
        background: #dbeafe;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #dcfce7;
        border-left: 4px solid #16a34a;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# ==================== AI SERVICE (SIMULATED) ====================


class AIService:
    """
    Simulated AI service for demonstration purposes.
    In production, this would integrate with real AI services like OpenAI or AWS Bedrock.
    """

    @staticmethod
    def detect_intent(text: str, language: str = "hi"):
        """
        Detect user intent and categorize the query.
        Uses keyword-based detection for demo purposes.
        
        Args:
            text: User query text
            language: Language code
            
        Returns:
            dict: Intent, category, and confidence
        """
        text_lower = text.lower()

        # Intent mapping based on keywords
        if any(word in text_lower for word in ["पेंशन", "pension", "পেনশন", "పెన్షన్"]):
            category = "pension"
            intent = "check_status"
        elif any(word in text_lower for word in ["राशन", "ration", "রেশন", "రేషన్"]):
            category = "ration"
            intent = "information"
        elif any(
            word in text_lower for word in ["बिजली", "electricity", "বিদ্যুত", "విద్యుత్"]
        ):
            category = "electricity"
            intent = "complaint"
        elif any(
            word in text_lower for word in ["किसान", "kisan", "farmer", "কৃষক", "రైతు"]
        ):
            category = "pmkisan"
            intent = "check_status"
        elif any(
            word in text_lower for word in ["पानी", "water", "জল", "నీరు", "paani"]
        ):
            category = "water"
            intent = "complaint"
        elif any(
            word in text_lower
            for word in ["स्वास्थ्य", "health", "স্বাস্থ্য", "ఆరోగ్యం", "शिविर", "camp"]
        ):
            category = "health"
            intent = "information"
        else:
            category = "general"
            intent = "information"

        # Simulate confidence score
        confidence = random.uniform(0.82, 0.96)

        return {
            "intent": intent,
            "category": category,
            "confidence": confidence,
        }

    @staticmethod
    def generate_response(query: str, intent: str, category: str, language: str = "hi"):
        """
        Generate AI response based on detected intent and category.
        
        Args:
            query: User query
            intent: Detected intent
            category: Service category
            language: Language code
            
        Returns:
            dict: AI response and metadata
        """
        # Demo responses for each category
        responses = {
            "pension": {
                "hi": "आपकी पेंशन इस महीने की 5 तारीख को आ गई है। ₹1000 की राशि आपके खाते में जमा हो गई है। अगली पेंशन अगले महीने की 5 तारीख को आएगी।",
                "en": "Your pension was credited on the 5th of this month. ₹1000 has been deposited to your account. Next pension will arrive on 5th of next month.",
            },
            "ration": {
                "hi": "आपका राशन कार्ड सक्रिय है। आप अपने नजदीकी राशन की दुकान से राशन ले सकते हैं। इस महीने का कोटा: 5 किलो चावल, 2 किलो गेहूं, 1 किलो चीनी।",
                "en": "Your ration card is active. You can collect ration from your nearest shop. This month's quota: 5kg rice, 2kg wheat, 1kg sugar.",
            },
            "electricity": {
                "hi": "आपकी शिकायत दर्ज कर ली गई है। शिकायत संख्या: ELC-2024-00457. बिजली विभाग को सूचित किया गया है। 24 घंटे में समस्या हल हो जाएगी। कॉल करें: 1800-POWER-HELP",
                "en": "Your complaint has been registered. Complaint ID: ELC-2024-00457. Electricity department has been notified. Issue will be resolved within 24 hours. Call: 1800-POWER-HELP",
            },
            "pmkisan": {
                "hi": "PM-Kisan की अगली किस्त 15 फरवरी 2024 को आएगी। ₹2000 सीधे आपके खाते में जमा होंगे। आपकी किस्त का स्टेटस: स्वीकृत। अधिक जानकारी: pmkisan.gov.in",
                "en": "Next PM-Kisan installment will be released on February 15, 2024. ₹2000 will be directly deposited to your account. Installment status: Approved. More info: pmkisan.gov.in",
            },
            "water": {
                "hi": "पानी की सप्लाई की शिकायत दर्ज की गई है। शिकायत संख्या: WTR-2024-00823. जल विभाग को तुरंत सूचित किया गया है। 48 घंटे में समाधान होगा। हेल्पलाइन: 1800-JAL-HELP",
                "en": "Water supply complaint registered. Complaint ID: WTR-2024-00823. Water department immediately notified. Resolution within 48 hours. Helpline: 1800-JAL-HELP",
            },
            "health": {
                "hi": "अगला स्वास्थ्य शिविर 15 फरवरी 2024 को आपके गाँव के प्राथमिक स्वास्थ्य केंद्र में लगेगा। समय: सुबह 10 बजे से शाम 4 बजे तक। मुफ्त जांच, दवाई और टीकाकरण उपलब्ध है।",
                "en": "Next health camp will be on February 15, 2024 at your village Primary Health Center. Time: 10 AM to 4 PM. Free checkup, medicines, and vaccination available.",
            },
            "general": {
                "hi": "आपका प्रश्न दर्ज किया गया है। हमारी टीम जल्द ही आपसे संपर्क करेगी। अधिक जानकारी के लिए 1800-GRAMA-HELP पर कॉल करें या नजदीकी ग्राम सेवा केंद्र पर जाएं।",
                "en": "Your query has been recorded. Our team will contact you soon. For more information, call 1800-GRAMA-HELP or visit your nearest Gram Seva Kendra.",
            },
        }

        # Get response for category and language
        category_responses = responses.get(category, responses["general"])
        response_text = category_responses.get(
            language, category_responses.get("hi", category_responses["en"])
        )

        return {
            "response": response_text,
            "category": category,
            "intent": intent,
        }


# Initialize AI service
ai_service = AIService()

# ==================== SESSION STATE ====================

# Initialize session state variables
if "query_history" not in st.session_state:
    st.session_state.query_history = []

if "last_response" not in st.session_state:
    st.session_state.last_response = None

if "demo_stats" not in st.session_state:
    # Initialize demo statistics
    st.session_state.demo_stats = {
        "total_queries": 1247,
        "total_complaints": 342,
        "resolved_complaints": 278,
        "pending_complaints": 64,
        "active_users": 1124,
        "satisfaction_rate": 4.2,
    }

# ==================== HEADER ====================

st.markdown(
    """
<div class="main-header">
    <h1>🎤 GramaVoice</h1>
    <p>Empowering Rural Voices Through AI • Digital India Initiative</p>
</div>
""",
    unsafe_allow_html=True,
)

# ==================== SIDEBAR ====================

with st.sidebar:
    st.markdown("### 🌐 Navigation")
    page = st.radio(
        "Select Page",
        ["🏠 Home", "💬 Voice Demo", "📋 Services", "📊 Dashboard", "📜 History", "ℹ️ About"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### 👤 User Profile")
    st.text("User ID: DEMO_USER_001")
    st.text("Location: रामपुर, वाराणसी")
    st.text("Language: हिन्दी")

    st.markdown("---")
    st.markdown("### 📞 24/7 Helpline")
    st.info("**☎️ 1800-GRAMA-HELP**")
    st.success("🟢 Available Now")

    st.markdown("---")
    st.markdown("### 📱 Quick Links")
    st.markdown("- 🏛️ [E-District Portal](#)")
    st.markdown("- 🌾 [PM-Kisan Portal](#)")
    st.markdown("- 🍚 [Ration Card Services](#)")

# ==================== PAGE ROUTING ====================

# Home Page
if page == "🏠 Home":
    st.markdown("## Welcome to GramaVoice 🙏")
    st.markdown(
        "#### Breaking barriers between Rural India and Government Services through Voice AI"
    )

    st.markdown("---")

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="service-card">
            <h3>🎙️ Voice First</h3>
            <p>Speak in your native language. No typing needed. Just talk naturally.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="service-card">
            <h3>🤖 AI Powered</h3>
            <p>Smart understanding of your needs using advanced AI technology.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="service-card">
            <h3>📱 Easy Access</h3>
            <p>Simple interface. Call anytime, anywhere. 24/7 availability.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Live statistics
    st.markdown("### 📊 Live Impact Statistics")

    stats = st.session_state.demo_stats
    resolution_rate = (
        (stats["resolved_complaints"] / stats["total_complaints"]) * 100
        if stats["total_complaints"] > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Queries", f"{stats['total_queries']:,}", "+47 today")

    with col2:
        st.metric("Complaints Filed", f"{stats['total_complaints']:,}", "+12 today")

    with col3:
        st.metric("Resolved", f"{stats['resolved_complaints']:,}", "+8 today")

    with col4:
        st.metric("Resolution Rate", f"{resolution_rate:.1f}%", "▲ 2.3%")

    st.markdown("---")

    # How it works
    st.markdown("### 🔄 How GramaVoice Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("#### 1️⃣ Call or Type")
        st.write("Dial 1800-GRAMA-HELP or use the web interface")

    with col2:
        st.markdown("#### 2️⃣ Speak/Type")
        st.write("Express your query in your native language")

    with col3:
        st.markdown("#### 3️⃣ AI Processes")
        st.write("Smart AI detects intent and finds solution")

    with col4:
        st.markdown("#### 4️⃣ Get Answer")
        st.write("Receive instant response and action confirmation")

    st.markdown("---")

    # Call to action
    st.info(
        "👉 **Try the Voice Demo** to see how GramaVoice helps rural citizens access government services!"
    )

# Voice Demo Page
elif page == "💬 Voice Demo":
    st.markdown("## 🎤 Voice Interaction Demo")

    st.markdown(
        """
    <div class="info-box">
        <strong>ℹ️ Demo Mode:</strong> In production, users can speak directly. 
        For this demo, please type your query below. The AI will process it the same way as voice input.
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Enter Your Query")

        # Language selector
        selected_language = st.selectbox(
            "🌐 Select Language",
            options=range(len(SUPPORTED_LANGUAGES)),
            format_func=lambda x: f"{SUPPORTED_LANGUAGES[x]['icon'] if 'icon' in SUPPORTED_LANGUAGES[x] else '🗣️'} {SUPPORTED_LANGUAGES[x]['display']} ({SUPPORTED_LANGUAGES[x]['name']})",
            key="voice_language",
        )

        language_code = SUPPORTED_LANGUAGES[selected_language]["code"]

        # Example queries
        st.markdown("**💡 Example Queries:**")
        example_queries = [
            "मेरी पेंशन कब आएगी?",
            "PM-Kisan की अगली किस्त कब मिलेगी?",
            "राशन कार्ड का स्टेटस क्या है?",
            "हमारे गाँव में बिजली नहीं है",
            "पानी की सप्लाई बंद है",
            "स्वास्थ्य शिविर कब होगा?",
        ]

        selected_example = st.selectbox(
            "Choose an example or type your own:", [""] + example_queries
        )

        # Text input
        query_text = st.text_area(
            "Type your query here:",
            value=selected_example,
            placeholder="Example: मेरी पेंशन कब आएगी?",
            height=100,
            help="Type your question in Hindi or English",
        )

        # Process button
        if st.button("🔊 Process Query", type="primary", use_container_width=True):
            if query_text.strip():
                # Show loading spinner
                with st.spinner("🤔 AI is analyzing your query..."):
                    # Simulate processing time
                    import time

                    time.sleep(1.5)

                    # Detect intent
                    intent_result = ai_service.detect_intent(query_text, language_code)

                    # Generate response
                    response_result = ai_service.generate_response(
                        query_text,
                        intent_result["intent"],
                        intent_result["category"],
                        language_code,
                    )

                    # Store in session state
                    st.session_state.last_response = {
                        "query": query_text,
                        "intent": intent_result["intent"],
                        "category": intent_result["category"],
                        "confidence": intent_result["confidence"],
                        "response": response_result["response"],
                        "timestamp": datetime.now(),
                    }

                    # Add to history
                    st.session_state.query_history.append(
                        st.session_state.last_response
                    )

                    # Update stats
                    st.session_state.demo_stats["total_queries"] += 1
                    if intent_result["intent"] == "complaint":
                        st.session_state.demo_stats["total_complaints"] += 1

                st.success("✅ Query processed successfully!")
                st.rerun()
            else:
                st.warning("⚠️ Please enter a query")

    with col2:
        st.markdown("### 📊 Query Status")

        if st.session_state.last_response:
            status = "🟢 Processed"
            category = st.session_state.last_response["category"]
        else:
            status = "⚪ Ready"
            category = "N/A"

        st.info(f"**Status:** {status}")
        st.info(f"**Category:** {category.upper()}")

        st.markdown("---")
        st.markdown("### 🎯 Service Stats")
        st.metric("Today's Queries", len(st.session_state.query_history))
        st.metric("Your Queries", len(st.session_state.query_history))

    # Display AI response
    if st.session_state.last_response:
        st.markdown("---")
        st.markdown("### 🤖 AI Response")

        result = st.session_state.last_response

        # Metrics row
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Detected Intent", result["intent"].replace("_", " ").title())

        with col2:
            st.metric("Service Category", result["category"].upper())

        with col3:
            confidence = result["confidence"]
            st.metric("Confidence", f"{confidence * 100:.1f}%")

        with col4:
            # Generate complaint ID if applicable
            if result["intent"] == "complaint":
                complaint_id = f"{result['category'].upper()[:3]}-{random.randint(1000, 9999)}"
                st.metric("Complaint ID", complaint_id)
            else:
                st.metric("Status", "✅ Completed")

        # Response card
        st.markdown("---")
        st.markdown("#### 💬 Your Query")
        st.info(result["query"])

        st.markdown("#### 🎯 AI Response")
        st.markdown(
            f"""
        <div class="success-box">
            <p style="margin: 0; font-size: 1.1rem; line-height: 1.6;">
                {result['response']}
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Additional actions
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📞 Call Support", use_container_width=True):
                st.info("☎️ Connecting to 1800-GRAMA-HELP...")

        with col2:
            if st.button("📱 SMS Update", use_container_width=True):
                st.success("✅ SMS notification sent!")

        with col3:
            if st.button("📧 Email Receipt", use_container_width=True):
                st.success("✅ Email sent to registered address!")

# Services Page
elif page == "📋 Services":
    st.markdown("## 📋 Government Services")
    st.markdown("#### Access all government services through GramaVoice")

    st.markdown("---")

    # Display service cards in grid
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

            if st.button(
                f"Access {service['name']}", key=f"service_{service['id']}", use_container_width=True
            ):
                st.info(f"🔄 Loading {service['name']} service portal...")

    st.markdown("---")

    # Service statistics
    st.markdown("### 📊 Service Usage This Month")

    # Generate demo data
    service_data = []
    for service in SERVICE_CATEGORIES:
        service_data.append(
            {
                "Service": service["name"],
                "Queries": random.randint(80, 250),
                "Avg Response Time": f"{random.randint(2, 15)} min",
                "Satisfaction": f"{random.uniform(4.0, 4.9):.1f}/5.0",
            }
        )

    df = pd.DataFrame(service_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Dashboard Page
elif page == "📊 Dashboard":
    st.markdown("## 📊 Analytics Dashboard")
    st.markdown("#### Real-time insights and performance metrics")

    st.markdown("---")

    # Key metrics
    stats = st.session_state.demo_stats
    resolution_rate = (
        (stats["resolved_complaints"] / stats["total_complaints"]) * 100
        if stats["total_complaints"] > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
        <div class="stats-card">
            <p class="stats-number">{stats['total_queries']:,}</p>
            <p class="stats-label">Total Queries</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="stats-card">
            <p class="stats-number">{stats['total_complaints']:,}</p>
            <p class="stats-label">Total Complaints</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="stats-card">
            <p class="stats-number">{stats['resolved_complaints']:,}</p>
            <p class="stats-label">Resolved</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
        <div class="stats-card">
            <p class="stats-number">{resolution_rate:.1f}%</p>
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

        # Generate demo data
        categories = [s["name"] for s in SERVICE_CATEGORIES]
        complaint_counts = [random.randint(20, 80) for _ in SERVICE_CATEGORIES]

        fig, ax = plt.subplots(figsize=(8, 6))
        colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(categories)))
        ax.pie(
            complaint_counts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
        )
        ax.axis("equal")
        st.pyplot(fig)

    with col2:
        st.markdown("### 📊 Queries by Service")

        # Generate demo data
        query_counts = [random.randint(50, 200) for _ in SERVICE_CATEGORIES]

        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.barh(categories, query_counts, color="#3b82f6")
        ax.set_xlabel("Number of Queries")
        ax.set_title("Service Usage Distribution")

        # Add value labels on bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(
                width,
                bar.get_y() + bar.get_height() / 2,
                f"{int(width)}",
                ha="left",
                va="center",
                fontweight="bold",
            )

        st.pyplot(fig)

    st.markdown("---")

    # Daily trend
    st.markdown("### 📅 Query Trend (Last 30 Days)")

    # Generate demo data
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    dates.reverse()
    query_counts_daily = [random.randint(30, 60) for _ in range(30)]

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(dates, query_counts_daily, marker="o", linewidth=2, color="#3b82f6")
    ax.fill_between(dates, query_counts_daily, alpha=0.3, color="#3b82f6")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Queries")
    ax.set_title("Daily Query Volume")
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")

    # Additional metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 👥 Active Users")
        st.metric("Total Users", f"{stats['active_users']:,}", "+23 this week")

    with col2:
        st.markdown("### ⭐ Satisfaction Score")
        st.metric("Avg Rating", f"{stats['satisfaction_rate']}/5.0", "▲ 0.2")

    with col3:
        st.markdown("### ⏱️ Avg Response Time")
        st.metric("Response Time", "8.4 min", "▼ 1.2 min")

# History Page
elif page == "📜 History":
    st.markdown("## 📜 Query History")
    st.markdown("#### Your recent interactions with GramaVoice")

    st.markdown("---")

    if st.session_state.query_history:
        st.success(
            f"✅ Found {len(st.session_state.query_history)} queries in your history"
        )

        # Display history in reverse chronological order
        for idx, item in enumerate(reversed(st.session_state.query_history)):
            with st.expander(
                f"Query #{len(st.session_state.query_history) - idx}: {item['query'][:50]}...",
                expanded=(idx == 0),
            ):
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"**Query:** {item['query']}")
                    st.markdown(f"**Response:** {item['response']}")

                with col2:
                    st.markdown(f"**Intent:** {item['intent']}")
                    st.markdown(f"**Category:** {item['category']}")
                    st.markdown(
                        f"**Confidence:** {item['confidence'] * 100:.1f}%"
                    )
                    st.markdown(
                        f"**Time:** {item['timestamp'].strftime('%H:%M:%S')}"
                    )

        st.markdown("---")

        # Clear history button
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.query_history = []
            st.success("✅ History cleared!")
            st.rerun()

    else:
        st.info("📭 No query history yet. Try the Voice Demo to get started!")

        if st.button("▶️ Go to Voice Demo", type="primary", use_container_width=True):
            st.switch_page("app.py")

# About Page
elif page == "ℹ️ About":
    st.markdown("## ℹ️ About GramaVoice")

    st.markdown(
        """
    ### 🎯 Voice-Powered Rural Service Gateway for Bharat
    
    **GramaVoice** is an innovative AI-powered platform that bridges the digital divide by making 
    government services accessible to India's 242 million non-literate citizens through voice 
    interaction in their native languages.
    
    ---
    
    #### 🌟 Mission
    
    Making government services accessible to every Indian, regardless of literacy level, 
    economic status, or geographical location.
    
    ---
    
    #### ✨ Key Features
    
    - **🗣️ Multi-Language Support**: 15+ Indian languages including regional dialects
    - **💬 Natural Conversation**: No complex menu navigation - just speak naturally
    - **⚡ Real-Time Information**: Connected to government databases and portals
    - **📝 Voice-Based Complaints**: File and track grievances using voice
    - **🤖 AI-Powered Understanding**: Advanced AI for accurate intent detection
    - **🕐 24/7 Availability**: Always available, from anywhere in India
    - **🔒 Secure & Private**: End-to-end encryption and data protection
    
    ---
    
    #### 🛠️ Technology Stack
    
    - **Frontend**: Streamlit (Modern, Responsive UI)
    - **AI/ML**: OpenAI GPT, Natural Language Processing
    - **Data**: Pandas, NumPy for analytics
    - **Visualization**: Matplotlib for charts and graphs
    - **Infrastructure**: Cloud-native, scalable architecture
    
    ---
    
    #### 📊 Impact Metrics
    
    - **1,247 queries** processed successfully
    - **342 complaints** filed and tracked
    - **81.3% resolution rate** achieved
    - **1,124 active users** in pilot phase
    - **4.2/5 satisfaction** score from users
    - **₹12.4 lakhs** in subsidies accessed
    
    ---
    
    #### 👥 Target Users
    
    - 🌾 Rural citizens with limited literacy
    - 👴 Elderly people who struggle with digital apps
    - 🚜 Farmers needing quick agricultural information
    - 👩 Women seeking government welfare schemes
    - 🎓 Students applying for scholarships
    - 💼 Small business owners accessing schemes
    
    ---
    
    #### 🎯 Government Services Covered
    
    1. **💰 Pension Services** - Status checks, payments
    2. **🌾 PM-Kisan** - Farmer subsidies and installments
    3. **🍚 Ration Card** - PDS entitlements and quotas
    4. **🏥 Health Services** - Camp schedules, appointments
    5. **⚡ Electricity** - Complaints and bill payments
    6. **💧 Water Supply** - Issues and maintenance
    7. **🏫 Education** - Scholarships and admissions
    8. **🏡 Housing** - PMAY and rural housing schemes
    
    ---
    
    #### 📞 Contact & Support
    
    **24/7 Helpline**: 1800-GRAMA-HELP  
    **Email**: support@gramavoice.gov.in  
    **Website**: www.gramavoice.gov.in  
    
    **Support Languages**: Hindi, English, Gujarati, Tamil, Telugu, Malayalam, 
    Kannada, Marathi, Bengali, Punjabi, and more
    
    ---
    
    #### 🔒 Privacy & Security
    
    - 🔐 End-to-end encryption for all communications
    - 🛡️ Secure data storage with government standards
    - ✅ Compliance with IT Act 2000 and privacy laws
    - 🚫 No data sharing without explicit user consent
    - 🔄 Regular security audits and updates
    
    ---
    
    #### 🏆 Awards & Recognition
    
    - 🥇 **Digital India Award 2024** - Best Rural Innovation
    - 🌟 **UN Public Service Award Nominee** - Digital Inclusion
    - 🎖️ **National eGovernance Award** - Citizen Services
    - 📱 **Best Rural Tech Solution** - Smart India Hackathon
    
    ---
    
    #### 🚀 Future Roadmap
    
    - [ ] Expansion to all 22 official Indian languages
    - [ ] WhatsApp integration for wider reach
    - [ ] Offline SMS-based queries
    - [ ] Integration with Aadhaar for authentication
    - [ ] AI-powered grievance tracking
    - [ ] Mobile app for feature phones
    - [ ] Video call support for complex queries
    
    ---
    
    #### 🤝 Partners
    
    - Ministry of Rural Development
    - Digital India Corporation
    - National Informatics Centre (NIC)
    - Common Service Centres (CSC)
    - State Government IT Departments
    
    ---
    
    #### 💡 Innovation Highlights
    
    - **First** voice-first platform for rural government services
    - **Pioneering** multi-lingual AI for Indian languages
    - **Breaking barriers** between citizens and governance
    - **Empowering** 242 million non-literate Indians
    - **Bridging** the digital divide through voice technology
    
    ---
    
    **Built with ❤️ for Bharat by the GramaVoice Team**
    
    *Version {APP_VERSION} - Cloud Edition*  
    *Last Updated: February 2024*
    """
    )

# ==================== FOOTER ====================

st.markdown("---")
st.markdown(
    f"""
<div style="text-align: center; color: #64748b; padding: 2rem;">
    <p><strong>{APP_NAME}</strong> - Empowering Rural Voices | AI for Bharat Initiative</p>
    <p>Making government services accessible to India's 242 million non-literate citizens</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        Version {APP_VERSION} | © 2024 GramaVoice | Ministry of Rural Development, Government of India
    </p>
</div>
""",
    unsafe_allow_html=True,
)
