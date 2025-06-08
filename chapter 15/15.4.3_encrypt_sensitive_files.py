# Encrypt with gpg
gpg -c credentials.json   # prompt for passphrase
gpg -d credentials.json.gpg > credentials.json
# Automate decrypt in CI only.
