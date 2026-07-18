# project-euler
Project Euler problems

## Setup

Dependencies are managed with [`uv`](https://docs.astral.sh/uv/):

```
uv sync
```

## Running a solution

```
uv run python pNNN/pNNN.py
```

## Working on a notebook

```
uv run jupyter lab
```

## Live kernel access for Claude Code (optional)

[`jupyter-mcp-server`](https://github.com/datalayer/jupyter-mcp-server) exposes a running Jupyter kernel to Claude Code as an MCP server, so it can execute code/cells directly instead of only editing `.ipynb` files as JSON.

1. Start JupyterLab with a fixed token, bound to localhost:

   ```
   uv run jupyter lab --no-browser --ip 127.0.0.1 --port 8888 --IdentityProvider.token <TOKEN>
   ```

2. Register the MCP server with Claude Code (run once per machine; `-s local` scopes it to this project only):

   ```
   claude mcp add jupyter -s local \
     -e JUPYTER_URL=http://127.0.0.1:8888 \
     -e JUPYTER_TOKEN=<TOKEN> \
     -e ALLOW_IMG_OUTPUT=true \
     -- uvx jupyter-mcp-server@latest
   ```

3. Restart the Claude Code session so it picks up the new MCP server. `/mcp` shows `jupyter` as connected.

The JupyterLab server must already be running at `JUPYTER_URL` before Claude Code can use the `jupyter` tools — if they fail to connect, start it first.
