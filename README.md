# Hilarious Greeter & Mad Libs MCP Server

This project provides a simple Model Context Protocol (MCP) server with two fun tools designed to be used with clients like Claude Desktop:

1.  **`greeting`**: Returns a random, hilariously over-the-top greeting.
2.  **`mad_libs`**: Generates a funny Mad Libs story based on user-provided words.

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Python package installer and virtual environment manager)

## Setup Instructions

1.  **Install `uv`:**
    If you haven't already, install `uv` by running the following in your terminal:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Restart your terminal or source the environment file as prompted
    # e.g., for zsh/bash: source $HOME/.local/bin/env
    ```

2.  **Clone or Download:**
    Get the project files (specifically `greeting_server.py`) onto your local machine.

3.  **Navigate to Project Directory:**
    Open your terminal and change into the project directory:

    ```bash
    cd path/to/hello-world-mcp
    ```

4.  **Initialize Project & Environment:**
    Set up the Python environment and install dependencies:

    ```bash
    # Initialize the project (if you haven't already)
    uv init --quiet

    # Create and activate a virtual environment
    uv venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`

    # Install the MCP library
    uv add "mcp[cli]"
    ```

## Connecting to Claude Desktop

1.  **Find Claude Desktop Configuration:**

    - Locate the configuration file. On **macOS**, it's typically:
      `~/Library/Application Support/Claude/claude_desktop_config.json`
    - On **Windows**, it might be in `%APPDATA%\Claude\claude_desktop_config.json` or similar.
    - If the `Claude` directory or the `.json` file doesn't exist, you may need to create them.

2.  **Find Absolute Paths:**

    - **Project Path:** In your terminal (while in the project directory), run `pwd` (macOS/Linux) or `cd` (Windows) to get the full, absolute path to the `hello-world-mcp` directory.
    - **`uv` Path:** In your terminal, run `which uv` (macOS/Linux) or `where uv` (Windows) to get the full, absolute path to the `uv` executable.

3.  **Edit Configuration File:**
    Open `claude_desktop_config.json` in a text editor and add the following structure within the main JSON object. If `mcpServers` already exists, add `"hilarious_greeter"` inside it.

    ```json
    {
      "mcpServers": {
        "hilarious_greeter": {
          "command": "/YOUR/ABSOLUTE/PATH/TO/uv", // <-- Replace with the actual path from 'which uv'
          "args": [
            "--directory",
            "/YOUR/ABSOLUTE/PATH/TO/PROJECT/hello-world-mcp", // <-- Replace with actual path from 'pwd'
            "run",
            "greeting_server.py"
          ]
        }
        // You can add configurations for other servers here
      }
    }
    ```

    **Important:** Replace the placeholder paths with the actual absolute paths you found in the previous step.

4.  **Save and Restart:**
    Save the `claude_desktop_config.json` file and **completely quit and restart** Claude Desktop.

## Testing the Tools

After restarting Claude Desktop, you should be able to use the tools:

- **Greeting Tool:** Ask Claude "Give me a greeting" or "Say hello".
- **Mad Libs Tool:** Ask Claude "Tell me a mad libs story". Claude will then prompt you for the required words (adjectives, nouns, verbs, etc.).

Enjoy the hilarious interactions!

## Links

[Quickstart](https://modelcontextprotocol.io/quickstart/server)
[Python SDK](https://github.com/modelcontextprotocol/python-sdk)
