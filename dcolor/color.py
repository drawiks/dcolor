
import re
import sys
from typing import Union, Tuple, Optional

ColorInput = Union[str, Tuple[int, int, int], int]
ColorValue = Union[Tuple[int, int, int], int]

NAMED_COLORS = {
    "black": (0,   0,   0),
    "red": (255, 0,   0),
    "green": (0,   255, 0),
    "yellow": (255, 255, 0),
    "blue": (0,   0,   255),
    "magenta": (255, 0,   255),
    "cyan": (0,   255, 255),
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "orange": (255, 165, 0),
    "pink": (255, 105, 180),
    "purple": (148, 0,   211),
    "brown": (139, 69,  19),
    "lime": (50,  205, 50),
    "teal": (0,   128, 128),
}

STYLES = {
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "strike": "\033[9m",
}

RESET = "\033[0m"
RE_ANSI = re.compile(r"\033\[[0-9;]*m")

def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r, g, b

def _is_color(c: ColorInput) -> bool:
    if c is None:
        return False
    if isinstance(c, tuple):
        return len(c) == 3 and all(isinstance(x, int) for x in c)
    if isinstance(c, int):
        return 0 <= c <= 255
    if isinstance(c, str):
        if c.startswith("#"):
            return True
        if c.lower() in NAMED_COLORS:
            return True
    return False

def _resolve_color(c: Optional[ColorInput]) -> Optional[ColorValue]:
    if c is None:
        return None
    if isinstance(c, tuple):
        return c
    if isinstance(c, int):
        if 0 <= c <= 255:
            return c
        raise ValueError(f"color index must be 0-255, got {c}")
    if isinstance(c, str):
        if c.startswith("#"):
            return _hex_to_rgb(c)
        if c.lower() in NAMED_COLORS:
            return NAMED_COLORS[c.lower()]
    raise ValueError(f"unknown color: '{c}'. use hex '#ff0000', rgb tuple, 256-color (0-255) or a named color.")

def color(
    text: str,
    fg: Optional[ColorInput] = None,
    *styles: str,
    bg: Optional[ColorInput] = None,
    force: bool = False
) -> str:
    if not force and not sys.stdout.isatty():
        return text

    result: str = ""

    for s in styles:
        if s in STYLES:
            result += STYLES[s]
        else:
            raise ValueError(f"unknown style: '{s}'. available: {', '.join(STYLES)}")

    fg_val = _resolve_color(fg)
    if fg_val is not None:
        if isinstance(fg_val, int):
            result += f"\033[38;5;{fg_val}m"
        else:
            r, g, b = fg_val
            result += f"\033[38;2;{r};{g};{b}m"

    bg_val = _resolve_color(bg)
    if bg_val is not None:
        if isinstance(bg_val, int):
            result += f"\033[48;5;{bg_val}m"
        else:
            r, g, b = bg_val
            result += f"\033[48;2;{r};{g};{b}m"

    result += text + RESET
    return result

def strip(text: str) -> str:
    return RE_ANSI.sub("", text)
