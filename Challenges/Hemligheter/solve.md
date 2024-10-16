1. Notice the .git folder, realise this is a git-repo
2. `git log` and find the bad commit
3. Checkout that commit, steal the `key.txt` file
4. Go back to ***HEAD*** and use `sops --decrypt ...` to decrypt the secrets (the flag is in the alloyToken-secret)
5. Base64 the data values, get the flag
