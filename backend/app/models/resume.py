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

    # --- columns (Mapped[T] syntax gives Pylance full type awareness) --------
    id:            Mapped[int]            = mapped_column(Integer, primary_key=True)
    filename:      Mapped[str]            = mapped_column(String(255), nullable=False)
    resume_text:   Mapped[str]            = mapped_column(Text, nullable=False)
    analysis_json: Mapped[Optional[str]]  = mapped_column(Text, nullable=True)
    ats_score:     Mapped[Optional[int]]  = mapped_column(Integer, nullable=True)
    recruiter_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at:    Mapped[datetime]       = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
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
            'created_at': self.created_at.isoformat(),
            'analysis': analysis,
        }

    def to_summary_dict(self) -> dict:
        """Lightweight version used for the history list (no full analysis)."""
        return {
            'id': self.id,
            'filename': self.filename,
            'ats_score': self.ats_score,
            'recruiter_score': self.recruiter_score,
            'created_at': self.created_at.isoformat(),
        }
