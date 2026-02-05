# GramaVoice - Quick Start Guide

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ravigohel142996/GramaVoice.git
cd GramaVoice
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
cp .env.example .env
# Edit .env with your API keys (optional for demo mode)
```

## Running the Application

### Start Backend Server (Terminal 1)
```bash
python backend/app/main.py
```
The API will be available at: http://localhost:8000

### Start Frontend Application (Terminal 2)
```bash
streamlit run frontend/app.py
```
The web interface will open at: http://localhost:8501

## Testing the Application

### 1. Seed Demo Data
```bash
curl -X POST http://localhost:8000/api/seed-demo
```

### 2. Test Voice Analysis
```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "मेरी पेंशन कब आएगी?", "language": "hi", "user_id": "demo_user"}'
```

### 3. Access the UI
- Open http://localhost:8501 in your browser
- Navigate to "Voice Demo" page
- Enter a query in Hindi or English
- Click "Process Query"

## Features to Test

1. **Voice Demo**: Test text-to-intent conversion
2. **Services**: View available government services
3. **Dashboard**: See analytics and charts
4. **History**: View query history

## API Endpoints

- `GET /health` - Health check
- `POST /api/voice-input` - Process voice input
- `POST /api/analyze` - Analyze text query
- `POST /api/dashboard-data` - Get dashboard analytics
- `POST /api/history` - Get user history
- `POST /api/seed-demo` - Seed demo data

## Demo Mode

The application runs in demo mode by default with:
- Simulated AI responses
- Mock database
- Sample data

For production, set `DEMO_MODE=false` in `.env` and configure:
- OpenAI API key
- AWS credentials
- Production database

## Troubleshooting

### Backend not starting
```bash
# Check if port 8000 is available
lsof -i :8000

# Try different port
API_PORT=8001 python backend/app/main.py
```

### Frontend not connecting
- Ensure backend is running on port 8000
- Check API_BASE_URL in frontend/app.py
- Clear browser cache

### Database errors
```bash
# Remove existing database
rm gramavoice.db

# Restart backend (will recreate tables)
python backend/app/main.py
```

## Production Deployment

### Streamlit Cloud
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Set environment variables
4. Deploy

### AWS Deployment
1. Deploy backend on AWS Lambda/ECS
2. Configure RDS for database
3. Set up API Gateway
4. Deploy frontend on Streamlit Cloud or EC2

## Support

For issues and questions:
- GitHub Issues: [repository]/issues
- Email: support@gramavoice.in
- Phone: 1800-GRAMA-HELP

---

**Built for Bharat 🇮🇳**
