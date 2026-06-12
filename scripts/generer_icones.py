# Génère les icônes PNG de l'application (192 et 512 px) et le QR code
# d'installation pointant vers le site GitHub Pages.

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent.parent
URL = "https://needlenosepliers.github.io/SpellingBee/"
JAUNE = (247, 218, 33)
NOIR = (26, 26, 26)


def icone(taille: int) -> Image.Image:
    e = 4  # surechantillonnage pour des bords lisses
    t = taille * e
    img = Image.new("RGBA", (t, t), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, t - 1, t - 1], radius=int(t * 0.19), fill=JAUNE)
    # hexagone pointe en haut, centre (t/2, t/2)
    cx, cy, r = t / 2, t / 2, t * 0.31
    pts = [(cx, cy - r), (cx + r * 0.866, cy - r / 2), (cx + r * 0.866, cy + r / 2),
           (cx, cy + r), (cx - r * 0.866, cy + r / 2), (cx - r * 0.866, cy - r / 2)]
    d.polygon(pts, fill=NOIR)
    police = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(t * 0.34))
    d.text((cx, cy), "B", font=police, fill=JAUNE, anchor="mm")
    return img.resize((taille, taille), Image.LANCZOS)


for taille in (192, 512):
    icone(taille).save(RACINE / f"icone-{taille}.png")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=3, box_size=12)
qr.add_data(URL)
img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img_qr.save(RACINE / "installer-qr.png")
print("icone-192.png, icone-512.png et installer-qr.png générés")
