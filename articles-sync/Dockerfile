FROM alpine:3.21

# define the args for the user/group IDs, can pass these in compose.yml or docker run command
ARG USER_ID=1000
ARG GROUP_ID=1000

# install git, dcron, tini
RUN apk add --no-cache git dcron tini

# create a group(appgroup) and user(appuser) with args
RUN addgroup -g ${GROUP_ID} -S appgroup && \
    adduser -u ${USER_ID} -S appuser -G appgroup

# create log directory, change the dir owner to appuser
RUN mkdir -p /var/log/personal-website && \
    chown appuser:appgroup /var/log/personal-website

# create working dir and set permission to appuser
RUN mkdir -p /articles/src && chown -R appuser:appgroup /articles
WORKDIR /articles/src

# copy the scripts, provide the permission, and set cron jobs
COPY --chown=appuser:appgroup update-articles.sh init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh && \
    chmod +x /usr/local/bin/init.sh

# let appuser have permission to run crontab, crond command
RUN chmod o+x /usr/bin/crontab &&\
    chmod u+s /usr/sbin/crond  &&\
    chmod o+x /usr/sbin/crond

# switch the non-root user to run the script
USER appuser

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/usr/local/bin/init.sh"]
