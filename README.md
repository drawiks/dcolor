<div align="center">
    <h1>🎨 dcolor</h1>
    <img height="20" alt="Python 3.7+" src="https://img.shields.io/badge/python-3.7+-blue">
    <img height="20" alt="License MIT" src="https://img.shields.io/badge/license-MIT-green">
    <img height="20" alt="Status" src="https://img.shields.io/badge/status-stable-brightgreen">
    <p><strong>dcolor</strong> — цветной вывод в терминал с поддержкой hex/rgb</p>
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

## **📦 установка**

```bash
pip install dcolor-drawiks
```

---

## **📑 быстрый старт**

```python
from dcolor import color

print(color("привет!", "#ff0000"))
print(color("привет!", (255, 0, 0)))
print(color("привет!", "red"))
print(color("привет!", "#ff0000", "bold", "underline"))
```

---

## **🧩 возможности**

- 🎨 **hex цвета** — `"#ff0000"` или `"#f00"`
- 🌈 **rgb цвета** — `(255, 0, 0)`
- 🏷️ **именованные цвета** — `"red"`, `"cyan"`, `"orange"`...
- ✨ **стили** — `bold`, `italic`, `underline`, `strike`, `dim`, `blink`
- 🚫 **без зависимостей** — только stdlib

---

## **📖 использование**

### hex цвет

```python
from dcolor import color

print(color("ошибка", "#ff0000"))
print(color("успех", "#00ff00"))
print(color("инфо", "#3b82f6"))
```

короткий hex тоже работает:
```python
print(color("текст", "#f00"))  # то же что и #ff0000
```

### rgb цвет

```python
print(color("текст", (255, 165, 0)))
```

### именованные цвета

```python
print(color("текст", "red"))
print(color("текст", "cyan"))
print(color("текст", "orange"))
```

доступные имена: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `grey`, `orange`, `pink`, `purple`, `brown`, `lime`, `teal`

### стили

```python
print(color("текст", "red", "bold"))
print(color("текст", "#ff0000", "bold", "underline"))
print(color("текст", "cyan", "italic", "strike"))
```

доступные стили: `bold`, `dim`, `italic`, `underline`, `blink`, `strike`

### только стиль (без цвета)

```python
print(color("текст", None, "bold"))
print(color("текст", None, "underline", "italic"))
```

### убрать ansi коды

```python
from dcolor import strip

raw = color("привет", "#ff0000", "bold")
clean = strip(raw)  # "привет"
```

---

## **💡 примеры**

```python
from dcolor import color

print(color("[ERROR]",   "#ff4444", "bold"), "что-то пошло не так")
print(color("[SUCCESS]", "#44ff44", "bold"), "всё хорошо")
print(color("[WARN]",    "#ffaa00", "bold"), "осторожно")
print(color("[INFO]",    "#888888"),         "просто инфо")
```

### использование в dlogger

```python
from dlogger import logger
from dcolor import color

logger.info(color("платёж получен", "#44ff44", "bold"))
logger.error(color("соединение потеряно", "#ff4444"))
```

---

## **📜 лицензия**
[MIT](LICENSE)