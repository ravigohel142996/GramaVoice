# GramaVoice Configuration
import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
API_RELOAD = os.getenv("API_RELOAD", "true").lower() == "true"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/gramavoice.db")

# AI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "demo-key")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "demo-key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "demo-key")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Application Settings
APP_NAME = "GramaVoice"
APP_VERSION = "1.0.0"
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"

# Supported Languages
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

# Service Categories
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

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "gramavoice.log")
