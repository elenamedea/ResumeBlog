"""Color palettes for the light and dark themes.

Text-role colors (headings, links, bold accents) meet WCAG AA contrast
(>= 4.5:1) against their backgrounds; the decorative brand purple
#d891ef is reserved for borders, button fills, and image frames, where
contrast requirements are looser. style.css consumes these values as
CSS custom properties — see css_variables().
"""

LIGHT = {
    "bg": "#f7f4f5",
    "bg_secondary": "#f9edfd",
    "bg_secondary_hover": "#f3dafb",
    "text": "#0a0a0a",
    "text_muted": "rgba(10, 10, 10, 0.6)",
    "accent": "#8e24aa",  # headings, links, bold text — 6.4:1 on bg (AA)
    "accent_hover": "#6a1b9a",
    "brand": "#d891ef",
    "brand_hover": "#c472e6",
    "btn_text": "#0a0a0a",
    "btn_text_hover": "#ffffff",
    "shadow": "rgba(216, 145, 239, 0.2)",
}

DARK = {
    "bg": "#1a1523",
    "bg_secondary": "#281f33",
    "bg_secondary_hover": "#322741",
    "text": "#ece7f0",
    "text_muted": "rgba(236, 231, 240, 0.65)",
    "accent": "#d891ef",  # headings, links, bold text — 7.8:1 on bg (AAA)
    "accent_hover": "#e5b3f5",
    "brand": "#d891ef",
    "brand_hover": "#e5b3f5",
    "btn_text": "#1a1523",
    "btn_text_hover": "#1a1523",
    "shadow": "rgba(216, 145, 239, 0.25)",
}


def css_variables(theme: dict) -> str:
    """Renders a palette dict as a :root CSS custom-properties block."""
    variables = "\n".join(
        f"    --{key.replace('_', '-')}: {value};" for key, value in theme.items()
    )
    return f":root {{\n{variables}\n}}\n"
