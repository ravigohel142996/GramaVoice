# GramaVoice - Technical Implementation Guide

## Project Structure

```
GramaVoice/
├── backend/
│   └── app/
│       ├── api/              # API endpoints
│       ├── models/           # Database models
│       │   ├── __init__.py   # DB initialization
│       │   └── database.py   # SQLAlchemy models
│       ├── services/         # Business logic
│       │   ├── ai_service.py # AI/ML services
│       │   └── data_service.py # Data operations
│       ├── utils/            # Utilities
│       └── main.py           # FastAPI application
├── frontend/
│   └── app.py                # Streamlit application
├── config/
│   └── settings.py           # Configuration
├── static/
│   ├── css/                  # Custom styles
│   ├── js/                   # JavaScript files
│   └── images/               # Images and icons
├── tests/
│   ├── backend/              # Backend tests
│   └── frontend/             # Frontend tests
├── logs/                     # Application logs
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
├── .gitignore               # Git ignore rules
├── start.sh                 # Linux/Mac startup script
├── start.bat                # Windows startup script
└── DEPLOYMENT.md            # Deployment guide
```

## Architecture Overview

### Backend (FastAPI)

**Components:**
1. **API Layer** (`backend/app/main.py`)
   - RESTful API endpoints
   - Request validation with Pydantic
   - CORS middleware
   - Error handling

2. **Database Layer** (`backend/app/models/`)
   - SQLAlchemy ORM models
   - Query, Complaint, User, Analytics tables
   - Session management
   - Database initialization

3. **AI Service** (`backend/app/services/ai_service.py`)
   - Speech-to-Text (Whisper simulation)
   - Intent Detection (NLU)
   - Response Generation (LLM)
   - Text-to-Speech (Polly simulation)

4. **Data Service** (`backend/app/services/data_service.py`)
   - CRUD operations
   - Analytics queries
   - Demo data seeding
   - History management

### Frontend (Streamlit)

**Pages:**
1. **Home** - Landing page with stats and overview
2. **Voice Demo** - Voice/text interaction interface
3. **Services** - Government service cards
4. **Dashboard** - Analytics with charts (Plotly)
5. **History** - User query history table
6. **About** - Information about the platform

**Features:**
- Responsive layout
- Government-style UI theme
- Real-time API integration
- Interactive charts and visualizations
- Multi-language support

## API Documentation

### Endpoints

#### Health Check
```http
GET /health
```
Returns: `{"status": "healthy", "timestamp": "..."}`

#### Voice Input
```http
POST /api/voice-input
Content-Type: multipart/form-data

{
  "audio_file": <file>,
  "language": "hi",
  "user_id": "demo_user"
}
```
Returns: Speech-to-text, intent, category, AI response, audio URL

#### Analyze Text
```http
POST /api/analyze
Content-Type: application/json

{
  "text": "मेरी पेंशन कब आएगी?",
  "language": "hi",
  "user_id": "demo_user"
}
```
Returns: Intent, category, confidence, AI response

#### Dashboard Data
```http
POST /api/dashboard-data
Content-Type: application/json

{
  "days": 7
}
```
Returns: Analytics data for specified period

#### User History
```http
POST /api/history
Content-Type: application/json

{
  "user_id": "demo_user",
  "limit": 50
}
```
Returns: User query history

#### Seed Demo Data
```http
POST /api/seed-demo
```
Returns: Success message

## Database Schema

### queries
- id (PK)
- user_id (FK)
- query_text
- query_audio_path
- language
- detected_intent
- service_category
- status
- ai_response
- confidence_score
- resolution_time
- created_at
- updated_at
- resolved

### complaints
- id (PK)
- complaint_id (unique)
- user_id (FK)
- category
- description
- location
- severity
- status
- assigned_to
- created_at
- updated_at
- resolved_at

### users
- id (PK)
- user_id (unique)
- name
- phone
- village
- district
- state
- preferred_language
- created_at
- last_interaction

### analytics
- id (PK)
- date
- total_queries
- total_complaints
- resolved_complaints
- avg_resolution_time
- most_common_category
- user_satisfaction

## Configuration

### Environment Variables

```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

# Database
DATABASE_URL=sqlite:///gramavoice.db

# AI Services
OPENAI_API_KEY=your-key
AWS_ACCESS_KEY=your-key
AWS_SECRET_KEY=your-key
AWS_REGION=us-east-1

# Application
DEMO_MODE=true
LOG_LEVEL=INFO
```

### Supported Languages

- Hindi (हिन्दी)
- English
- Gujarati (ગુજરાતી)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Malayalam (മലയാളം)
- Kannada (ಕನ್ನಡ)
- Marathi (मराठी)
- Bengali (বাংলা)
- Punjabi (ਪੰਜਾਬੀ)

