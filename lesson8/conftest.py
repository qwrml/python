import pytest
import random
from api.projects_client import ProjectsAPI

@pytest.fixture
def projects_api():
    return ProjectsAPI()

@pytest.fixture
def random_project_name():
    return f"Test Project {random.randint(1000, 9999)}"