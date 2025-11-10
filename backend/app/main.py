"""
SEO Agent MVP - Main FastAPI Application
100% FREE implementation with Google Gemini
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from contextlib import asynccontextmanager
import logging
from datetime import datetime

from app.config import settings
from app.models.responses import ErrorResponse

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager
    Handles startup and shutdown events
    """
    # Startup
    logger.info("Starting SEO Agent MVP...")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"Frontend URL: {settings.FRONTEND_URL}")
    logger.info(f"Gemini API configured: {'Yes' if settings.GEMINI_API_KEY else 'No'}")
    
    # Create results directory if it doesn't exist
    import os
    os.makedirs(settings.RESULTS_DIR, exist_ok=True)
    logger.info(f"Results directory: {settings.RESULTS_DIR}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down SEO Agent MVP...")


# Create FastAPI app
app = FastAPI(
    title="SEO Agent API",
    description="AI-powered SEO analysis service for SMBs - 100% FREE MVP",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions"""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal server error",
            code="INTERNAL_ERROR",
            details={"message": str(exc) if settings.DEBUG else "An unexpected error occurred"}
        ).model_dump()
    )


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint
    Returns service status and configuration
    """
    from app.models.responses import HealthResponse
    
    # Check if Gemini API is configured
    gemini_available = bool(settings.GEMINI_API_KEY and len(settings.GEMINI_API_KEY) > 10)
    
    status = "healthy" if gemini_available else "degraded"
    
    return HealthResponse(
        status=status,
        timestamp=datetime.utcnow(),
        version="1.0.0",
        gemini_available=gemini_available
    )


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - API information
    """
    return {
        "name": "SEO Agent API",
        "version": "1.0.0",
        "description": "AI-powered SEO analysis service - 100% FREE MVP",
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "analyze": "POST /api/v1/analyze",
            "status": "GET /api/v1/status/{task_id}",
            "download": "GET /api/v1/download/{task_id}"
        },
        "ai_model": "Google Gemini 1.5 Flash",
        "cost": "$0/month (FREE tier)"
    }


# Include API routers (we'll create these next)
# from app.api.routes import analyze, health
# app.include_router(analyze.router, prefix="/api/v1", tags=["Analysis"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=1  # Single worker for MVP
    )
