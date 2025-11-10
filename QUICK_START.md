# SEO Agent MVP - Quick Start 🚀

Get up and running in 5 minutes!

## ✅ Checklist

- [ ] Python 3.11+ installed
- [ ] Git installed
- [ ] Got Gemini API key from https://makersuite.google.com/app/apikey

## 🎯 Quick Commands

```bash
# 1. Install uv (if not already)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. Setup backend
cd backend
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
playwright install chromium

# 3. Configure
copy .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 4. Run
uv run uvicorn app.main:app --reload --port 3001

# 5. Test
# Open browser: http://localhost:3001/docs
```

## 📝 What You Get

✅ FastAPI backend with async support  
✅ Google Gemini AI integration (1,500 free requests/day)  
✅ Pydantic models for type safety  
✅ Rate limiting & CORS configured  
✅ Interactive API documentation  
✅ Health check endpoint  
✅ 100% FREE hosting ready (Render)  

## 🎨 Project Structure

```
seo-agent-mvp/
├── backend/
│   ├── app/
│   │   ├── main.py          ✅ FastAPI app
│   │   ├── config.py        ✅ Settings
│   │   ├── models/          ✅ Request/Response models
│   │   ├── api/routes/      ⏳ TODO: API endpoints
│   │   ├── modules/         ⏳ TODO: Processing modules
│   │   └── utils/           ⏳ TODO: Utilities
│   ├── requirements.txt     ✅ Dependencies
│   └── .env.example         ✅ Config template
├── render.yaml              ✅ Deployment config
├── SETUP.md                 ✅ Detailed guide
└── README.md                ✅ Documentation
```

## 🔨 Next Steps

**Phase 1: Core Modules** (What's needed next)

1. **AI Agent** (`backend/app/modules/ai_agent.py`)
   - Integrate Gemini API
   - Create SEO analysis prompts
   
2. **Web Crawler** (`backend/app/modules/crawler.py`)
   - Playwright browser automation
   - Extract website content
   
3. **SEO Analyzer** (`backend/app/modules/seo_analyzer.py`)
   - Meta tags, headers, keywords
   - Technical SEO checks
   
4. **Report Generator** (`backend/app/modules/report_gen.py`)
   - PDF reports with ReportLab
   - ZIP file packaging

**Phase 2: API Routes**

5. **Analysis Routes** (`backend/app/api/routes/analyze.py`)
   - POST /api/v1/analyze
   - GET /api/v1/status/{task_id}
   - GET /api/v1/download/{task_id}

## 💰 Cost Breakdown

| Service | Cost | Usage |
|---------|------|-------|
| Render Hosting | $0 | Free tier (750hrs/month) |
| Gemini API | $0 | 1,500 requests/day free |
| Google APIs | $0 | Free tier |
| Playwright | $0 | Open source |
| **Total** | **$0/month** | Perfect for MVP! |

## 🎓 Learn More

- Full setup: See [SETUP.md](SETUP.md)
- Architecture: See [README.md](README.md)
- API docs: http://localhost:3001/docs (after starting server)

## 💡 Tips

- Use `--reload` flag during development for auto-reload
- Check logs for detailed error messages
- Test with interactive docs at `/docs`
- Health check at `/health`

---

**Ready to build the core modules?** Just ask which one you'd like to implement next!
