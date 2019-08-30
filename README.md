# python-hotkey-listener
Listen for global hotkey CTRL+C using `python` and `keyboard`.

# Install
pip install -r requirements.txt --find-links file:///tmp/packages

# Build executable: platform dependent
1. Install `pyinstaller`
``` bash
pip install pyinstaller
```
2. Build executable file
``` bash
pyinstaller --onefile index.py
```
3. You can find the executable in `dist/` or `build/` directory.
