#!/bin/bash

# GramaVoice - Quick Start Script
# This script sets up and runs the GramaVoice application

set -e

echo "========================================="
echo "  GramaVoice - Setup & Launch Script"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Copy .env.example to .env if not exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created"
fi

# Create logs directory
mkdir -p logs

echo ""
echo "========================================="
echo "  Starting GramaVoice Application"
echo "========================================="
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down GramaVoice..."
    kill $BACKEND_PID 2>/dev/null || true
    kill $FRONTEND_PID 2>/dev/null || true
    echo "✅ Cleanup complete"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start backend
echo "🚀 Starting Backend API server..."
python backend/app/main.py &
BACKEND_PID=$!
echo "   Backend PID: $BACKEND_PID"
echo "   Backend URL: http://localhost:8000"

# Wait for backend to start
sleep 3

# Check if backend is running
if ! curl -s http://localhost:8000/health > /dev/null; then
    echo "❌ Backend failed to start"
    exit 1
fi
echo "✅ Backend is running"
echo ""

# Seed demo data
echo "🌱 Seeding demo data..."
curl -s -X POST http://localhost:8000/api/seed-demo > /dev/null
echo "✅ Demo data seeded"
echo ""

# Start frontend
echo "🚀 Starting Frontend application..."
streamlit run frontend/app.py &
FRONTEND_PID=$!
echo "   Frontend PID: $FRONTEND_PID"
echo "   Frontend URL: http://localhost:8501"
echo ""

echo "========================================="
echo "  ✅ GramaVoice is now running!"
echo "========================================="
echo ""
echo "📱 Access the application:"
echo "   Frontend: http://localhost:8501"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for processes
wait $BACKEND_PID $FRONTEND_PID
