"""
Response models for API endpoints
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from uuid import UUID


class AnalysisResponse(BaseModel):
    """Response after submitting analysis request"""
    
    task_id: UUID = Field(
        ...,
        description="Unique task ID for tracking analysis progress"
    )
    status: Literal["queued", "processing", "complete", "failed"] = Field(
        ...,
        description="Current status of the analysis"
    )
    estimated_time: str = Field(
        ...,
        description="Estimated completion time",
        examples=["15 minutes"]
    )
    status_url: str = Field(
        ...,
        description="URL to check analysis status",
        examples=["/api/v1/status/550e8400-e29b-41d4-a716-446655440000"]
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "task_id": "550e8400-e29b-41d4-a716-446655440000",
                "status": "queued",
                "estimated_time": "15 minutes",
                "status_url": "/api/v1/status/550e8400-e29b-41d4-a716-446655440000"
            }
        }
    }


class StatusResponse(BaseModel):
    """Response for status check"""
    
    task_id: UUID = Field(
        ...,
        description="Task ID"
    )
    status: Literal["queued", "processing", "complete", "failed"] = Field(
        ...,
        description="Current status"
    )
    progress: int = Field(
        ...,
        ge=0,
        le=100,
        description="Progress percentage (0-100)"
    )
    current_step: Optional[str] = Field(
        None,
        description="Current processing step",
        examples=["Running AI analysis", "Generating report"]
    )
    estimated_time_remaining: Optional[str] = Field(
        None,
        description="Estimated time remaining",
        examples=["5 minutes"]
    )
    download_url: Optional[str] = Field(
        None,
        description="Download URL (available when status is 'complete')",
        examples=["/api/v1/download/550e8400-e29b-41d4-a716-446655440000"]
    )
    expires_at: Optional[datetime] = Field(
        None,
        description="When the results will be deleted"
    )
    error: Optional[str] = Field(
        None,
        description="Error message (if status is 'failed')"
    )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "task_id": "550e8400-e29b-41d4-a716-446655440000",
                    "status": "processing",
                    "progress": 60,
                    "current_step": "Running AI analysis",
                    "estimated_time_remaining": "5 minutes"
                },
                {
                    "task_id": "550e8400-e29b-41d4-a716-446655440000",
                    "status": "complete",
                    "progress": 100,
                    "download_url": "/api/v1/download/550e8400-e29b-41d4-a716-446655440000",
                    "expires_at": "2025-11-11T10:00:00Z"
                }
            ]
        }
    }


class HealthResponse(BaseModel):
    """Health check response"""
    
    status: Literal["healthy", "degraded", "unhealthy"] = Field(
        ...,
        description="Service health status"
    )
    timestamp: datetime = Field(
        ...,
        description="Current server time"
    )
    version: str = Field(
        default="1.0.0",
        description="API version"
    )
    gemini_available: bool = Field(
        ...,
        description="Whether Gemini API is configured and available"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "healthy",
                "timestamp": "2025-11-10T10:00:00Z",
                "version": "1.0.0",
                "gemini_available": True
            }
        }
    }


class ErrorResponse(BaseModel):
    """Error response"""
    
    error: str = Field(
        ...,
        description="Error message",
        examples=["Invalid URL format"]
    )
    code: str = Field(
        ...,
        description="Error code",
        examples=["INVALID_INPUT", "RATE_LIMIT_EXCEEDED"]
    )
    details: Optional[dict] = Field(
        None,
        description="Additional error details"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "error": "Invalid URL format",
                "code": "INVALID_INPUT",
                "details": {
                    "field": "url",
                    "issue": "URL must include protocol (http:// or https://)"
                }
            }
        }
    }
