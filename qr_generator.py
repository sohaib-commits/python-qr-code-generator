import qrcode
from PIL import Image
import argparse
import os
from datetime import datetime

# ---------- CLI ARGUMENTS ----------
parser = argparse.ArgumentParser(description="QR Code Generator (CLI Tool)")
parser.add_argument("--data", required=True, help="Text or URL for QR code")
parser.add_argument("--color", default="black", help="QR color (default: black)")
parser.add_argument("--bg", default="white", help="Background color (default: white)")
parser.add_argument("--size", type=int, default=10, help="Box size (default: 10)")
parser.add_argument("--logo", help="Path to logo image (optional)")

args = parser.parse_args()

# ---------- QR SETUP ----------
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=args.size,
    border=4
)

qr.add_data(args.data)
qr.make(fit=True)

img = qr.make_image(
    fill_color=args.color,
    back_color=args.bg
).convert("RGBA")

# ---------- LOGO ADD ----------
if args.logo and os.path.exists(args.logo):
    logo = Image.open(args.logo).convert("RGBA")

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

print("QR code generated:", path)
