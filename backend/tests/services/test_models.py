from app.models.project import LearningProject


def test_project_model_has_owner_and_status():
    assert hasattr(LearningProject, 'user_id')
    assert hasattr(LearningProject, 'status')
    assert hasattr(LearningProject, 'title')
    assert hasattr(LearningProject, 'goal')
