from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        #self.open_manage_projects_page()

    def open_manage_projects_page(self):
         wd = self.app.wd
         if not (wd.current_url.endswith("/manage_proj_page.php")):
             if not (wd.current_url.endswith("/manage_overview_page.php")):
                wd.find_element_by_link_text("Manage").click()
             wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
         wd = self.app.wd
         self.change_field("name", project.name)
         self.change_field("description", project.description)

    def change_field(self, field_name, text):
         wd = self.app.wd
         if text is not None:
             wd.find_element_by_name(field_name).click()
             wd.find_element_by_name(field_name).clear()
             wd.find_element_by_name(field_name).send_keys(text)

    def delete_by_name(self, name):
         wd = self.app.wd
         self.open_manage_projects_page()
         self.select_project_by_name(name)
         # submit deletion
         wd.find_element_by_xpath("//input[@value='Delete Project']").click()
         wd.find_element_by_xpath("//input[@value='Delete Project']").click()
         #self.open_manage_projects_page()

    def select_project_by_name(self, name):
         wd = self.app.wd
         wd.find_element_by_link_text("%s" % name).click()

   # def return_to_groups_page(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("group page").click()
    #
    # def create(self, group):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     # init group creation
    #     wd.find_element_by_name("new").click()
    #     self.fill_group_form(group)
    #     # submit group creation
    #     wd.find_element_by_name("submit").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def open_groups_page(self):
    #     wd = self.app.wd
    #     if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
    #         wd.find_element_by_link_text("groups").click()
    #
    # def delete_by_index(self, index):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     # submit deletion
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def delete_first(self):
    #     self.delete_by_index(0)
    #
    # def edit_by_index(self, index, group):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     # open edit form
    #     wd.find_element_by_name("edit").click()
    #     self.fill_group_form(group)
    #     # submit group update
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def edit_first(self, group):
    #     self.edit_by_index(0, group)
    #
    # def select_first_group(self):
    #     wd = self.app.wd
    #     wd.find_element_by_name("selected[]").click()
    #
    # def select_group_by_index(self, index):
    #     wd = self.app.wd
    #     wd.find_elements_by_name("selected[]")[index].click()
    #
    # def fill_group_form(self, group):
    #     wd = self.app.wd
    #     self.change_field("group_name", group.name)
    #     self.change_field("group_header", group.header)
    #     self.change_field("group_footer", group.footer)
    #
    # def change_field(self, field_name, text):
    #     wd = self.app.wd
    #     if text is not None:
    #         wd.find_element_by_name(field_name).click()
    #         wd.find_element_by_name(field_name).clear()
    #         wd.find_element_by_name(field_name).send_keys(text)
    #
    # def count(self):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     return len(wd.find_elements_by_name("selected[]"))
    #
    # group_cache = None
    #
    # def get_list(self):
    #     if self.group_cache is None:
    #         wd = self.app.wd
    #         self.open_groups_page()
    #         self.group_cache = []
    #         for element in wd.find_elements_by_css_selector("span.group"):
    #             text = element.text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.group_cache.append(Group(name=text, id=id))
    #     return list(self.group_cache)
    #
    # def delete_by_id(self, id):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     # submit deletion
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def select_group_by_id(self, id):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("input[value='%s']" % id).click()
    #
    # def edit_by_id(self, id, group):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     # open edit form
    #     wd.find_element_by_name("edit").click()
    #     self.fill_group_form(group)
    #     # submit group update
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None