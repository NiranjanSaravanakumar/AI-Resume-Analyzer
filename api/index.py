import sys
import os

# ---------------------------------------------------------------------------
# Ensure backend/ is on sys.path so `app` package and `config` module resolve
# ---------------------------------------------------------------------------
_backend_dir = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, os.path.abspath(_backend_dir))

# pyright: ignore [reportMissingImports]
from app import create_app

# `app` must be module-level for Vercel's Python runtime to find the WSGI callable
app = create_app()

# Vercel also accepts `handler` as an alias — expose both for compatibility
handler = app
