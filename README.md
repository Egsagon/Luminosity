# Luminosity
Polybar module for settings the luminosity

Simple script writen in Python which spawns a window for setting the luminosity with the `xgamma` command on linux.

To use it with polybar, use :
```python
[module/Luminosity]
type = custom/script
exec = echo "Any icon you want"
tail = true
click-left = python3 /path/to/script.py
```

By adding the path and the icon / text you want.
