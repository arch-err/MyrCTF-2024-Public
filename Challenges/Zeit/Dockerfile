#!CMD: docker-build-run -t arch3rr/myrctf2024:zeit-1.0.1 -p 8888:8080

FROM archlinux/archlinux:latest

USER 0

COPY setup.sh /setup.sh
COPY srv /srv
COPY files /home/tod/files
COPY root /root

RUN bash setup.sh && rm setup.sh


USER tod
EXPOSE 80
CMD python /srv/flask/app.py
