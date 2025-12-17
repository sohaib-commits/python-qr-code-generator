# Python QR Code Generator (CLI)

A command-line tool to generate QR codes with custom colors, size, and optional logo embedding.

## Features
- Generate QR codes from text or URL
- Custom QR color and background color
- Adjustable size
- Optional center logo
- Clean CLI interface using `argparse`

## Requirements
- Python 3.8+
- qrcode
- Pillow

### Install dependencies
You can install the required packages using:

```bash
pip install qrcode[pil] Pillow


## Usage

**Basic usage:**

```bash
python qr_generator.py --data "https://google.com"


With custom colors and size:

python qr_generator.py \
  --data "Hello World" \
  --color darkblue \
  --bg white \
  --size 12


With logo:

python qr_generator.py \
  --data "https://google.com" \
  --logo logo.png


Help command:

python qr_generator.py --help
