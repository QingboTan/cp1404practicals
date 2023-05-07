import datetime
from project import Project
MENU = "- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit"

display_list = []


def main(self):
    in_file = open("projects.txt", "r")
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "L":
            user_file = input("File name: ")
            in_file = open(user_file, "r")
        if user_choice == "S":
            filename = input("Filename: ")
            save_data(filename, projects)
            print("Save complete")
        if user_choice == "D":
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                projects = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                display_list.append(projects)
            display_list.sort()
            for i in display_list:
                print(i)
        if user_choice == "F":
            self.filter_projects_by_date
        if user_choice == "A":
            self.add_project()
        if user_choice == "U":
            self.update_project
        print(MENU)
        user_choice = input(">>> ").upper()
    in_file.close()


def save_data(filename, projects):
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete", file=out_file)
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(self, projects):
    print("Incomplete projects: ")
    for project in projects:
        if project.completion < 100:
            print(f"  {project}")
    print("Completed projects: ")
    for project in projects:
        if project.completion == 100:
            print(f"  {project}")


def filter_projects_by_date(self, projects):
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        filtered_projects = [project for project in projects if project.start_date > date]
        self.display_projects(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yy.")


def add_project(self):
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
        priority = int(input("Priority: "))
        estimate = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        self.projects.append(Project(name, start_date, priority, estimate, completion))
        print("Project added successfully")
    except ValueError:
        print("Invalid input. Please try again.")


def update_project(self):
    self.display_projects(self.projects)
    choice = int(input("Project choice: "))
    project = self.projects[choice]
    print(project)
    try:
        new_completion = int(input("New Percentage: "))
        new_priority_str = input("New Priority: ")
        if new_priority_str:
            new_priority = int(new_priority_str)
            project.priority = new_priority
        project.completion = new_completion
        print("Project updated successfully")
    except ValueError:
        print("Invalid input. Please try again.")

main(self="projects.txt")
