#!CMD: docker-build-run -t arch3rr/myrctf2024:verborgen-1.0.0 -p 8889:8888

FROM archlinux

USER 0

COPY flag.txt /root/.hidden_secrets.txt

COPY setup.sh /setup.sh
COPY srv /srv
RUN bash setup.sh && rm setup.sh


USER verborgen
CMD python /srv/flask/app.py
