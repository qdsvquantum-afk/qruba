project = "Qruba"
author = "QDSV / Qruba"
copyright = "2026, QDSV / Qruba"

extensions = [
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "Qruba Documentation"
html_baseurl = "https://qdsvquantum-afk.github.io/qruba/"
html_static_path = ["_static"]
html_theme_options = {
    "source_repository": "https://github.com/qdsvquantum-afk/qruba/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "#0f766e",
        "color-brand-content": "#0f766e",
    },
    "dark_css_variables": {
        "color-brand-primary": "#2dd4bf",
        "color-brand-content": "#2dd4bf",
    },
}
