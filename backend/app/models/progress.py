from sqlalchemy import String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from uuid import uuid4, UUID
from app.core.database import Base


class StudyProgress(Base):
    __tablename__ = 'study_progress'

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey('learning_projects.id', ondelete='CASCADE'), unique=True, nullable=False)
    workspace_progress: Mapped[str] = mapped_column(Text, nullable=True)
    course_progress: Mapped[str] = mapped_column(Text, nullable=True)
    quiz_attempts: Mapped[str] = mapped_column(Text, nullable=True)
    completed_task_ids: Mapped[str] = mapped_column(Text, nullable=True)
    recent_knowledge_node_ids: Mapped[str] = mapped_column(Text, nullable=True)
    last_activity_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
