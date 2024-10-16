#!CMD: docker-build-run -t Cerebrichan -p 25565:80

FROM ubuntu

USER 0

COPY src /web
COPY setup.sh /setup.sh
RUN bash setup.sh && rm setup.sh

#USER php-www-root
COPY run.sh /run.sh
CMD ["/bin/bash", "/run.sh"]
