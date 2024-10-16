FROM alpine

WORKDIR /rc_additions

ADD flag.txt /rc_additions/passwd.txt
RUN rm /rc_additions/passwd.txt
CMD sh -c "cat /rc_additions/passwd.txt"
