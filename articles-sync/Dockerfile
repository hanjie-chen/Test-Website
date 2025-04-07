FROM alpine:3.19

# define the args for the user/group IDs, can pass these in compose.yml or docker run command
ARG USER_ID=1000
ARG GROUP_ID=1000

# install git, dcron, logrotate
RUN apk add --no-cache git dcron logrotate

# create a group(appgroup) and user(appuser) with args
RUN addgroup -g ${GROUP_ID} -S appgroup && \
    adduser -u ${USER_ID} -S appuser -G appgroup

# create log directory and log file, change the files owner to appuser
RUN mkdir -p /var/log/personal-website && \
    touch /var/log/personal-website/{articles-sync,crond}.log &&\
    chown -R appuser:appgroup /var/log/personal-website/*.log

# create logrotate dir and copy file
COPY logrotate.conf /etc/logrotate.d/personal-website

WORKDIR /articles-data

# copy the scripts, provide the permission, and set cron jobs
COPY update-articles.sh init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh && \
    chmod +x /usr/local/bin/init.sh

ENTRYPOINT [ "/usr/local/bin/init.sh" ]