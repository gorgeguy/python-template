# python-template

Python project template with batteries included.

## What's included

| File | Purpose |
|------|---------|
| `pyproject.toml` | Package config, ruff rules, pyright, pytest, coverage |
| `.pre-commit-config.yaml` | ruff format/lint + pylint W0621 (name shadowing) |
| `CLAUDE.md` | Agent instructions — copy to new projects |
| `Makefile` | `make install`, `make ci`, `make test-cov`, etc. |
| `.github/workflows/ci.yml` | GitHub Actions: lint, format, typecheck, test |
| `.vscode/settings.json` | Format-on-save, ruff integration |
| `.editorconfig` | Consistent indentation across editors |
| `src/` layout | PEP 621 src layout with `py.typed` marker |

## Usage

### Starting a new project

```bash
# 1. Copy the template
cp -r ~/g/gorgeguy/python-template ~/g/myorg/my-new-project
cd ~/g/myorg/my-new-project

# 2. Reinitialize git
rm -rf .git && git init

# 3. Rename the package
mv src/mypackage src/yourpackage
# Update "mypackage" references in pyproject.toml, src/yourpackage/__init__.py, tests/

# 4. Install
make install

# 5. Customize CLAUDE.md "What This Is" section
```

### Ruff rule selection rationale

**Core** (catch real bugs and enforce consistency):
`E` `F` `I` `B` `UP` `C4` `RUF` `ARG` `SIM` `A`

**Safety** (prevent runtime issues):
`BLE` (blind exceptions), `DTZ` (naive datetimes), `TCH` (type-checking imports), `TRY400` (logger.exception)

**Quality** (maintain readability):
`D417` (docstring completeness), `FURB` (modern idioms), `PLR0912` (complexity)

**Via pylint pre-commit** (not available in ruff):
`W0621` (redefined-outer-name)

### Rules deliberately excluded

| Rule | Why |
|------|-----|
| `FBT` | Fights Typer/framework conventions (boolean params) |
| `T20` | CLIs legitimately print to stdout |
| `S` | High false-positive rate for non-web projects |
| `PLR2004` | Magic value detection too noisy for numeric code |
| `PLC0415` | Deferred imports are an intentional pattern |
| `D` (full) | Too heavy — `D417` alone catches real drift without requiring docstrings everywhere |
