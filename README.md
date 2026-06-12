# 🐝 Spelling Bee but French

Le [Spelling Bee du New York Times](https://www.nytimes.com/puzzles/spelling-bee), mais en français.

**▶ Jouer : [needlenosepliers.github.io/SpellingBee](https://needlenosepliers.github.io/SpellingBee/)**

Ou scannez pour installer sur votre téléphone :

![QR code d'installation](installer-qr.png)

Sur **Android**, le navigateur propose « Installer l'application ». Sur **iPhone**,
ouvrez le lien dans Safari puis Partager → « Sur l'écran d'accueil ». Dans les deux
cas le jeu fonctionne ensuite sans connexion.

- **Une grille par jour** : les 7 lettres changent chaque jour à minuit (heure de l'appareil).
- **151 000 mots français** acceptés (toutes conjugaisons, sans accents), intégrés dans la page.
- **100 % hors ligne** : tout tient dans `index.html`, aucune connexion requise pour jouer.
- **Progression mémorisée** sur l'appareil (mots trouvés, score, série de jours).

## Règles

Formez des mots d'au moins **4 lettres** contenant la **lettre centrale**. Les lettres
peuvent être réutilisées. Un mot de 4 lettres vaut 1 point, les plus longs 1 point par
lettre, et un **pangramme** (les 7 lettres) rapporte 7 points bonus.

## Développement

`scripts/construire_dico.py` régénère le dictionnaire intégré à partir de
[an-array-of-french-words](https://github.com/words/an-array-of-french-words).
