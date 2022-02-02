FROM agaarbi/alpine-modified
COPY . /app

RUN mkdir -p app/logs

COPY root /var/spool/cron/crontabs/root
RUN chmod +x /app/main.py
CMD crond -l 2 -f