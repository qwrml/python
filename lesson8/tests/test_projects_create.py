import pytest

class TestProjectsCreate:
    def test_create_project_success(self, projects_api, random_project_name):
        response = projects_api.create_project(random_project_name)
        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        assert isinstance(response_data["id"], str)
        assert len(response_data["id"]) > 0
    
    def test_create_project_without_title(self, projects_api):
        response = projects_api.create_project(title=None)
        assert response.status_code != 201
        assert response.status_code >= 400