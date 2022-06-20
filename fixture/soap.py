from suds.client import Client
from fixture.project import Project



class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        client = Client(self.app.base_url + 'api/soap/mantisconnect.php?wsdl')
        project_list = []
        resp = client.service.mc_projects_get_user_accessible(username=self.app.config["username"],
                                                              password=self.app.config["password"])

        for r in resp:
            project_list.append(Project(id=str(r["id"]), name=r["name"], description=r["description"]))
        return project_list