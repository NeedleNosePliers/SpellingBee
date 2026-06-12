# Construit le dictionnaire intégré de index.html à partir d'une liste
# de mots français complète (toutes formes conjuguées incluses).
#
# Source : https://github.com/words/an-array-of-french-words (~336 000 mots)
# Filtres : 4 à 15 lettres, uniquement a-z après normalisation (accents
# retirés, oe/ae décomposés), au plus 7 lettres distinctes (un mot avec
# plus de 7 lettres uniques ne peut jamais être valide dans une grille).
#
# Usage : python scripts/construire_dico.py %TEMP%\mots_fr.json

import json
import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
HTML = RACINE / "index.html"
MARQUEUR = "__GROS_DICO__"


def normaliser(mot: str) -> str:
    mot = mot.lower().replace("œ", "oe").replace("æ", "ae")
    mot = unicodedata.normalize("NFD", mot)
    return "".join(c for c in mot if not unicodedata.combining(c))


def construire(source: Path) -> list[str]:
    brut = json.loads(source.read_text(encoding="utf-8"))
    valide = re.compile(r"^[a-z]{4,15}$")
    mots = set()
    for m in brut:
        n = normaliser(m)
        if valide.match(n) and len(set(n)) <= 7:
            mots.add(n)
    return sorted(mots)


def injecter(mots: list[str]) -> None:
    contenu = HTML.read_text(encoding="utf-8")
    if MARQUEUR not in contenu:
        sys.exit("Marqueur __GROS_DICO__ introuvable dans index.html — déjà injecté ?")
    contenu = contenu.replace(MARQUEUR, " ".join(mots), 1)
    HTML.write_text(contenu, encoding="utf-8")


if __name__ == "__main__":
    source = Path(sys.argv[1])
    mots = construire(source)
    injecter(mots)
    print(f"{len(mots)} mots injectés dans {HTML} "
          f"({HTML.stat().st_size / 1_000_000:.1f} Mo)")
