@echo off
REM Example Windows runner
REM 1) Edit the two lines below, then double‑click this file.

set SRC_HTML=C:\temp\advantage_help
set OUT_DIR=%CD%\advantage-md

python convert_help_to_md.py --in "%SRC_HTML%" --out "%OUT_DIR%" --make-jsonl

echo.
echo Done. Output: %OUT_DIR%
pause
