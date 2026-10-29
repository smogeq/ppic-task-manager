#!/bin/bash
# Activity 6: the script the Docker container runs when it starts.
# pipefail makes a failing test fail the whole run, even through tee.
set -eo pipefail

echo "Running the task manager..."
python3 /app/.github/scripts/todo.py | tee /tmp/tasks_output.txt

echo "Running the unit tests..."
python3 /app/.github/scripts/todo-test.py | tee /tmp/test_results.txt

echo "Updating index.html..."
bash /app/.github/scripts/update_index.sh /tmp/tasks_output.txt /tmp/test_results.txt

echo "Pipeline finished."
