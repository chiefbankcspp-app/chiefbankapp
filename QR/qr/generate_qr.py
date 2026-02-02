import qrcode
import os

BASE_URL = "https://YOUR_USERNAME.github.io/app-download-qr/"

campaigns = {
    "main": "",
    "poster": "?src=poster",
    "facebook": "?src=facebook",
    "branch": "?src=branch"
}

os.makedirs("output", exist_ok=True)

for name, param in campaigns.items():
    qr = qrcode.make(BASE_URL + param)
    qr.save(f"output/{name}.png")

print("Chief Mobile Bank QR codes generated successfully.")
