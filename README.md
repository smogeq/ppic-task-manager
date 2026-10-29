# Task Manager CI/CD

UTS 43030 Professional Practice in Computing, Software Development module, Lecture 4 activities.

A small Python task manager with unit tests, packaged in Docker and run by GitHub Actions on every push to `main`. The workflow writes the current tasks and test results into `index.html`. A second workflow (`tracker.yml`) closes and comments on the linked issue when a pull request is merged, and the GitHub Projects board moves it to Done.
