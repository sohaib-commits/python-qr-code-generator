import qrcode
from PIL import Image
import os
from datetime import datetime

# ---------- USER INPUT ----------
data = input("Enter text or link: ").strip()
if not data:
    print("Error: input empty")
    exit()

fill_color = input("QR color (e.g. black, darkblue, red): ").strip() or "black"
back_color = input("Background color (e.g. white, yellow): ").strip() or "white"

try:
    box_size = int(input("Box size (recommended 8–12): ").strip())
except:
    box_size = 10

logo_path = input("Logo path (leave empty if none): ").strip()

# ---------- QR SETUP ----------
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=box_size,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

# ---------- LOGO ADD ----------
if logo_path and os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")

    qr_w, qr_h = img.size
    logo_size = qr_w // 4
    logo = logo.resize((logo_size, logo_size))

    pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
    img.paste(logo, pos, logo)

# ---------- SAVE ----------
os.makedirs("qr_codes", exist_ok=True)
filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
path = os.path.join("qr_codes", filename)
img.save(path)

print("Saved:", path)
