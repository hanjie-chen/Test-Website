# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# install git and cron
RUN apt-get update && \
    apt-get install -y git cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create log directory
RUN mkdir -p /var/log/personal-website

# set web app directory
WORKDIR /app

# 复制requirements.txt
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# clone 文章
RUN git clone https://github.com/hanjie-chen/PersonalArticles.git /articles-data

# copy shell scripts and give execute permision
COPY update-articles.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh

# 暴露端口（Flask默认使用5000端口）
EXPOSE 5000

# 启动命令
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
