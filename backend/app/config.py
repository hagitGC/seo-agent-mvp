"""
Configuration module for SEO Agent MVP
Loads environment variables and provides settings
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Server Configuration
    PORT: int = 3001
    HOST: str = "0.0.0.0"
    DEBUG: bool = True
    FRONTEND_URL: str = "http://localhost:3000"
    
    # Google Gemini API (FREE tier)
    GEMINI_API_KEY: str = "not-set"  # Will be required later, but optional for testing
    GEMINI_PRIMARY_MODEL: str = "gemini-1.5-flash"
    GEMINI_PRIMARY_DAILY_LIMIT: int = 1500
    GEMINI_FALLBACK_MODEL: str = "gemini-1.5-pro"
    GEMINI_FALLBACK_DAILY_LIMIT: int = 50
    
    # Google OAuth (Optional)
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: Optional[str] = None
    
    # Rate Limiting & Processing
    MAX_REQUESTS_PER_15MIN: int = 5
    MAX_PAGES_PER_SITE: int = 50
    MAX_CONCURRENT_ANALYSES: int = 3
    
    # File Storage
    TEMP_FILE_RETENTION_HOURS: int = 24
    RESULTS_DIR: str = "/tmp/seo-agent-results"
    
    # Optional: OpenAI (for comparison/testing)
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o-mini"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode"""
        return not self.DEBUG
    
    @property
    def has_google_oauth(self) -> bool:
        """Check if Google OAuth is configured"""
        return all([
            self.GOOGLE_CLIENT_ID,
            self.GOOGLE_CLIENT_SECRET,
            self.GOOGLE_REDIRECT_URI
        ])
    
    @property
    def has_openai(self) -> bool:
        """Check if OpenAI is configured"""
        return self.OPENAI_API_KEY is not None


# Create global settings instance
settings = Settings()
