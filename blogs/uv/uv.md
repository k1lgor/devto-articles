---
title: Stop Using pip — Switch to uv in 5 Minutes
published: false
description: A hands-on guide to uv, the blazing-fast Python package manager that replaces pip, virtualenv, and pyenv all at once.
tags: "python, beginners, productivity, tutorial"
cover_image: null
canonical_url: null
series: "Modern Python Tooling"
---

---

### **_Introduction_**

If you write Python, you've used `pip`. It works — but it's slow, it has no built-in lockfile, and it doesn't manage Python versions. You end up juggling `pip`, `virtualenv`, `pyenv`, and maybe `pipenv` or `poetry` on top.

Meet `uv`: a single tool written in Rust that replaces all of them, and runs **10–100× faster** than pip. In this article we'll go from zero to a fully managed Python project in under 5 minutes.

---

### **_What is uv?_**

`uv` is an open-source Python package manager built by [Astral](https://astral.sh) — the same team behind the `ruff` linter. It speaks the same language as `pip` (PyPI, `requirements.txt`, `pyproject.toml`) but adds:

- ⚡ A global dependency cache — packages are never downloaded twice
- 🔒 A `uv.lock` lockfile for fully reproducible installs
- 🐍 Built-in Python version management (no more `pyenv`)
- 📦 A single binary with zero Python dependencies

---

### **_Installation_**

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or with pip (if you already have it):**

```bash
pip install uv
```

Verify it works:

```bash
uv --version
# uv 0.6.x
```

---

### **_Creating a New Project_**

Forget `mkdir myproject && cd myproject && python -m venv .venv && source .venv/bin/activate && pip install ...`. With `uv`:

```bash
uv init myproject
cd myproject
```

This creates:

```
myproject/
├── .python-version   # pins Python version
├── pyproject.toml    # project metadata + dependencies
├── README.md
└── hello.py
```

`uv` automatically picks the best available Python interpreter, or you can pin a specific one:

```bash
uv init myproject --python 3.12
```

---

### **_Adding Dependencies_**

Instead of `pip install requests`, run:

```bash
uv add requests
```

`uv` will:

1. Resolve the dependency
2. Install it into a local `.venv/`
3. Update `pyproject.toml` under `[project.dependencies]`
4. Regenerate `uv.lock` with the exact resolved version

Add a dev-only dependency (e.g. for testing):

```bash
uv add --dev pytest
```

Your `pyproject.toml` will now look like this:

```toml
[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0.0",
]
```

---

### **_Running Your Code_**

No need to activate the virtual environment manually. Use `uv run`:

```bash
uv run hello.py
uv run python -c "import requests; print(requests.__version__)"
uv run pytest
```

`uv run` ensures the right virtualenv and Python version are always used — even if you forget to activate it.

---

### **_Syncing the Environment_**

When you clone a project that uses `uv`, getting it running is one command:

```bash
uv sync
```

This reads `uv.lock` and installs exact versions of every dependency. No surprises.

To sync including dev dependencies:

```bash
uv sync --dev
```

---

### **_Migrating From pip_**

Already have a `requirements.txt`? Import it in seconds:

```bash
uv add -r requirements.txt
```

Coming from `poetry`? `uv` reads `pyproject.toml` natively — just swap the build backend and run `uv sync`.

---

### **_Speed Comparison_**

Here's what installing a typical data-science stack looks like:

| Tool  | Cold install | Warm install (cached) |
| ----- | ------------ | --------------------- |
| `pip` | ~45s         | ~30s                  |
| `uv`  | ~4s          | ~0.5s                 |

The difference is even more dramatic in CI pipelines where time is money.

---

### **_Cheat Sheet_**

```bash
# Project setup
uv init myproject          # new project
uv sync                    # install from uv.lock

# Dependencies
uv add requests            # add a dependency
uv add --dev pytest        # add a dev dependency
uv remove requests         # remove a dependency
uv lock --upgrade          # upgrade all deps + regenerate lockfile

# Running code
uv run script.py           # run with managed venv
uv run pytest              # run any tool

# Python versions
uv python install 3.12     # install a Python version
uv python list             # list available versions
uv python pin 3.11         # pin for this project
```

---

### **_Conclusion_**

`uv` is not just "pip but faster" — it's a complete rethinking of the Python developer experience. One tool. One lockfile. One command to go from clone to running. Give it 5 minutes and you won't go back.

In the next article, we'll dive deeper into `pyproject.toml` — the modern standard replacing `setup.py`, `requirements.txt`, and `Pipfile` all at once.

**_Thank you for reading_** 🧑‍💻

**_Stay tuned for more_** 🚀

✌️ and **_logout_**

<a href="https://www.buymeacoffee.com/k1lgor" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
</a>
