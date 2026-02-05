#!/bin/sh
set -e

ARTICLES_DIR="${SOURCE_ARTICLES_DIRECTORY:-/articles/src}"
GITHUB_REPO="${GITHUB_REPO:-https://github.com/hanjie-chen/PersonalArticles.git}"
REPO_BRANCH="${REPO_BRANCH:-main}"

# record the time
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INIT] $1"
}
# record the repo and branch message
log_message "Using GITHUB_REPO: $GITHUB_REPO"
log_message "Using REPO_BRANCH: $REPO_BRANCH"

# initial the repo or update the repo
if [ -z "$(ls -A "$ARTICLES_DIR")" ]; then
    log_message "Initializing articles directory..."
    cd "$ARTICLES_DIR"
    if ! git clone -b "$REPO_BRANCH" "$GITHUB_REPO" .; then
        log_message "Git clone failed"
        exit 1
    fi
    log_message "Repository cloned successfully"
else
    log_message "Articles directory exists, performing update..."
    if ! /usr/local/bin/update-articles.sh; then
        log_message "run update-articles.sh scripts failed"
        exit 1
    fi
fi

# Create a temporary crontab file
cat << EOF > /tmp/crontab
0 16 * * * /usr/local/bin/update-articles.sh
EOF

# Install crontab for appuser, then delete it
crontab /tmp/crontab
rm /tmp/crontab

# 设置 umask
umask 022

# set crond as main process
exec crond -f -L /dev/stdout -l 6
