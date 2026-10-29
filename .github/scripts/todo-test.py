"""Activity 4: unit tests for TaskPool, printed in a short readable format."""
import io
import sys
import unittest

from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        # Runs before each test: start every test with an empty pool.
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Write the README")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertEqual(len(done_tasks), 3)
        self.assertTrue(all(task.completed for task in done_tasks))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

    # Capture the runner's output so we can print a cleaner version.
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)

    for line in stream.getvalue().splitlines():
        if line.endswith("... ok"):
            test_name = line.split(" ")[0]
            print(f"{test_name} ... ok")

    if not result.wasSuccessful():
        # Show the full report and fail the pipeline.
        print(stream.getvalue())
        sys.exit(1)
