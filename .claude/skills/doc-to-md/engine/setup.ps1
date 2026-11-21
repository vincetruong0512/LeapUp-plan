# One-time setup for /doc-to-md: isolated venv at .tools/convert (gitignored via .tools/).
# Usage (from repo root):  powershell -ExecutionPolicy Bypass -File .claude/skills/doc-to-md/engine/setup.ps1
$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')
$venv = Join-Path $root '.tools\convert'
$req  = Join-Path $PSScriptRoot 'requirements.txt'
$env:UV_CACHE_DIR = Join-Path $root '.tools\uv-cache'

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) { throw 'uv not found on PATH - install from https://docs.astral.sh/uv/' }
if (-not (Test-Path (Join-Path $venv 'Scripts\python.exe'))) { uv venv $venv --python 3.13 }
uv pip install --python (Join-Path $venv 'Scripts\python.exe') -r $req

# Functional probe, not just import: an empty markitdown 0.0.1a1 package passes `import markitdown`
# but has no MarkItDown class (lesson from BA-Kit /reverse-doc).
& (Join-Path $venv 'Scripts\python.exe') -c "from markitdown import MarkItDown; import docx, openpyxl, pptx, pymupdf; print('doc-to-md engine OK')"
if ($LASTEXITCODE -ne 0) { throw 'Functional probe failed' }
