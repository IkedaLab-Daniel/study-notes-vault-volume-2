# Module 2: MCP Server

## Hello World of MCP Servers

- FastMCP simplifies creating MCP servers in Python.
- MCP servers act like function libraries that expose capabilities to AI applications.
- This lesson demonstrates how to build a calculator MCP server and register three MCP primitives: tools, resources, and prompts.
- It also covers testing servers, connecting through STDIO and HTTP, and integrating MCP tools with ReAct agents.

## Creating an MCP Server with FastMCP

The first step is creating a FastMCP server object.

Two important configuration properties:

- Name: Identifies the MCP server.
- Instructions: Provides natural-language documentation that helps LLMs understand when and how the server's tools should be used.

## Registering MCP Tools

Tools are executable functions that an AI agent can invoke.

FastMCP uses the `@mcp.tool` decorator to register Python functions as MCP tools.

Example tools in the calculator server:

- Addition: Adds two integers.
- Subtraction: Subtracts one integer from another.

Important implementation details:

- Use Python type hints to define input and return types.
- Provide a docstring describing the function's purpose.
- The LLM uses the tool's description to determine when it is appropriate to call the function.

## Registering MCP Resources

Resources are like filing cabinets that AI applications can access to retrieve information.

FastMCP uses the `@mcp.resource` decorator to register resources.

### URI Templates and Parameters

A resource can use a URI template containing a path parameter, such as:

```
file:///endpoint/{name}
```

The workflow is:

1. The client requests a resource URI.
2. The server extracts the `{name}` parameter from the URI.
3. The parameter is passed to the resource function.
4. The function uses the name to construct a file path.
5. The server reads the file contents and returns them to the client.

For example, requesting a resource with `name = "dog"` retrieves the corresponding document contents, assuming the file exists.

## Registering MCP Prompts

Prompts are reusable instruction templates for common tasks.

- Registered using the `@mcp.prompt` decorator.
- Allow predefined instructions to be stored and retrieved by name.
- Can accept parameters to customize the generated prompt.

Example:

- Prompt template: `Please review this code: {code}`
- Parameter: `code = "n = 1"`
- Result: `Please review this code: n = 1`

Prompts reduce the need to repeatedly write the same instructions.

## Testing MCP Servers with In-Memory Transport

In-memory transport provides a simple way to test an MCP server without starting a separate process or establishing a network connection.

- Import the FastMCP client.
- Instantiate the client using the MCP server object.
- This creates a direct connection between the client and server within the same Python process.

### Calling a Tool

The video demonstrates testing the addition tool:

1. Create an asynchronous function.
2. Establish a connection using `async with client`.
3. Invoke `client.call_tool()` with the tool name and parameters.
4. Use `await` to wait for the server's response without blocking other tasks.

Example:

```
await client.call_tool("add", {"a": 4, "b": 5})
```

Result: 9

The returned response object provides multiple ways to access the result.

### Reading a Resource

Resources can be tested using:

```
await client.read_resource("file:///endpoint/dog")
```

The client receives the resource contents returned by the server.

## Running an MCP Server with HTTP Transport

FastMCP can run an MCP server as an HTTP service.

- Use `run_http_async()` to start the server.
- Specify the port number.
- The example runs on port `8000` with the MCP endpoint at `/mcp`.

The client must be configured with a Streamable HTTP transport object containing the server URL.

The HTTP client then uses this transport to communicate with the server.

Key point: The MCP server can run on another machine or location, provided the client can access its URL.

## Integrating an HTTP MCP Server with a ReAct Agent

The video demonstrates connecting the calculator MCP server to an LLM-powered agent.

### Main Components

| Component                | Purpose                                                |
| ------------------------ | ------------------------------------------------------ |
| `ChatOpenAI`             | Provides the language model.                           |
| `create_react_agent`     | Creates an agent capable of reasoning and using tools. |
| `load_mcp_tools`         | Converts MCP tools into LangChain-compatible tools.    |
| `streamable_http_client` | Establishes the HTTP connection.                       |
| `ClientSession`          | Manages MCP protocol communication.                    |

### Agent Connection Workflow

1. Establish an HTTP connection using `streamable_http_client`.
2. Obtain the read and write streams, along with the session ID.
3. Pass the streams into `ClientSession`.
4. Initialize the session using `await session.initialize()`.
5. Load MCP tools using `load_mcp_tools(session)`.
6. Create a ReAct agent with the LLM and converted tools.
7. Invoke the agent with a user prompt.

The agent can now identify when to use the calculator tool, extract the required numbers, and send them to the MCP server.

Example workflow:

- User asks: "What is 1 + 2?"
- Agent extracts the numbers `1` and `2`.
- MCP server calculates the result.
- The result is returned to the agent.
- The LLM generates a natural-language response.

## Running an MCP Server with STDIO Transport

Unlike HTTP, where the client connects to an already-running server, STDIO allows the client to launch the MCP server as a child process.

### Server Configuration

- Save the server implementation in a Python file, such as `stdio_server.py`.
- Add `mcp.run()` to start the server using STDIN and STDOUT.
- If working in Jupyter Notebook, save the server code as a `.py` file.

### Client Configuration

1. Configure the STDIO transport using `stdio_transport_client`.
2. Specify the Python file that runs the server.
3. The client launches the server process when the connection is established.
4. Use the client to discover and invoke tools.

The calculator example sends `4` and `5` to the server and receives `9`.

### Using STDIO with an LLM

The agent integration process is essentially identical to HTTP:

1. Create the STDIO connection.
2. Initialize the MCP session.
3. Load the MCP tools.
4. Create the ReAct agent.
5. Invoke the agent.

The main difference is the transport configuration: STDIO uses a client that launches the server process, while HTTP connects to a running server through its URL.

## Connecting Multiple MCP Servers

The MultiServer MCP Client allows an application to connect to multiple MCP servers through a single client configuration.

It accepts a dictionary where:

- Each key represents a server name.
- Each value contains the server type and transport configuration.

Example configuration concept:

| Server Type | Configuration                                     |
| ----------- | ------------------------------------------------- |
| STDIO       | Python file or command used to launch the server. |
| HTTP        | URL of the remote MCP server.                     |

The application can then:

1. Connect to all configured servers.
2. Retrieve tools from all connected servers.
3. Pass the combined tool list to a ReAct agent.
4. Invoke the agent to process user requests using tools from different servers.

## Key Takeaways

- FastMCP makes it easier to create MCP servers using Python.
- MCP servers can expose three main primitives: tools, resources, and prompts.
- Tools execute functions, resources provide information, and prompts provide reusable instruction templates.
- In-memory transport is useful for testing clients and servers within the same process.
- HTTP connects to an already-running server through a URL.
- STDIO launches a local server as a child process and communicates through standard input/output pipes.
- Both HTTP and STDIO can be integrated with ReAct agents using MCP sessions and tool adapters.
- MultiServer MCP Client allows one application to use tools from multiple MCP servers.