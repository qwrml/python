import requests
from config import BASE_URL, API_KEY

class ProjectsAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def create_project(self, title):
        url = f"{self.base_url}/api-v2/projects"
        data = {"title": title}
        response = requests.post(url, json=data, headers=self.headers)
        return response
    
    def get_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response
    
    def update_project(self, project_id, title):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        data = {"title": title}
        response = requests.put(url, json=data, headers=self.headers)
        return response