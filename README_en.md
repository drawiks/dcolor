<div align="center">
    <h1>🎨 dcolor</h1>
    <img height="20" alt="Python 3.7+" src="https://img.shields.io/badge/python-3.7+-blue">
    <img height="20" alt="License MIT" src="https://img.shields.io/badge/license-MIT-green">
    <img height="20" alt="Status" src="https://img.shields.io/badge/status-stable-brightgreen">
    <p><strong>dcolor</strong> — colored terminal output with hex/rgb support</p>
    <blockquote>(─‿‿─)</blockquote>
</div>

---

```
     ____
    / __ \ ______ ____   / /____  _____
   / / / // ____// __ \ / // __ \/ ___/
  / /_/ // /____/ /_/ // // /_/ / /
 /_____/ \____/ \____//_/ \____/_/

```

## **📦 installation**

```bash
pip install dcolor-drawiks
```

---

## **📑 quick start**

```python
from dcolor import color

print(color("hello!", "#ff0000"))
print(color("hello!", (255, 0, 0)))
print(color("hello!", "red"))
print(color("hello!", "#ff0000", "bold", "underline"))
```

---

## **🧩 features**

- 🎨 **hex colors** — `"#ff0000"` or `"#f00"`
- 🌈 **rgb colors** — `(255, 0, 0)`
- 🏷️ **named colors** — `"red"`, `"cyan"`, `"orange"`...
- ✨ **styles** — `bold`, `italic`, `underline`, `strike`, `dim`, `blink`
- 🚫 **no dependencies** — stdlib only

---

## **📖 usage**

### hex color

```python
from dcolor import color

print(color("error", "#ff0000"))
print(color("success", "#00ff00"))
print(color("info", "#3b82f6"))
```

short hex also works:
```python
print(color("text", "#f00"))  # same as #ff0000
```

### rgb color

```python
print(color("text", (255, 165, 0)))
```

### named colors

```python
print(color("text", "red"))
print(color("text", "cyan"))
print(color("text", "orange"))
```

available names: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `grey`, `orange`, `pink`, `purple`, `brown`, `lime`, `teal`

### styles

```python
print(color("text", "red", "bold"))
print(color("text", "#ff0000", "bold", "underline"))
print(color("text", "cyan", "italic", "strike"))
```

available styles: `bold`, `dim`, `italic`, `underline`, `blink`, `strike`

### style only (no color)

```python
print(color("text", None, "bold"))
print(color("text", None, "underline", "italic"))
```

### strip ansi codes

```python
from dcolor import strip

raw = color("hello", "#ff0000", "bold")
clean = strip(raw)  # "hello"
```

---

## **💡 examples**

```python
from dcolor import color

print(color("[ERROR]",   "#ff4444", "bold"), "something went wrong")
print(color("[SUCCESS]", "#44ff44", "bold"), "everything is fine")
print(color("[WARN]",    "#ffaa00", "bold"), "watch out")
print(color("[INFO]",    "#888888"),         "just fyi")
```

### use in dlogger

```python
from dlogger import logger
from dcolor import color

logger.info(color("payment received", "#44ff44", "bold"))
logger.error(color("connection failed", "#ff4444"))
```

---

## **📜 license**
[MIT](LICENSE)
