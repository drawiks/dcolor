from typing import Union, Tuple


NAMED_COLORS = {
    "black":   (0,   0,   0),
    "red":     (255, 0,   0),
    "green":   (0,   255, 0),
    "yellow":  (255, 255, 0),
    "blue":    (0,   0,   255),
    "magenta": (255, 0,   255),
    "cyan":    (0,   255, 255),
    "white":   (255, 255, 255),
    "grey":    (128, 128, 128),
    "orange":  (255, 165, 0),
    "pink":    (255, 105, 180),
    "purple":  (148, 0,   211),
    "brown":   (139, 69,  19),
    "lime":    (50,  205, 50),
    "teal":    (0,   128, 128),
}

STYLES = {
    "bold":      "\033[1m",
    "dim":       "\033[2m",
    "italic":    "\033[3m",
    "underline": "\033[4m",
    "blink":     "\033[5m",
    "strike":    "\033[9m",
}

RESET = "\033[0m"


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r, g, b


def _resolve_color(c: Union[str, Tuple[int, int, int]]) -> Tuple[int, int, int]:
    if isinstance(c, tuple):
        return c
    if c.startswith("#"):
        return _hex_to_rgb(c)
    if c.lower() in NAMED_COLORS:
        return NAMED_COLORS[c.lower()]
    raise ValueError(f"unknown color: '{c}'. use hex '#ff0000', rgb tuple or a named color.")


def color(
    text: str,
    fg: Union[str, Tuple[int, int, int]] = None,
    *styles: str
) -> str:
    result = ""

    for s in styles:
        if s in STYLES:
            result += STYLES[s]
        else:
            raise ValueError(f"unknown style: '{s}'. available: {', '.join(STYLES)}")

    if fg is not None:
        r, g, b = _resolve_color(fg)
        result += f"\033[38;2;{r};{g};{b}m"

    result += text + RESET
    return result


def strip(text: str) -> str:
    import re
    return re.sub(r"\033\[[0-9;]*m", "", text)
