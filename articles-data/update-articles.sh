#!/bin/bash

LOG_FILE="${LOG_DIR}/git-pull.log"

# 记录时间
echo "=== Git pull started at $(date) ===" >> $LOG_FILE

# 切换到仓库目录
cd /articles-data

# 执行 git pull
/usr/bin/git pull origin main >> $LOG_FILE 2>&1

# 记录完成状态
echo "=== Git pull completed at $(date) ===" >> $LOG_FILE
echo "----------------------------------------" >> $LOG_FILE