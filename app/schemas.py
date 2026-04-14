"""
Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


# =============================================================================
# Schema Definitions
# =============================================================================

class PredictionRequest(BaseModel):
    """Request schema for prediction endpoint."""
    user_id: str = Field(..., example="196")
    movie_id: str = Field(..., example="242")




class PredictionResponse(BaseModel):
    """Response schema for prediction endpoint."""
    model_config = ConfigDict(protected_namespaces=())
    
    user_id: str = Field(..., example="196")
    movie_id: str = Field(..., example="242")
    predicted_rating: float = Field(..., example=4.02)
    model_version: str = Field(..., example="1.0.0")




class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""
    # Disable protected namespaces to avoid naming conflicts with Pydantic's internal model_ prefixed variables
    model_config = ConfigDict(protected_namespaces=())
    
    status: str = Field(..., example="healthy")
    model_loaded: bool = Field(..., example=True)


# =============================================================================
# Batch Prediction Schemas
# =============================================================================

class PredictionItem(BaseModel):
    """Single prediction item for batch requests."""
    user_id: str = Field(..., example="196")
    movie_id: str = Field(..., example="242")


class BatchPredictionRequest(BaseModel):
    """Request schema for batch prediction endpoint."""
    predictions: List[PredictionItem]


class BatchPredictionResponse(BaseModel):
    """Response schema for batch prediction endpoint."""
    predictions: List[PredictionResponse]
    total_count: int = Field(..., example=1)
