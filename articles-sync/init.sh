#!/bin/sh
set -e

ARTICLES_DIR="/articles-data"
GIT_LOG="/var/log/personal-website/articles-sync.log"
CROND_LOG="/var/log/personal-website/crond.log"
GITHUB_REPO="${GITHUB_REPO:-https://github.com/hanjie-chen/PersonalArticles.git}"
REPO_BRANCH="${REPO_BRANCH:-main}"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INIT] $1" | tee -a "$GIT_LOG"
}

# 确保日志目录存在
for log_file in "$GIT_LOG" "$CROND_LOG"; do
    if [ ! -d "$(dirname "$log_file")" ]; then
        mkdir -p "$(dirname "$log_file")"
        touch "$log_file"
        chmod 644 "$log_file"
    fi
done

# 检查目录是否为空
if [ -z "$(ls -A $ARTICLES_DIR)" ]; then
    log_message "Initializing articles directory..."
    git clone "$GITHUB_REPO" -b "$REPO_BRANCH" .
    log_message "Repository cloned successfully"
else
    log_message "Articles directory exists, performing update..."
    # 执行更新脚本
    /usr/local/bin/update-articles.sh
fi

# 设置定时任务
echo "0 16 * * * /usr/local/bin/update-articles.sh >> $GIT_LOG 2>&1" >> /etc/crontabs/root
echo "0 2 * * * /usr/sbin/logrotate /etc/logrotate.d/personal-website" >> /etc/crontabs/root

# 启动 crond 在后台
crond -b -L "$CROND_LOG" -l 6

# 使用 tail 作为前台进程
exec tail -f "$GIT_LOG" "$CROND_LOG"