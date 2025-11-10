# SEO Agent MVP - Setup Guide

Complete setup instructions for the 100% FREE SEO Agent MVP.

## 📋 Prerequisites

Before starting, ensure you have:

- **Python 3.11+** installed
- **Git** installed
- **Google Gemini API key** (FREE - instructions below)
- **Text editor** (VS Code recommended)

## 🔑 Step 1: Get Google Gemini API Key (2 minutes, FREE)

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the API key (starts with `AIzaSy...`)
5. Save it somewhere safe - you'll need it in Step 3

**Important**: 
- No credit card required!
- Free tier: 1,500 requests/day
- This is enough for 100-200 website analyses per day

## 🚀 Step 2: Clone and Setup Project

```bash
# Clone the repository (if not already done)
git clone <your-repo-url>
cd seo-agent-mvp

# Verify directory structure
ls
# You should see: backend/ frontend/ docs/ README.md etc.
```

## 🐍 Step 3: Backend Setup

### Option A: Using uv (Recommended - Faster)

```bash
# Install uv if not already installed
# Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/Mac:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to backend
cd backend

# Create virtual environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Option B: Using pip (Standard)

```bash
cd backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

## ⚙️ Step 4: Configure Environment Variables

```bash
# From backend directory
# Copy example env file
# Windows:
copy .env.example .env
# Linux/Mac:
cp .env.example .env

# Edit .env file with your favorite editor
# Windows:
notepad .env
# Linux/Mac:
nano .env
# Or use VS Code:
code .env
```

**Required**: Edit `.env` and add your Gemini API key:

```env
# REQUIRED: Your Google Gemini API key
GEMINI_API_KEY=AIzaSy...paste-your-key-here

# These have sensible defaults, but you can customize:
PORT=3001
DEBUG=True
FRONTEND_URL=http://localhost:3000
MAX_REQUESTS_PER_15MIN=5
MAX_PAGES_PER_SITE=50
```

## ✅ Step 5: Test the Setup

```bash
# Make sure you're in backend directory and venv is activated
cd backend
# (verify venv is active - you should see (.venv) in your prompt)

# Run the server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 3001

# Or using uv:
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 3001
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:3001 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Starting SEO Agent MVP...
INFO:     Debug mode: True
INFO:     Frontend URL: http://localhost:3000
INFO:     Gemini API configured: Yes
INFO:     Application startup complete.
```

## 🧪 Step 6: Verify API is Working

Open your browser and visit:

1. **API Root**: http://localhost:3001/
   - Should show API information

2. **Health Check**: http://localhost:3001/health
   - Should show `"status": "healthy"` and `"gemini_available": true`

3. **Interactive Docs**: http://localhost:3001/docs
   - Should show Swagger UI with API documentation

**If you see the interactive docs, congratulations! Your backend is working! 🎉**

## 🔍 Troubleshooting

### Issue: "GEMINI_API_KEY is required"

**Solution**: Make sure you created `.env` file in the `backend/` directory and added your API key:
```bash
cd backend
ls -la  # Should see .env file
cat .env  # Verify GEMINI_API_KEY is set
```

### Issue: "Module not found"

**Solution**: Make sure virtual environment is activated and dependencies are installed:
```bash
# Check if venv is active (should see (.venv) in prompt)
# If not active:
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Playwright browsers not found"

**Solution**: Install Playwright browsers:
```bash
playwright install chromium
```

### Issue: Port 3001 already in use

**Solution**: Either:
1. Stop the process using port 3001
2. Or change PORT in `.env` to another number (e.g., 3002)

## 📦 What's Next?

Your backend foundation is now ready! Here's what needs to be implemented:

### Phase 1: Core Processing Modules (Next Priority)

1. **Create AI Agent Module** (`backend/app/modules/ai_agent.py`)
   - Gemini API integration
   - SEO analysis prompts
   - Response parsing

2. **Create Web Crawler Module** (`backend/app/modules/crawler.py`)
   - Playwright-based crawling
   - Page extraction
   - robots.txt compliance

3. **Create SEO Analyzer Module** (`backend/app/modules/seo_analyzer.py`)
   - Meta tags analysis
   - Keyword density
   - Header hierarchy
   - Internal linking

4. **Create Report Generator Module** (`backend/app/modules/report_gen.py`)
   - PDF generation with ReportLab
   - Charts and visualizations
   - Implementation checklist

### Phase 2: API Routes

1. **Create Analysis Route** (`backend/app/api/routes/analyze.py`)
   - POST /api/v1/analyze endpoint
   - GET /api/v1/status/{task_id} endpoint
   - GET /api/v1/download/{task_id} endpoint

### Phase 3: Frontend (Optional for MVP)

Basic HTML/CSS/JS form to test the API, or a full Next.js application.

## 🚀 Quick Development Workflow

```bash
# Start backend development server
cd backend
.venv\Scripts\activate  # or source .venv/bin/activate
uvicorn app.main:app --reload

# Keep this terminal open and code in another window
# Changes will auto-reload thanks to --reload flag
```

## 📚 Additional Resources

- **Gemini API Docs**: https://ai.google.dev/docs
- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Playwright Python**: https://playwright.dev/python/docs/intro
- **ReportLab Docs**: https://www.reportlab.com/docs/reportlab-userguide.pdf

## 💡 Development Tips

1. **Use Interactive Docs**: http://localhost:3001/docs
   - Test API endpoints without writing frontend code
   - See request/response examples
   - Try out API calls directly

2. **Check Logs**: The server logs will show detailed information about requests and errors

3. **Use DEBUG=True**: In development, this gives detailed error messages

4. **Test with curl**:
   ```bash
   curl http://localhost:3001/health
   ```

## ✅ Ready to Build!

Once you see the health check returning `"healthy"`, you're ready to start implementing the core modules!

Would you like me to create:
1. The AI Agent module with Gemini integration?
2. The Web Crawler module with Playwright?
3. The SEO Analyzer module?
4. API route handlers?

Just let me know which module you'd like me to build next!

---

**Need Help?**
- Check the logs in your terminal
- Verify `.env` file is configured correctly
- Ensure virtual environment is activated
- Make sure Gemini API key is valid
