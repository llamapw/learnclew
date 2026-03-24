from sqlalchemy import String, DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from uuid import uuid4, UUID
from app.core.database import Base


class LearningWorkspace(Base):
    __tablename__ = 'learning_workspaces'

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey('learning_projects.id', ondelete='CASCADE'), unique=True, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    knowledge_map_version: Mapped[str] = mapped_column(String(64), nullable=True)
    quiz_set_version: Mapped[str] = mapped_column(String(64), nullable=True)
    study_plan_version: Mapped[str] = mapped_column(String(64), nullable=True)
    qa_index_version: Mapped[str] = mapped_column(String(64), nullable=True)
    generated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
