import requests

#https://api.ropro.io/generateVerificationToken.php
#https://api.ropro.io/verificationMetadata.php

cookie = input("Cookie: ")
userid = requests.get("https://users.roblox.com/v1/users/authenticated", cookies={'.ROBLOSECURITY': str(cookie)}).json()["id"]

game=requests.post("https://api.ropro.io/verificationMetadata.php").json()["universeId"])



requests.post(f"https://games.roblox.com/v1/games/{game}/favorites", cookies={'.ROBLOSECURITY': str(cookie)}, json={"isFavorited": True})
r=requests.post("https://api.ropro.io/generateVerificationToken.php", cookies={'.ROBLOSECURITY': str(cookie)}, json={"isFavorited": True}).json()
print(r)

# work in progress
