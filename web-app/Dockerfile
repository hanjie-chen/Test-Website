# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# set web app directory
WORKDIR /app

# 复制requirements.txt
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# product env used, dev env use bind mount, which define in the compose.yml
# COPY . .

# 暴露端口（Flask默认使用5000端口）
EXPOSE 5000

# 启动命令
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]