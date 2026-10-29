#!/bin/bash
# Activity 5: write the task lists and test results into index.html, then commit and push.
# Usage: update_index.sh <tasks output file> <test results file>
set -e

TASKS_FILE="$1"
TESTS_FILE="$2"
HTML_FILE="index.html"

# Lines between "ToDo Tasks:" and "Done Tasks:" (grep + sed)
TODO_TASKS=$(sed -n '/^ToDo Tasks:/,/^Done Tasks:/p' "$TASKS_FILE" | grep -v -e '^ToDo Tasks:' -e '^Done Tasks:' || true)
# Lines after "Done Tasks:" (awk)
DONE_TASKS=$(awk '/^Done Tasks:/{found=1; next} found' "$TASKS_FILE")
TEST_RESULTS=$(cat "$TESTS_FILE")

# Replace everything inside <pre id="ID">...</pre> with new content.
update_pre() {
  local id="$1"
  local content="$2"
  local file="$3"
  CONTENT="$content" perl -0pi -e 's|(<pre id="'"$id"'">).*?(</pre>)|$1$ENV{CONTENT}$2|s' "$file"
}

update_pre "todo" "$TODO_TASKS" "$HTML_FILE"
update_pre "done" "$DONE_TASKS" "$HTML_FILE"
update_pre "tests" "$TEST_RESULTS" "$HTML_FILE"

git config --global user.name "github-actions"
git config --global user.email "github-actions@users.noreply.github.com"
git add "$HTML_FILE"
git commit -m "Update index.html with tasks and test results (pushed by ${GITHUB_USER:-unknown})" || echo "No changes to commit"

# Set SKIP_PUSH=true to test locally without pushing.
if [ "${SKIP_PUSH:-false}" != "true" ]; then
  git push origin HEAD:main
fi
