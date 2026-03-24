"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-03-24

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Users table
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('account_identifier', sa.String(length=255), nullable=False),
        sa.Column('display_name', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('last_active_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('account_identifier')
    )

    # Auth identities table
    op.create_table('auth_identities',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('identity_type', sa.String(length=64), nullable=False),
        sa.Column('identity_value', sa.String(length=255), nullable=False),
        sa.Column('credential_meta', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Learning projects table
    op.create_table('learning_projects',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('goal', sa.Text(), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('last_studied_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Learning sources table
    op.create_table('learning_sources',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('type', sa.String(length=64), nullable=False),
        sa.Column('source_url', sa.Text(), nullable=True),
        sa.Column('file_name', sa.String(length=255), nullable=True),
        sa.Column('storage_key', sa.String(length=512), nullable=True),
        sa.Column('status', sa.String(length=32), nullable=False),
        sa.Column('extra_metadata', sa.Text(), nullable=True),
        sa.Column('error', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Asset processing jobs table
    op.create_table('asset_processing_jobs',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('job_type', sa.String(length=64), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False),
        sa.Column('step', sa.String(length=64), nullable=True),
        sa.Column('progress', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(length=512), nullable=True),
        sa.Column('payload', sa.Text(), nullable=True),
        sa.Column('result', sa.Text(), nullable=True),
        sa.Column('retry_count', sa.Integer(), nullable=False),
        sa.Column('error', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Learning assets table
    op.create_table('learning_assets',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('normalized_text', sa.Text(), nullable=False),
        sa.Column('source_chunks', sa.Text(), nullable=True),
        sa.Column('images', sa.Text(), nullable=True),
        sa.Column('video_frames', sa.Text(), nullable=True),
        sa.Column('timeline_segments', sa.Text(), nullable=True),
        sa.Column('references', sa.Text(), nullable=True),
        sa.Column('extra_metadata', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('project_id')
    )

    # Learning workspaces table
    op.create_table('learning_workspaces',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('summary', sa.Text(), nullable=False),
        sa.Column('knowledge_map_version', sa.String(length=64), nullable=True),
        sa.Column('quiz_set_version', sa.String(length=64), nullable=True),
        sa.Column('study_plan_version', sa.String(length=64), nullable=True),
        sa.Column('qa_index_version', sa.String(length=64), nullable=True),
        sa.Column('generated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('project_id')
    )

    # Interactive courses table
    op.create_table('interactive_courses',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('course_manifest', sa.Text(), nullable=False),
        sa.Column('scene_graph', sa.Text(), nullable=False),
        sa.Column('agent_profiles', sa.Text(), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False),
        sa.Column('generated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('project_id')
    )

    # Study progress table
    op.create_table('study_progress',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('workspace_progress', sa.Text(), nullable=True),
        sa.Column('course_progress', sa.Text(), nullable=True),
        sa.Column('quiz_attempts', sa.Text(), nullable=True),
        sa.Column('completed_task_ids', sa.Text(), nullable=True),
        sa.Column('recent_knowledge_node_ids', sa.Text(), nullable=True),
        sa.Column('last_activity_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['project_id'], ['learning_projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('project_id')
    )

    # Stored objects table
    op.create_table('stored_objects',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('storage_provider', sa.String(length=64), nullable=False),
        sa.Column('storage_key', sa.String(length=512), nullable=False),
        sa.Column('mime_type', sa.String(length=128), nullable=False),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('kind', sa.String(length=64), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('storage_key')
    )


def downgrade() -> None:
    op.drop_table('stored_objects')
    op.drop_table('study_progress')
    op.drop_table('interactive_courses')
    op.drop_table('learning_workspaces')
    op.drop_table('learning_assets')
    op.drop_table('asset_processing_jobs')
    op.drop_table('learning_sources')
    op.drop_table('learning_projects')
    op.drop_table('auth_identities')
    op.drop_table('users')
