Bot Discord minimal (Python)

Prérequis : Python 3.10+, crée un environnement virtuel.

Installation :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Édite .env et colle ton token
```

Lancer le bot :

```bash
python bot.py
```

Commandes disponibles :
- `!ping` → répond `Pong!`

Notes :
- Le token doit rester secret.
- Active l'intent `Message Content` dans l'interface développeur si nécessaire.
