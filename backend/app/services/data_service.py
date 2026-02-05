"""
Data service for managing queries, complaints, and analytics
"""
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from backend.app.models.database import Query, Complaint, User, Analytics
from loguru import logger
import random


class DataService:
    """Service for database operations"""

    @staticmethod
    def create_query(
        db: Session,
        user_id: str,
        query_text: str,
        language: str,
        intent: str,
        category: str,
        ai_response: str,
        confidence: float = 0.0,
    ) -> Query:
        """Create a new query record"""
        try:
            query = Query(
                user_id=user_id,
                query_text=query_text,
                language=language,
                detected_intent=intent,
                service_category=category,
                ai_response=ai_response,
                confidence_score=confidence,
                status="completed",
            )
            db.add(query)
            db.commit()
            db.refresh(query)
            logger.info(f"Created query {query.id} for user {user_id}")
            return query
        except Exception as e:
            logger.error(f"Error creating query: {e}")
            db.rollback()
            raise

    @staticmethod
    def create_complaint(
        db: Session,
        user_id: str,
        category: str,
        description: str,
        location: str,
        severity: str = "medium",
    ) -> Complaint:
        """Create a new complaint"""
        try:
            # Generate complaint ID
            complaint_id = f"{category[:3].upper()}-{datetime.now().year}-{random.randint(1000, 9999)}"

            complaint = Complaint(
                complaint_id=complaint_id,
                user_id=user_id,
                category=category,
                description=description,
                location=location,
                severity=severity,
                status="open",
            )
            db.add(complaint)
            db.commit()
            db.refresh(complaint)
            logger.info(f"Created complaint {complaint_id} for user {user_id}")
            return complaint
        except Exception as e:
            logger.error(f"Error creating complaint: {e}")
            db.rollback()
            raise

    @staticmethod
    def get_user_history(
        db: Session, user_id: str, limit: int = 50
    ) -> List[Dict[str, Any]]:
        """Get user query history"""
        try:
            queries = (
                db.query(Query)
                .filter(Query.user_id == user_id)
                .order_by(desc(Query.created_at))
                .limit(limit)
                .all()
            )

            return [
                {
                    "id": q.id,
                    "query": q.query_text,
                    "date": q.created_at.strftime("%Y-%m-%d %H:%M"),
                    "service": q.service_category,
                    "status": q.status,
                    "resolution": "Resolved" if q.resolved else "Pending",
                }
                for q in queries
            ]
        except Exception as e:
            logger.error(f"Error getting user history: {e}")
            return []

    @staticmethod
    def get_dashboard_data(db: Session, days: int = 7) -> Dict[str, Any]:
        """Get analytics data for dashboard"""
        try:
            start_date = datetime.now() - timedelta(days=days)

            # Get total queries
            total_queries = (
                db.query(func.count(Query.id))
                .filter(Query.created_at >= start_date)
                .scalar()
            )

            # Get total complaints
            total_complaints = (
                db.query(func.count(Complaint.id))
                .filter(Complaint.created_at >= start_date)
                .scalar()
            )

            # Get resolved complaints
            resolved_complaints = (
                db.query(func.count(Complaint.id))
                .filter(
                    Complaint.created_at >= start_date, Complaint.status == "resolved"
                )
                .scalar()
            )

            # Get complaints by category
            complaints_by_category = (
                db.query(Complaint.category, func.count(Complaint.id))
                .filter(Complaint.created_at >= start_date)
                .group_by(Complaint.category)
                .all()
            )

            # Get queries by service
            queries_by_service = (
                db.query(Query.service_category, func.count(Query.id))
                .filter(Query.created_at >= start_date)
                .group_by(Query.service_category)
                .all()
            )

            # Get daily query trend
            daily_queries = (
                db.query(
                    func.date(Query.created_at).label("date"),
                    func.count(Query.id).label("count"),
                )
                .filter(Query.created_at >= start_date)
                .group_by(func.date(Query.created_at))
                .all()
            )

            # Calculate resolution rate
            resolution_rate = (
                (resolved_complaints / total_complaints * 100)
                if total_complaints > 0
                else 0
            )

            return {
                "total_queries": total_queries or 0,
                "total_complaints": total_complaints or 0,
                "resolved_complaints": resolved_complaints or 0,
                "resolution_rate": round(resolution_rate, 2),
                "complaints_by_category": [
                    {"category": cat, "count": count}
                    for cat, count in complaints_by_category
                ],
                "queries_by_service": [
                    {"service": svc, "count": count}
                    for svc, count in queries_by_service
                ],
                "daily_trend": [
                    {"date": str(date), "count": count} for date, count in daily_queries
                ],
            }
        except Exception as e:
            logger.error(f"Error getting dashboard data: {e}")
            return {
                "total_queries": 0,
                "total_complaints": 0,
                "resolved_complaints": 0,
                "resolution_rate": 0,
                "complaints_by_category": [],
                "queries_by_service": [],
                "daily_trend": [],
            }

    @staticmethod
    def seed_demo_data(db: Session):
        """Seed database with demo data for testing"""
        try:
            # Check if data already exists
            if db.query(Query).count() > 0:
                logger.info("Demo data already exists")
                return

            logger.info("Seeding demo data...")

            # Create demo user
            demo_user = User(
                user_id="demo_user_001",
                name="राज कुमार",
                phone="+91-9876543210",
                village="रामपुर",
                district="वाराणसी",
                state="उत्तर प्रदेश",
                preferred_language="hi",
            )
            db.add(demo_user)

            # Create demo queries
            demo_queries = [
                {
                    "user_id": "demo_user_001",
                    "query_text": "मेरी पेंशन कब आएगी?",
                    "language": "hi",
                    "detected_intent": "check_status",
                    "service_category": "pension",
                    "ai_response": "आपकी पेंशन इस महीने की 5 तारीख को आ गई है।",
                    "confidence_score": 0.92,
                    "status": "completed",
                    "resolved": True,
                },
                {
                    "user_id": "demo_user_001",
                    "query_text": "राशन कार्ड की जानकारी चाहिए",
                    "language": "hi",
                    "detected_intent": "information",
                    "service_category": "ration",
                    "ai_response": "आपका राशन कार्ड सक्रिय है।",
                    "confidence_score": 0.89,
                    "status": "completed",
                    "resolved": True,
                },
                {
                    "user_id": "demo_user_001",
                    "query_text": "हमारे गाँव में बिजली नहीं है",
                    "language": "hi",
                    "detected_intent": "complaint",
                    "service_category": "electricity",
                    "ai_response": "आपकी शिकायत दर्ज कर ली गई है।",
                    "confidence_score": 0.95,
                    "status": "completed",
                    "resolved": False,
                },
            ]

            for q_data in demo_queries:
                query = Query(**q_data)
                db.add(query)

            # Create demo complaints
            demo_complaints = [
                {
                    "complaint_id": "ELC-2024-001",
                    "user_id": "demo_user_001",
                    "category": "electricity",
                    "description": "गाँव में 2 दिन से बिजली नहीं है",
                    "location": "रामपुर, वाराणसी",
                    "severity": "high",
                    "status": "in_progress",
                },
                {
                    "complaint_id": "WTR-2024-002",
                    "user_id": "demo_user_001",
                    "category": "water",
                    "description": "पानी की सप्लाई बंद है",
                    "location": "रामपुर, वाराणसी",
                    "severity": "medium",
                    "status": "open",
                },
            ]

            for c_data in demo_complaints:
                complaint = Complaint(**c_data)
                db.add(complaint)

            db.commit()
            logger.info("Demo data seeded successfully")

        except Exception as e:
            logger.error(f"Error seeding demo data: {e}")
            db.rollback()


# Singleton instance
data_service = DataService()
