FROM alpine:3.21

# define the args for the user/group IDs, can pass these in compose.yml or docker run command
ARG USER_ID=1000
ARG GROUP_ID=1000

# install git, dcron, logrotate
RUN apk add --no-cache git dcron logrotate

# create a group(appgroup) and user(appuser) with args
RUN addgroup -g ${GROUP_ID} -S appgroup && \
    adduser -u ${USER_ID} -S appuser -G appgroup

# create log directory, change the dir owner to appuser
RUN mkdir -p /var/log/personal-website && \
    chown appuser:appgroup /var/log/personal-website

# create logrotate dir and copy file
COPY logrotate.conf /etc/logrotate.d/personal-website

# create working dir and set permission to appuser
RUN mkdir -p /articles-data && chown appuser:appgroup /articles-data
WORKDIR /articles-data

# copy the scripts, provide the permission, and set cron jobs
COPY --chown=appuser:appgroup update-articles.sh init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh && \
    chmod +x /usr/local/bin/init.sh

# switch the non-root user to run the script
USER appuser

ENTRYPOINT [ "/usr/local/bin/init.sh" ]