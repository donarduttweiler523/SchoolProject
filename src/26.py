class SimpleSchoolProject:
    def __init__(self):
        self.projects = []

    def add_project(self, name, description):
        new_project = {
            "name": name,
            "description": description
        }
        self.projects.append(new_project)
        return new_project

    def list_projects(self):
        return selfprojects

    def remove_project(self, project_name):
        for p in self.projects:
            if p["name"] == project_name:
                self.projects.remove(p)
                break
