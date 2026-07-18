# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Structure

Project Euler solutions, one `pNNN/` directory per problem (zero-padded, e.g. `p001/`, `p237/`):

- `pNNN.ipynb` — primary deliverable: problem statement, explanation, solution code as markdown/code cells.
- `pNNN.py` — optional standalone mirror with a `pNNN(...)` function and `if __name__ == '__main__':` block (see `p003/p003.py`). Not every problem has one.
- Occasionally a local helper module used only by that problem (e.g. `p170/dlx.py`).

No shared package structure, test runner, linter, or CI. Nothing imports across `pNNN/` directories. Root `prime.py` is unused by current solutions — prefer `sympy` (`primerange`, `isprime`, `factorint`) for prime-related needs instead.

## Environment

`uv` manages dependencies via `pyproject.toml`/`uv.lock`.

- `uv sync` — install
- `uv run python pNNN/pNNN.py` — run a solution script
- `uv run jupyter lab` — edit a notebook
- `uv add <package>` — add a dependency (repo-wide, not per-problem)

`jupyterlab` is pinned `<4.6`: 4.6+ bundles a `@jupyter/ydoc` version incompatible with `jupyter-collaboration`'s prebuilt extension. Don't bump without checking upstream compatibility.

## Live kernel access via MCP

`jupyter-mcp-server` is registered as the `jupyter` MCP server (local scope, this project only), giving direct tool access to a running Jupyter kernel — `execute_code`, `execute_cell`, `use_notebook`, `read_cell`, etc. Setup/run instructions are in `README.md`. Requires a JupyterLab server already running at the configured `JUPYTER_URL`; if tools fail to connect, that server probably isn't up.

## Conventions

- New problem: `pNNN/pNNN.ipynb` with markdown cell (title + link to `https://projecteuler.net/problem=NNN`), markdown cell (problem description), then alternating markdown/code cells per solution approach (brute force first, then optimized).
- Common idioms already in use: `functools.cache`/`lru_cache`, `itertools.count`/`product`/`permutations`/`combinations`, `time.time()` for timing, `dataclasses` for small structured state.

## Git

Commit messages follow `P<NNN>` (no leading zeros), merged via PR (e.g. `P240 (#45)`).
