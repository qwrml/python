import pytest

class TestProjectsUpdate:
    def test_update_project_success(self, projects_api, random_project_name):
        create_response = projects_api.create_project(random_project_name)
        project_id = create_response.json()["id"]
        
        new_title = f"Updated {random_project_name}"
        response = projects_api.update_project(project_id, new_title)
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data
        assert response_data["id"] == project_id
        
        get_response = projects_api.get_project(project_id)
        assert get_response.json()["title"] == new_title
    
    def test_update_nonexistent_project(self, projects_api):
        response = projects_api.update_project("invalid-project-id", "New Title")
        assert response.status_code != 200
        assert response.status_code >= 400