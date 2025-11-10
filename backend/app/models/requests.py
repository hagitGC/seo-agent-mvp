"""
Request models for API endpoints
"""

from pydantic import BaseModel, HttpUrl, Field, field_validator
from typing import List, Optional


class BusinessInfo(BaseModel):
    """Business information for SEO analysis context"""
    
    industry: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Business industry or niche",
        examples=["E-commerce", "SaaS", "Consulting"]
    )
    target_audience: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Target audience description",
        examples=["Small business owners", "B2B enterprises"]
    )
    location: Optional[str] = Field(
        None,
        max_length=100,
        description="Geographic service area",
        examples=["United States", "Global", "New York"]
    )


class AnalysisOptions(BaseModel):
    """Optional configuration for analysis"""
    
    include_competitor_analysis: bool = Field(
        default=False,
        description="Whether to include competitor SERP analysis (uses free tier API)"
    )
    max_pages: int = Field(
        default=50,
        ge=1,
        le=100,
        description="Maximum number of pages to crawl"
    )
    google_auth_token: Optional[str] = Field(
        None,
        description="OAuth token for Google Search Console/Analytics access"
    )


class AnalysisRequest(BaseModel):
    """Request body for website SEO analysis"""
    
    url: HttpUrl = Field(
        ...,
        description="Website URL to analyze",
        examples=["https://example.com"]
    )
    business_info: BusinessInfo = Field(
        ...,
        description="Business context information"
    )
    keywords: List[str] = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Target keywords for SEO analysis (3-10 keywords)",
        examples=[["business consulting", "marketing services", "growth strategies"]]
    )
    options: Optional[AnalysisOptions] = Field(
        default_factory=AnalysisOptions,
        description="Optional analysis configuration"
    )
    
    @field_validator('keywords')
    @classmethod
    def validate_keywords(cls, v: List[str]) -> List[str]:
        """Ensure keywords are not empty strings"""
        keywords = [k.strip() for k in v if k.strip()]
        if len(keywords) < 3:
            raise ValueError("At least 3 non-empty keywords are required")
        if len(keywords) > 10:
            raise ValueError("Maximum 10 keywords allowed")
        return keywords
    
    @field_validator('url')
    @classmethod
    def validate_url(cls, v: HttpUrl) -> HttpUrl:
        """Validate URL and prevent SSRF attacks"""
        url_str = str(v)
        blocked_hosts = ['localhost', '127.0.0.1', '0.0.0.0', '::1']
        
        # Extract hostname
        from urllib.parse import urlparse
        parsed = urlparse(url_str)
        
        if parsed.hostname in blocked_hosts:
            raise ValueError(f"Invalid hostname: {parsed.hostname}")
        
        return v
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "url": "https://example.com",
                "business_info": {
                    "industry": "E-commerce",
                    "target_audience": "Small business owners",
                    "location": "United States"
                },
                "keywords": [
                    "business consulting",
                    "marketing services",
                    "growth strategies"
                ],
                "options": {
                    "include_competitor_analysis": False,
                    "max_pages": 50
                }
            }
        }
    }
