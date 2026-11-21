# Mini MCP Server

A beginner-friendly implementation of a Model Context Protocol (MCP) server using Python and the MCP Python SDK.

## Overview

This project demonstrates how to build an MCP server that exposes tools, resources, and prompts to MCP-compatible AI applications.

## Features

- **Tools:** Perform operations such as addition and multiplication.
- **Resources:** Expose learning notes through a resource URI.
- **Prompts:** Provide reusable prompt templates for explaining MCP concepts.
- **Transport:** Uses STDIO for local communication.

## Project Structure

```text
mini-mcp-server/
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kushwaha-ashutosh/mini-mcp-server.git
cd mini-mcp-server
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python server.py
```

The server uses STDIO transport and is intended to be launched by an MCP client.

## Available Capabilities

### Tools

| Tool | Description |
|---|---|
| `add(a, b)` | Adds two numbers |
| `multiply(a, b)` | Multiplies two numbers |

### Resources

| URI | Description |
|---|---|
| `notes://welcome` | Returns introductory MCP notes |

### Prompts

| Prompt | Argument | Description |
|---|---|---|
| `explain_mcp` | `topic` | Generates a structured explanation of an MCP topic |

## Technologies

- Python
- Model Context Protocol (MCP)
- MCP Python SDK

## Learning Objectives

- Understand MCP architecture.
- Learn the difference between tools, resources, and prompts.
- Understand STDIO transport.
- Build MCP clients and connect them to servers.

## License

This project is open-source and available under the MIT License.