from sqlalchemy import String, DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from uuid import uuid4, UUID
from app.core.database import Base


class InteractiveCourse(Base):
    __tablename__ = 'interactive_courses'

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey('learning_projects.id', ondelete='CASCADE'), unique=True, nullable=False)
    course_manifest: Mapped[str] = mapped_column(Text, nullable=False)
    scene_graph: Mapped[str] = mapped_column(Text, nullable=False)
    agent_profiles: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default='ready')
    generated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
