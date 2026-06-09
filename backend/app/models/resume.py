from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Optional

from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, Integer, Float, String, DateTime


class ResumeAnalysis(db.Model):
    """Stores each resume upload and its AI analysis result."""

    __tablename__ = 'resume_analyses'

    id:              Mapped[int]            = mapped_column(Integer, primary_key=True)
    filename:        Mapped[str]            = mapped_column(String(255), nullable=False)
    resume_text:     Mapped[str]            = mapped_column(Text, nullable=False)
    analysis_json:   Mapped[Optional[str]]  = mapped_column(Text, nullable=True)
    ats_score:       Mapped[Optional[int]]  = mapped_column(Integer, nullable=True)
    recruiter_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at:      Mapped[datetime]       = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def __init__(
        self,
        filename: str,
        resume_text: str,
        analysis_json: Optional[str] = None,
        ats_score: Optional[int] = None,
        recruiter_score: Optional[float] = None,
    ) -> None:
        """
        Explicit __init__ so Pylance knows exactly which keyword arguments
        this model accepts. SQLAlchemy's declarative base would generate this
        automatically at runtime, but static type checkers cannot see that.
        """
        super().__init__(
            filename=filename,
            resume_text=resume_text,
            analysis_json=analysis_json,
            ats_score=ats_score,
            recruiter_score=recruiter_score,
        )

    # -------------------------------------------------------------------------
    # Serialisers
    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:
        analysis: dict = {}
        if self.analysis_json:
            try:
                analysis = json.loads(self.analysis_json)
            except json.JSONDecodeError:
                analysis = {}

        return {
            'id': self.id,
            'filename': self.filename,
            'ats_score': self.ats_score,
            'recruiter_score': self.recruiter_score,
            'created_at': self.created_at.isoformat() if self.created_at else '',
            'analysis': analysis,
        }

    def to_summary_dict(self) -> dict:
        """Lightweight version used for the history list (no full analysis)."""
        return {
            'id': self.id,
            'filename': self.filename,
            'ats_score': self.ats_score,
            'recruiter_score': self.recruiter_score,
            'created_at': self.created_at.isoformat() if self.created_at else '',
        }
