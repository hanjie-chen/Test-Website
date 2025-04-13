#!/bin/sh
set -e

ARTICLES_DIR="/articles-data"
GIT_LOG="/var/log/personal-website/articles-sync.log"
CROND_LOG="/var/log/personal-website/crond.log"
GITHUB_REPO="${GITHUB_REPO:-https://github.com/hanjie-chen/PersonalArticles.git}"
REPO_BRANCH="${REPO_BRANCH:-main}"

# record the time
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INIT] $1" | tee -a "$GIT_LOG"
}
# record the repo and branch message
log_message "Using GITHUB_REPO: $GITHUB_REPO"
log_message "Using REPO_BRANCH: $REPO_BRANCH"

# confirm the log dir and files exist
for log_file in "$GIT_LOG" "$CROND_LOG"; do
    if [ ! -d "$(dirname "$log_file")" ]; then
        mkdir -p "$(dirname "$log_file")"
    fi
    if [ ! -f "$log_file" ]; then
        touch "$log_file"
        chmod 644 "$log_file"
    fi
done

# initial the repo or update the repo
if [ -z "$(ls -A $ARTICLES_DIR)" ]; then
    log_message "Initializing articles directory..."
    if ! git clone "$GITHUB_REPO" -b "$REPO_BRANCH" "$ARTICLES_DIR"; then
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

# use > and here document, make sure the crontab file is overwritten
cat << EOF > /etc/crontabs/root
0 16 * * * /usr/local/bin/update-articles.sh >> /var/log/personal-website/articles-sync.log 2>&1
0 2 * * * /usr/sbin/logrotate /etc/logrotate.d/personal-website
EOF

# 设置 umask
umask 022

# set crond as main process
exec crond -f -L "$CROND_LOG" -l 6