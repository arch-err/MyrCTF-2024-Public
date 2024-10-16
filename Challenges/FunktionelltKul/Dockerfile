#!CMD: docker-build-run -t arch3rr/myrctf2024:funktionelltkul-1.0.0 -p 31337:1337

FROM archlinux

USER 0

COPY src/Funkiskul /Funkiskul
COPY src/RunProgram.sh /RunProgram.sh
#COPY setup.sh /setup.sh
#RUN bash setup.sh && rm setup.sh


CMD /RunProgram.sh
