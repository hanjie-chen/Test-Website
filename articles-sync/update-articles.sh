#!/bin/sh

ARTICLES_DIR="${SOURCE_ARTICLES_DIRECTORY:-/articles/src}"
REPO_BRANCH="${REPO_BRANCH:-main}"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [SYNC] $1"
}

echo "----------------------------------------"
log_message "Starting articles synchronization"
log_message "Using REPO_BRANCH: $REPO_BRANCH"

# go to articles dir
cd "$ARTICLES_DIR" || {
    log_message "Failed to change directory to /articles/src"
    exit 1
}

# check if it is a git repo
if [ ! -d ".git" ]; then
    log_message "/articles/src is not a git repository"
    exit 1
fi

# 执行 git pull
if /usr/bin/git pull origin "$REPO_BRANCH"; then
    log_message "Git pull successful"
else
    log_message "Git pull failed with exit code $?"
    exit 1
fi

log_message "Articles synchronization completed"
echo "----------------------------------------"
