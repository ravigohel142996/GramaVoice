"""
FastAPI application for GramaVoice backend
"""
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
import uvicorn
from loguru import logger

from config.settings import APP_NAME, APP_VERSION, API_HOST, API_PORT, API_RELOAD
from backend.app.models import init_db, get_db
from backend.app.services.ai_service import ai_service
from backend.app.services.data_service import data_service

# Configure logger
logger.add(
    "logs/gramavoice.log", rotation="500 MB", retention="10 days", level="INFO"
)

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Voice-Powered Rural Service Gateway for India",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response
class VoiceInputRequest(BaseModel):
    language: str = "hi"
    user_id: str = "demo_user"


class AnalyzeRequest(BaseModel):
    text: str
    language: str = "hi"
    user_id: str = "demo_user"


class HistoryRequest(BaseModel):
    user_id: str = "demo_user"
    limit: int = 50


class DashboardRequest(BaseModel):
    days: int = 7


# API Endpoints


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    logger.info(f"Starting {APP_NAME} v{APP_VERSION}")
    init_db()
    logger.info("Database initialized")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": f"Welcome to {APP_NAME}",
        "version": APP_VERSION,
        "status": "operational",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/api/voice-input")
async def voice_input(
    audio_file: UploadFile = File(...),
    language: str = "hi",
    user_id: str = "demo_user",
    db: Session = Depends(get_db),
):
    """
    Process voice input
    1. Convert speech to text
    2. Detect intent
    3. Generate response
    4. Store in database
    """
    try:
        logger.info(f"Receiving voice input from user {user_id} in language {language}")

        # Read audio data
        audio_data = await audio_file.read()

        # Convert speech to text
        stt_result = await ai_service.speech_to_text(audio_data, language)

        if stt_result.get("error"):
            raise HTTPException(status_code=400, detail="Speech recognition failed")

        query_text = stt_result["text"]
        stt_confidence = stt_result["confidence"]

        # Detect intent
        intent_result = await ai_service.detect_intent(query_text, language)
        intent = intent_result["intent"]
        category = intent_result["category"]
        intent_confidence = intent_result["confidence"]

        # Generate response
        response_result = await ai_service.generate_response(
            query_text, intent, category, language
        )
        ai_response = response_result["response"]

        # Generate audio response
        tts_result = await ai_service.text_to_speech(ai_response, language)

        # Store in database
        query = data_service.create_query(
            db=db,
            user_id=user_id,
            query_text=query_text,
            language=language,
            intent=intent,
            category=category,
            ai_response=ai_response,
            confidence=(stt_confidence + intent_confidence) / 2,
        )

        # If it's a complaint, create complaint record
        if intent == "complaint":
            complaint = data_service.create_complaint(
                db=db,
                user_id=user_id,
                category=category,
                description=query_text,
                location="Demo Location",
                severity="medium",
            )
            complaint_id = complaint.complaint_id
        else:
            complaint_id = None

        logger.info(f"Voice input processed successfully for user {user_id}")

        return {
            "success": True,
            "query_id": query.id,
            "query_text": query_text,
            "detected_intent": intent,
            "service_category": category,
            "ai_response": ai_response,
            "audio_response_url": tts_result.get("audio_url"),
            "confidence": query.confidence_score,
            "complaint_id": complaint_id,
        }

    except Exception as e:
        logger.error(f"Error processing voice input: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/analyze")
async def analyze_text(request: AnalyzeRequest, db: Session = Depends(get_db)):
    """
    Analyze text input (for testing without voice)
    """
    try:
        logger.info(
            f"Analyzing text from user {request.user_id} in language {request.language}"
        )

        # Detect intent
        intent_result = await ai_service.detect_intent(request.text, request.language)
        intent = intent_result["intent"]
        category = intent_result["category"]
        confidence = intent_result["confidence"]

        # Generate response
        response_result = await ai_service.generate_response(
            request.text, intent, category, request.language
        )
        ai_response = response_result["response"]

        # Store in database
        query = data_service.create_query(
            db=db,
            user_id=request.user_id,
            query_text=request.text,
            language=request.language,
            intent=intent,
            category=category,
            ai_response=ai_response,
            confidence=confidence,
        )

        logger.info(f"Text analysis completed for user {request.user_id}")

        return {
            "success": True,
            "query_id": query.id,
            "detected_intent": intent,
            "service_category": category,
            "confidence": confidence,
            "ai_response": ai_response,
        }

    except Exception as e:
        logger.error(f"Error analyzing text: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/dashboard-data")
async def dashboard_data(request: DashboardRequest, db: Session = Depends(get_db)):
    """
    Get analytics data for dashboard
    """
    try:
        logger.info(f"Fetching dashboard data for last {request.days} days")

        data = data_service.get_dashboard_data(db, request.days)

        return {"success": True, "data": data}

    except Exception as e:
        logger.error(f"Error getting dashboard data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/history")
async def get_history(request: HistoryRequest, db: Session = Depends(get_db)):
    """
    Get user query history
    """
    try:
        logger.info(f"Fetching history for user {request.user_id}")

        history = data_service.get_user_history(db, request.user_id, request.limit)

        return {"success": True, "history": history}

    except Exception as e:
        logger.error(f"Error getting history: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/seed-demo")
async def seed_demo_data(db: Session = Depends(get_db)):
    """
    Seed database with demo data (for testing)
    """
    try:
        logger.info("Seeding demo data")

        data_service.seed_demo_data(db)

        return {"success": True, "message": "Demo data seeded successfully"}

    except Exception as e:
        logger.error(f"Error seeding demo data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # Run the application
    uvicorn.run("main:app", host=API_HOST, port=API_PORT, reload=API_RELOAD)
