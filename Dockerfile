# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制requirements.txt
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# 复制所有项目文件到容器中
COPY . .

# 暴露端口（Flask默认使用5000端口）
EXPOSE 5000

# 启动命令
CMD ["flask", "run", "--host=0.0.0.0"]
