
from dash import Dash
from pathlib import Path

# after building app
html_str = app.index()
Path("reports/figures/dashboard.html").write_text(html_str)
