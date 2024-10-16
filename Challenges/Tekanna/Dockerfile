#!CMD: docker-build-run -t arch3rr/myrctf2024:tekanna-1.0.0 -p 8888:8888

FROM archlinux

USER 0

COPY setup.sh /setup.sh
COPY srv /srv
RUN bash setup.sh && rm setup.sh


USER teapot
CMD python /srv/flask/app.py