### Service Categories

1. Pension Status (💰)
2. PM-Kisan (🌾)
3. Ration Card (🍚)
4. Health Camps (🏥)
5. Electricity (⚡)
6. Water Supply (💧)

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/ravigohel142996/GramaVoice.git
cd GramaVoice

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

### Running Backend

```bash
# Development mode (auto-reload)
python backend/app/main.py

# Production mode
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

### Running Frontend

```bash
# Development mode
streamlit run frontend/app.py

# Custom port
streamlit run frontend/app.py --server.port 8502
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=backend --cov=frontend

# Run specific test file
pytest tests/backend/test_api.py
```

## Demo Mode

By default, the application runs in **demo mode** which:

1. **Simulates AI Services**: No real API calls
2. **Uses Mock Data**: Pre-defined responses
3. **SQLite Database**: Local file-based DB
4. **Sample Queries**: Hindi/English examples

### Demo Responses

The AI service returns contextual responses based on keywords:
- "पेंशन" / "pension" → Pension status
- "राशन" / "ration" → Ration card info
- "बिजली" / "electricity" → Electricity complaint
- "किसान" / "kisan" → PM-Kisan info
- "पानी" / "water" → Water supply complaint
- "स्वास्थ्य" / "health" → Health camp info

## Production Deployment

### Prerequisites

1. Python 3.8+
2. PostgreSQL (for production DB)
3. OpenAI API key
4. AWS credentials
5. Domain name (optional)

### Steps

1. **Set Environment Variables**
```bash
DEMO_MODE=false
DATABASE_URL=postgresql://user:pass@host:5432/gramavoice
OPENAI_API_KEY=sk-...
AWS_ACCESS_KEY=AKIA...
AWS_SECRET_KEY=...
```

2. **Deploy Backend**
   - Option A: AWS Lambda + API Gateway
   - Option B: AWS ECS/Fargate
   - Option C: Heroku/Railway

3. **Deploy Frontend**
   - Option A: Streamlit Cloud
   - Option B: AWS EC2
   - Option C: Docker container

4. **Configure Database**
   - Use PostgreSQL RDS
   - Run migrations
   - Seed initial data

5. **Set Up Monitoring**
   - CloudWatch logs
   - Error tracking (Sentry)
   - Performance monitoring

## Security

### Best Practices

1. **API Security**
   - Use HTTPS in production
   - Implement rate limiting
   - Add authentication (OAuth2/JWT)
   - Validate all inputs

2. **Database Security**
   - Encrypt sensitive data
   - Use parameterized queries
   - Regular backups
   - Access control

3. **AI Service Security**
   - Secure API keys
   - Use environment variables
   - Implement request signing
   - Monitor usage

4. **Privacy**
   - Encrypt audio files
   - Anonymize personal data
   - GDPR compliance
   - Data retention policies

## Performance Optimization

### Backend

1. **Caching**
   - Redis for frequently accessed data
   - Cache AI responses
   - Static file caching

2. **Database**
   - Index frequently queried columns
   - Use connection pooling
   - Optimize queries
   - Implement pagination

3. **API**
   - Async endpoints
   - Response compression
   - Load balancing
   - CDN for static files

### Frontend

1. **Streamlit**
   - Cache data with @st.cache_data
   - Minimize API calls
   - Lazy load components
   - Optimize images

## Monitoring & Logging

### Logs

- Application logs: `logs/gramavoice.log`
- Access logs: Backend server logs
- Error logs: Separate error log file

### Metrics

- Total queries
- Response time
- Error rate
- User satisfaction
- Resolution rate

### Alerts

- High error rate
- Slow response time
- Database connection issues
- AI service failures

## Contributing

### Code Style

- Follow PEP 8 for Python
- Use type hints
- Write docstrings
- Add comments for complex logic

### Git Workflow

1. Create feature branch
2. Make changes
3. Write tests
4. Submit PR
5. Code review
6. Merge to main

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process
   lsof -i :8000
   # Kill process
   kill -9 <PID>
   ```

2. **Module not found**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

3. **Database locked**
   ```bash
   # Remove database file
   rm gramavoice.db
   # Restart application
   ```

4. **Frontend not connecting**
   - Check backend is running
   - Verify API_BASE_URL
   - Check CORS settings

## License

[To be determined based on project goals]

## Support

- GitHub Issues: Report bugs and feature requests
- Email: support@gramavoice.in
- Documentation: See all .md files in repository

---

**Built with ❤️ for Bharat 🇮🇳**
