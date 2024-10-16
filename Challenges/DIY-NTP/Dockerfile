#!CMD: docker-build-run -t arch3rr/myrctf2024:diy-ntp-1.0.0 -p 32123:321

FROM archlinux

USER 0

COPY src/DIY-NTP /DIY-NTP
COPY src/RunProgram.sh /RunProgram.sh
COPY flag.txt /flag.txt
#COPY setup.sh /setup.sh
#RUN bash setup.sh && rm setup.sh


CMD /RunProgram.sh
