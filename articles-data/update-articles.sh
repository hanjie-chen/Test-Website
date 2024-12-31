#!/bin/sh

GIT_LOG="/var/log/personal-website/articles-sync.log"  # 更新名称
REPO_BRANCH="${REPO_BRANCH:-main}"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [SYNC] $1" >> "$GIT_LOG"
}

log_message "Starting articles synchronization"

# 切换到仓库目录
cd /articles-data || {
    log_message "Failed to change directory to /articles-data"
    exit 1
}

# 执行 git pull
if /usr/bin/git pull origin "$REPO_BRANCH" >> "$GIT_LOG 2>&1"; then
    log_message "Git pull successful"
else
    log_message "Git pull failed"
    exit 1
fi

log_message "Articles synchronization completed"
echo "----------------------------------------" >> "$GIT_LOG"
