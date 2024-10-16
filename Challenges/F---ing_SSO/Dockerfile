#!CMD: docker-build-run -t tod:dev -p 8888:8888

FROM archlinux

USER 0

COPY setup.sh /setup.sh
COPY srv /srv

RUN bash setup.sh && rm setup.sh

COPY flag.txt /flag.txt

USER u40036659
CMD python /srv/flask/app.py
