from sqlalchemy import String, DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from uuid import uuid4, UUID
from app.core.database import Base


class LearningAsset(Base):
    __tablename__ = 'learning_assets'

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey('learning_projects.id', ondelete='CASCADE'), unique=True, nullable=False)
    normalized_text: Mapped[str] = mapped_column(Text, nullable=False)
    source_chunks: Mapped[str] = mapped_column(Text, nullable=True)
    images: Mapped[str] = mapped_column(Text, nullable=True)
    video_frames: Mapped[str] = mapped_column(Text, nullable=True)
    timeline_segments: Mapped[str] = mapped_column(Text, nullable=True)
    references: Mapped[str] = mapped_column(Text, nullable=True)
    extra_metadata: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
