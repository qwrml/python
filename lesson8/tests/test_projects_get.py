import pytest

class TestProjectsGet:
    def test_get_project_success(self, projects_api, random_project_name):
        create_response = projects_api.create_project(random_project_name)
        project_id = create_response.json()["id"]
        
        response = projects_api.get_project(project_id)
        assert response.status_code == 200
        project_data = response.json()
        assert project_data["id"] == project_id
        assert project_data["title"] == random_project_name
    
    def test_get_nonexistent_project(self, projects_api):
        response = projects_api.get_project("invalid-project-id")
        assert response.status_code != 200
        assert response.status_code >= 400