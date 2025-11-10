# SEO Agent MVP - 100% FREE POC

AI-powered SEO analysis service for small to medium businesses. Completely FREE implementation using open-source tools and free-tier services.

## 🎯 Features

- **Automated Website Crawling**: Analyze up to 50 pages per site (Playwright)
- **Technical SEO Audit**: Performance, accessibility, Core Web Vitals (Google Lighthouse)
- **AI-Powered Recommendations**: Google Gemini 1.5 Flash (1,500 free requests/day)
- **On-Page SEO Analysis**: Meta tags, headers, keywords, internal linking
- **Google Integration**: Search Console & Analytics (optional, free)
- **Deliverables**: 
  - Optimized website files (HTML/CSS/JS)
  - Comprehensive PDF report
  - Implementation checklist

## 💰 Total Cost: $0/month

- **Hosting**: Render Free Tier
- **AI Model**: Google Gemini (1,500 requests/day FREE)
- **Web Crawling**: Playwright (open source)
- **Technical Audit**: Google Lighthouse (free)
- **All APIs**: Google services (free tier)

## 🏗️ Architecture

```
Frontend (Next.js) → API Gateway (FastAPI) → Processing Pipeline
                                                ↓
                                    ┌───────────────────────┐
                                    │ 1. Playwright Crawler │
                                    │ 2. Lighthouse Audit   │
                                    │ 3. SEO Analysis       │
                                    │ 4. Gemini AI Agent    │
                                    │ 5. Report Generation  │
                                    └───────────────────────┘
                                                ↓
                                    Results Package (ZIP)
```

## 📦 Tech Stack

**Backend:**
- FastAPI - Modern async Python API framework
- Playwright - Headless browser automation
- Google Gemini - AI analysis (FREE tier)
- ReportLab - PDF generation
- Google APIs - Search Console & Analytics

**Frontend:**
- Next.js 14 - React framework
- Tailwind CSS - Styling
- Shadcn/ui - UI components

**Deployment:**
- Render Free Tier - $0/month hosting
- GitHub Actions - Free CI/CD

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- uv (recommended) or pip
- Git
- Node.js 20+ (for frontend)

### Backend Setup

```bash
# Clone repository
git clone <your-repo-url>
cd seo-agent-mvp/backend

# Install uv if not already installed
# Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Initialize Python environment with uv
uv venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
uv pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Set up environment variables
copy .env.example .env
# Edit .env with your API keys
```

### Environment Variables

Create `.env` file in backend directory:

```env
# Google Gemini API (FREE - get from https://makersuite.google.com/app/apikey)
GEMINI_API_KEY=AIzaSy...

# Google OAuth (optional, for Search Console/Analytics)
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_REDIRECT_URI=http://localhost:3001/auth/google/callback

# Server Configuration
PORT=3001
HOST=0.0.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3000

# Rate Limiting
MAX_REQUESTS_PER_15MIN=5
MAX_PAGES_PER_SITE=50

# Processing
TEMP_FILE_RETENTION_HOURS=24
```

### Run Backend

```bash
cd backend
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 3001
```

API will be available at: http://localhost:3001
Interactive docs at: http://localhost:3001/docs

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: http://localhost:3000

## 📊 API Documentation

### Key Endpoints

**POST /api/v1/analyze**
- Submit website for SEO analysis
- Returns task ID for tracking

**GET /api/v1/status/:taskId**
- Check analysis progress
- Poll every 5 seconds

**GET /api/v1/download/:taskId**
- Download results package (ZIP)
- Contains optimized files + PDF report

**GET /health**
- Health check endpoint

Full API documentation: [docs/api-spec.yaml](docs/api-spec.yaml)

## 🧪 Testing

```bash
# Backend tests
cd backend
uv run pytest

# Frontend tests
cd frontend
npm test
```

## 🚢 Deployment

### Deploy to Render (FREE)

1. **Create Render Account**: https://render.com (free, no credit card)

2. **Create New Web Service**:
   - Connect GitHub repository
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt && playwright install chromium`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Plan: **Free** ($0/month)

3. **Add Environment Variables** in Render dashboard:
   - `GEMINI_API_KEY`
   - `FRONTEND_URL` (your frontend URL)
   - All other vars from `.env.example`

4. **Deploy Frontend** (Render or Vercel):
   - Root directory: `frontend`
   - Build command: `npm run build`
   - Start command: `npm start`
   - Plan: **Free**

### Auto-Deploy with GitHub Actions

Push to `main` branch automatically deploys to Render.

## 📈 Success Metrics

**MVP POC Goals (Month 1):**
- ✅ Complete 20-30 test analyses
- ✅ Maintain $0/month cost
- ✅ Validate product-market fit
- ✅ Gather user feedback

**Technical Targets:**
- Uptime: ≥99%
- Analysis completion time: <15 minutes
- Success rate: >95%

## 🎯 MVP Feature Scope

**✅ Included in POC:**
- Website crawling (up to 50 pages)
- Technical SEO audit (Lighthouse)
- On-page SEO analysis
- AI-powered recommendations (Gemini)
- PDF report generation
- Optimized file package
- Download as ZIP

**⏸️ Phase 2 Features:**
- User authentication
- Competitor SERP analysis
- Backlink analysis
- Email notifications
- Analysis history
- Subscription plans

## 📋 Project Structure

```
seo-agent-mvp/
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── main.py            # FastAPI application
│   │   ├── config.py          # Settings & environment
│   │   ├── api/
│   │   │   └── routes/        # API endpoints
│   │   ├── modules/           # Core processing modules
│   │   ├── models/            # Pydantic models
│   │   ├── services/          # External services
│   │   └── utils/             # Utilities
│   ├── tests/                 # Tests
│   ├── requirements.txt       # Python dependencies
│   └── pyproject.toml         # uv configuration
├── frontend/                  # Next.js frontend
│   ├── app/                   # Next.js app directory
│   ├── components/            # React components
│   └── package.json
├── docs/                      # Documentation
│   ├── api-spec.yaml         # OpenAPI specification
│   └── architecture.md       # Architecture details
├── shared/                    # Shared code/types
└── .github/
    └── workflows/            # CI/CD pipelines
```

## 🔑 Getting API Keys

### Google Gemini (FREE, 2 minutes)

1. Visit: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy key (starts with `AIzaSy...`)
4. Add to `.env`: `GEMINI_API_KEY=AIzaSy...`

**No credit card required!** Free tier: 1,500 requests/day

### Google Search Console (Optional, FREE)

1. Visit: https://console.cloud.google.com
2. Create new project
3. Enable Search Console API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URI
6. Copy Client ID and Secret to `.env`

## 📝 License

MIT License - Free for commercial use

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md

## 📧 Support

- Report bugs: GitHub Issues
- Questions: GitHub Discussions

---

**Built with ❤️ for the SEO community**

*Completely FREE MVP - Zero monthly costs*
