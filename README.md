# MCP LangChain Integration

A demonstration project showcasing the integration of Model Context Protocol (MCP) servers with LangChain and LangGraph, enabling AI agents to interact with multiple specialized tools and services.

## Overview

This project demonstrates how to create and integrate MCP servers with LangChain to build powerful AI agents that can perform various tasks like mathematical calculations and weather queries. It uses the `langchain-mcp-adapters` library to bridge MCP servers with LangChain's agent framework.

## Features

- **Multi-Server MCP Integration**: Connect to multiple MCP servers simultaneously
- **Math Operations**: Mathematical calculations via a dedicated MCP server
- **Weather Service**: Weather information retrieval via HTTP-based MCP server
- **LangGraph Agent**: ReAct agent pattern for intelligent tool usage
- **Groq Integration**: Uses Groq's high-performance language models

## Architecture

The project consists of three main components:

1. **MCP Servers**:
   - `mathserver.py`: Provides mathematical operations (add, multiply) via stdio transport
   - `weather.py`: Provides weather information via HTTP transport

2. **Client Application**:
   - `client.py`: Main application that integrates MCP servers with LangChain

3. **Agent Framework**:
   - Uses LangGraph's ReAct agent for intelligent tool selection and execution

## Project Structure

```
mcplangchain/
├── client.py          # Main client application
├── mathserver.py      # Math operations MCP server (stdio)
├── weather.py         # Weather information MCP server (HTTP)
├── main.py           # Entry point placeholder
├── requirements.txt   # Python dependencies
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
└── README.md        # This file
```

## Prerequisites

- Python >= 3.12
- Groq API key (for the language model)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcplangchain
   ```

2. Install dependencies using uv (recommended) or pip:
   
   **Using uv:**
   ```bash
   uv sync
   ```
   
   **Using pip:**
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Create a .env file and add your Groq API key
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

## Usage

### Running the MCP Servers

1. **Start the Weather Server** (HTTP transport):
   ```bash
   python weather.py
   ```
   This starts an HTTP server at `http://127.0.0.1:8000/mcp`

2. **Math Server** is automatically started by the client via stdio transport.

### Running the Client

Execute the main client application:
```bash
python client.py
```

The client will:
1. Connect to both MCP servers
2. Create a LangGraph ReAct agent with access to all tools
3. Demonstrate math operations: `(3 + 5) * 12`
4. Demonstrate weather queries: Weather in New Jersey

## MCP Servers Details

### Math Server (`mathserver.py`)
- **Transport**: stdio
- **Tools**:
  - `add(a: int, b: int)`: Addition operation
  - `multiple(a: int, b: int)`: Multiplication operation

### Weather Server (`weather.py`)
- **Transport**: HTTP (streamable-http)
- **Endpoint**: `http://127.0.0.1:8000/mcp`
- **Tools**:
  - `get_weather(location: str)`: Get weather information for a location

## Configuration

The client configuration in `client.py` defines how to connect to each MCP server:

```python
{
    "math": {
        "command": "python",
        "args": ["mathserver.py"],
        "transport": "stdio"
    },
    "weather": {
        "url": "http://127.0.0.1:8000/mcp",
        "transport": "streamable_http"
    }
}
```

## Dependencies

- **langchain-groq**: Groq language model integration
- **langchain-mcp-adapters**: MCP to LangChain adapter
- **langgraph**: Agent framework for tool usage
- **mcp**: Model Context Protocol implementation
- **python-dotenv**: Environment variable management

## Example Output

When running the client, you'll see responses like:

```
math response: 
The result of (3 + 5) * 12 is 96.

weather response: 
It's always raining in New Jersey [with some creative flair]
```

## Extending the Project

To add new MCP servers:

1. Create a new server file following the FastMCP pattern
2. Define your tools using the `@mcp.tool()` decorator
3. Add server configuration to the client
4. Update the agent to use the new tools

## License

This project is licensed under the [Apache License 2.0](LICENSE).


## Troubleshooting

- Ensure your Groq API key is correctly set in the `.env` file
- Make sure the weather server is running before executing the client
- Check that all dependencies are properly installed

## Links

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://docs.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Groq API](https://groq.com/)