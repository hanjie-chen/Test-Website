FROM alpine:3.19

# install git and dcron
RUN apk add --no-cache git dcron logrotate

# create log directory and log file, set the log file permission
RUN mkdir -p /var/log/personal-website && \
    touch /var/log/personal-website/{articles-sync,crond}.log &&\
    chmod 644 /var/log/personal-website/*.log

# create logrotate dir and copy file
COPY logrotate.conf /etc/logrotate.d/personal-website

WORKDIR /articles-data

# copy the scripts, provide the permission, and set cron jobs
COPY update-articles.sh init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh && \
    chmod +x /usr/local/bin/init.sh

ENTRYPOINT [ "/usr/local/bin/init.sh" ]