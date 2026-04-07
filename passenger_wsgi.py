import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR / "myproject"

# Mirror manage.py so Passenger can resolve the nested Django package.
for path in (PROJECT_DIR, BASE_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Keep Passenger's entrypoint tiny and reuse Django's canonical WSGI module.
from myproject.wsgi import application

app = application
