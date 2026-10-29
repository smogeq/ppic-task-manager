"""Activity 3: a simple task manager with Task and TaskPool classes."""


class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        """Create six sample tasks and mark the first three as completed."""
        tasks = [
            Task("Set up the repository"),
            Task("Write todo.py"),
            Task("Write the unit tests"),
            Task("Write the Dockerfile"),
            Task("Configure ci.yml"),
            Task("Automate the project board"),
        ]
        for task in tasks[:3]:
            task.mark_completed()
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    open_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in open_titles:
        print(title)

    done_titles = [task.title for task in pool.get_done_tasks()]
    print("Done Tasks:")
    for title in done_titles:
        print(title)


if __name__ == "__main__":
    main()
