"""
Database models for GramaVoice
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Query(Base):
    """User query/interaction model"""

    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    query_text = Column(Text)
    query_audio_path = Column(String, nullable=True)
    language = Column(String)
    detected_intent = Column(String)
    service_category = Column(String)
    status = Column(String, default="pending")
    ai_response = Column(Text)
    confidence_score = Column(Float, default=0.0)
    resolution_time = Column(Integer, nullable=True)  # in hours
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved = Column(Boolean, default=False)


class Complaint(Base):
    """Complaint/Grievance model"""

    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    complaint_id = Column(String, unique=True, index=True)
    user_id = Column(String, index=True)
    category = Column(String)
    description = Column(Text)
    location = Column(String)
    severity = Column(String, default="medium")  # low, medium, high, critical
    status = Column(String, default="open")  # open, in_progress, resolved, closed
    assigned_to = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)


class User(Base):
    """User profile model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    name = Column(String)
    phone = Column(String)
    village = Column(String)
    district = Column(String)
    state = Column(String)
    preferred_language = Column(String, default="hi")
    created_at = Column(DateTime, default=datetime.utcnow)
    last_interaction = Column(DateTime, default=datetime.utcnow)


class Analytics(Base):
    """Analytics data model"""

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    total_queries = Column(Integer, default=0)
    total_complaints = Column(Integer, default=0)
    resolved_complaints = Column(Integer, default=0)
    avg_resolution_time = Column(Float, default=0.0)
    most_common_category = Column(String, nullable=True)
    user_satisfaction = Column(Float, default=0.0)
