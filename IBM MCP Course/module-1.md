# Module 1: Getting Started with MCP

## Course Overview: Building AI Agents with MCP

- The Model Context Protocol (MCP) is a standardized protocol for connecting AI applications and large language models (LLMs) to external tools, data sources, and services.
- MCP reduces the need for fragile, one-off integrations by providing a consistent and scalable interface for tool and context access.
- It enables AI agents to interact with external systems through structured communication, supporting scalable, secure, and reliable AI workflows.
- The course provides hands-on experience building, running, testing, and optimizing MCP applications using Python.

## Learning Prerequisites

- Required: Basic proficiency in Python programming.
- Recommended: Familiarity with AI concepts, large language models (LLMs), client-server architecture, HTTP requests, and command-line tools.
- Prior experience with MCP or specific frameworks is not required.

## Course Learning Objectives

By the end of the course, learners should be able to:

- Explain MCP fundamentals and its advantages over traditional APIs and tool-calling approaches.
- Analyze MCP client-server interactions and design efficient multi-agent workflows.
- Build and run MCP applications using Python.
- Develop MCP servers with tools, resources, and prompts.
- Implement advanced MCP features, including sampling, root controls, and bidirectional LLM calls.
- Evaluate performance optimization, context management, and server reliability.
- Apply security best practices and user interaction patterns to develop scalable MCP applications.

## Module 1: Getting Started with MCP

Topics covered:

- Introduction to MCP and its core concepts.
- MCP client-server architecture and communication mechanisms.
- How MCP works in practical applications.
- Connecting to existing MCP servers and running them locally.
- Building basic MCP applications using Python.

Key takeaway: MCP provides a standardized way for AI applications to access external capabilities and context through a defined client-server architecture.

## Module 2: MCP Server Development

Topics covered:

- Understanding MCP server fundamentals.
- Converting existing tools into MCP servers.
- Extending servers with tools, resources, and prompts.
- Building enhanced MCP servers for practical use cases.
- Running, testing, and integrating MCP servers.
- Applying MCP to retrieval-augmented generation (RAG).

Key takeaway: MCP servers expose capabilities and contextual information to AI applications in a standardized format, allowing existing functionality to be integrated into agentic workflows.

## Module 3: MCP Hosts and Clients

Topics covered:

- MCP client architecture and implementation patterns.
- Client lifecycle and connection management.
- Query routing and retrieval.
- Performance optimization through connection pooling, context caching, and load balancing.
- Advanced MCP features, including sampling and root controls.
- Bidirectional LLM calls and interactive workflows.
- Elicitation, user permissions, and secure interaction patterns.

Key takeaway: Efficient MCP clients manage communication, context, and connections while supporting secure interactions between AI models, servers, and users.

## Important MCP Concepts

- MCP Client: Connects to an MCP server and facilitates communication between the host application and the server.
- MCP Server: Exposes tools, resources, and prompts that AI applications can use.
- MCP Host: The AI application that manages MCP clients and coordinates their interactions with models and servers.
- Tools: Executable functions that an AI application can invoke to perform actions or retrieve information.
- Resources: Contextual data exposed to applications, such as files, documents, or other information sources.
- Prompts: Reusable prompt templates or predefined instructions exposed by an MCP server.
- Sampling: Allows an MCP server to request LLM generation through the connected client, subject to the host's policies and permissions.
- Roots: Define filesystem or other supported resource boundaries that communicate the scope of accessible content; they are not a security boundary by themselves.
- Elicitation: Allows an MCP server to request additional information from the user through the client.
- Context Caching: Reuses previously obtained context to reduce redundant processing and improve performance.

## Tools and Technologies

- Python: Primary programming language for implementing MCP clients, servers, and workflows.
- MCP clients and servers: Core components used to implement standardized communication.
- HTTP and Standard I/O (stdio): Transport mechanisms for communication between MCP components.
- Cloud IDE: Environment for completing hands-on labs and testing implementations.

## Recommended Study Approach

1. Watch the course videos and review the readings.
2. Use cheat sheets to reinforce important concepts.
3. Complete hands-on labs to build and test MCP clients and servers.
4. Take practice quizzes to evaluate understanding.
5. Complete graded assessments to verify mastery.
6. Pay particular attention to client-server interactions, context management, performance, and security.

## Course Structure Summary

| Module   | Primary Focus                                                      |
| -------- | ------------------------------------------------------------------ |
| Module 1 | MCP fundamentals and basic applications                            |
| Module 2 | MCP server development, tools, resources, prompts, and RAG         |
| Module 3 | Client architecture, advanced features, optimization, and security |

The course is part of the IBM RAG and Agentic AI Professional Certificates and focuses on practical skills for developing advanced AI applications that integrate external tools, data, and services through MCP.

## MCP Tool-Calling Workflow

1. User submits a question: The user asks a question through a chat application.
2. LLM identifies available tools: The MCP host and client provide the LLM with information about the available tools. The LLM determines which tools are appropriate for the request.
3. Host and client select the MCP server: Based on the LLM's tool selection, the host and client identify the MCP server that exposes the required tool.
4. MCP server executes the tool: The server runs the requested operation, which may involve:
   - Querying a database.
   - Calling an external API.
   - Executing local code.
5. Server returns the result: The MCP server sends the tool's output back to the MCP client and host.
6. LLM processes the result: The tool result is passed to the LLM, which uses it to formulate a response. Additional tool calls may occur if needed.
7. Final answer is returned: The LLM generates the final answer and displays it in the chat application.

## Why Use MCP?

- Standardized integration: MCP provides a common protocol for connecting AI agents to external data sources and tools.
- Reusability: An MCP server can expose capabilities that different compatible AI applications can use.
- Reduced integration complexity: Developers do not need to build a completely different integration for every AI application and data source.
- Industry relevance: Even if a developer does not build AI agents directly, their clients or other systems they integrate with may use agents. Understanding MCP helps developers build compatible services and integrations.

## Key Takeaway

MCP acts as a standardized bridge between AI applications and external capabilities. The LLM decides which tools are needed, the MCP client coordinates communication, and the MCP server executes the requested operations and returns their results.

## Why Model Context Protocol (MCP)?

### Learning Objectives

After this lesson, learners should be able to:
- Explain the importance of standardization to developers.
- Describe the key benefits of MCP.
- Identify common real-world use cases for MCP.

## What Is MCP?

- **Model Context Protocol (MCP)** is an open protocol that standardizes how AI applications and large language models (LLMs) connect to external data sources, tools, and services.
- MCP servers can be developed using different programming languages, including Python, JavaScript, Java, and C#.
- MCP acts as a **universal integration layer**, allowing AI applications to discover and use external capabilities through a consistent interface.

### Two Main Requirements of AI Agents

1. **Context:** External information used to answer questions, such as documents, database entries, and articles.
2. **Tools and capabilities:** Functions that allow agents to perform actions, such as web searches, booking reservations through external services, and complex calculations.

With MCP, an AI agent can discover the capabilities offered by an MCP server and invoke them through a standardized protocol.

## Importance of Standardization

Standardization simplifies development and makes integrations more consistent and reusable.

- **Extensibility:** New tools and functionality can be added more easily without redesigning existing integrations.
- **Interoperability:** Applications can work across different platforms, vendors, models, and frameworks.
- **Consistency:** Tools follow a common communication pattern across compatible AI applications and models.
- **Reusability:** Developers can build tools once and reuse them across multiple projects.
- **Rapid development:** Standardized integrations reduce duplicated work and eliminate the need to build custom connectors for every project.

## Key Benefits of MCP

### 1. Standardized Integration

MCP provides a common protocol for connecting AI models to external tools and data sources. It reduces the need to create custom integration code for every function, tool, or third-party API.

**Benefit:** Faster development, less duplicated code, and simpler integration management.

### 2. Simple Client-Server Architecture

MCP uses a client-server architecture that separates the AI application from the capabilities exposed by MCP servers.

This plug-and-play approach simplifies connection setup, integration, deployment, and scaling.

**Benefit:** Components can be developed and maintained separately, making systems easier to extend.

### 3. Interoperability

MCP supports diverse development environments and can integrate with compatible models, platforms, and frameworks, such as OpenAI, Azure OpenAI, LangChain, and LlamaIndex.

**Benefit:** Developers can reuse integrations instead of tying their tools to a single AI provider or framework.

### 4. Enhanced Security

MCP implementations can use authentication and authorization mechanisms to control access to external systems and resources. Depending on the transport and deployment, security measures may include OAuth 2.0, access tokens, and TLS-encrypted communication.

**Benefit:** Properly configured authentication, authorization, and transport security help protect data and restrict unauthorized access.

### 5. Reduced AI Hallucinations

LLMs may generate incorrect, outdated, or fabricated information when their internal knowledge is insufficient.

MCP allows AI applications to retrieve relevant information from external sources, such as databases, documents, and live APIs, and use that information to generate responses.

**Benefit:** Grounding responses in reliable, current data can reduce hallucinations and improve factual accuracy.

*Note: MCP does not eliminate hallucinations. Accuracy still depends on the quality of retrieved information, tool implementation, and how the LLM interprets the results.*

### 6. Support for Agentic Workflows

MCP enables agents to access tools and information needed to complete multistep tasks. Multiple agents or AI components can also coordinate through appropriate integrations and workflows.

For example, one agent could retrieve information, another could analyze it, and a subsequent step could generate a report.

**Benefit:** Complex tasks can be divided into smaller operations, improving automation and workflow flexibility.

### 7. Improved Data Relevance

LLMs have knowledge limitations because their training data covers a particular period and may not include recent events.

MCP servers can retrieve updated information from external sources, including databases, APIs, and other connected services.

**Benefit:** AI applications can use more current and contextually relevant information when generating responses.

## Common Use Cases for MCP

### 1. Enterprise Applications

MCP can connect AI applications to internal business systems, including:

- Databases and enterprise information systems.
- Customer relationship management (CRM) systems.
- Ticketing platforms and support services.
- Workflow automation and report generation.
- Live information sources, such as stock prices, weather, and news.

### 2. Agentic AI

MCP supports AI agents that select and use tools based on a user's goals.

Common applications include:
- Autonomous tool selection and execution.
- Retrieving information from multiple data sources.
- Combining external context to support decisions.
- Automating complex, multistep tasks.

### 3. DevOps

DevOps focuses on software development and IT operations. MCP can support:

- CI/CD pipeline automation.
- Repository and code management, such as GitHub integrations.
- Infrastructure automation.
- Automated incident response.

### 4. NetOps

NetOps focuses on network operations, management, and reliability.

Potential applications include:
- Network management and performance monitoring.
- Router and firewall configuration.
- Network anomaly detection.
- Automated troubleshooting and issue remediation.

### 5. SecOps

SecOps focuses on security operations and incident management.

Potential applications include:
- Proactive threat detection and mitigation.
- Real-time incident orchestration and response.
- Security vulnerability identification and management.
- Automated security investigation workflows.

## MCP for Retrieval-Augmented Generation (RAG)

### Example: A Bank with 100,000 Documents

Suppose an AI engineer is building a RAG system for a bank containing over 100,000 documents. The system must retrieve only a few relevant text passages to provide context to an LLM.

A traditional implementation may require document storage, vector embeddings, a vector database, and infrastructure for retrieving relevant content.

An MCP server can expose a retrieval tool that handles the retrieval process behind a standardized interface.

### Workflow

1. **User submits a query:** The user asks a question about the bank's documents.
2. **LLM requests retrieval:** The AI application determines that relevant documents are needed and invokes an available retrieval tool.
3. **MCP server performs retrieval:** The server searches the document collection using its configured retrieval system, which may include a vector database.
4. **Relevant chunks are returned:** The server returns only the most relevant text passages rather than the entire document collection.
5. **LLM generates an answer:** The model uses the retrieved passages as context to answer the user's question.

### Key Takeaway

MCP does not replace the underlying vector database or RAG infrastructure. Instead, it provides a standardized interface through which an AI application can access retrieval capabilities implemented by an MCP server.

This separates the retrieval implementation from the AI application and makes the retrieval tool easier to reuse across compatible clients.

## Summary

MCP is an open protocol that standardizes how AI applications and LLMs access external tools, data, and services.

Its main benefits are:
- Standardized integration.
- Simple client-server architecture.
- Interoperability.
- Enhanced security when properly configured.
- Reduced risk of hallucinations through external data grounding.
- Support for agentic workflows.
- Access to relevant and up-to-date information.

Its applications span enterprise systems, agentic AI, DevOps, NetOps, SecOps, and RAG systems.

**Core concept:** MCP standardizes how AI applications connect to external capabilities. It does not replace the tools, databases, or services themselves; it provides a consistent way to expose and access them.

## Model Context Protocol (MCP) vs. Application Programming Interface (API)

### Introduction

Large language models (LLMs) often need to interact with external data sources, services, and tools to perform useful tasks. Traditionally, developers used **Application Programming Interfaces (APIs)** to connect applications to these systems.

In November 2024, Anthropic introduced the **Model Context Protocol (MCP)**, an open standard that standardizes how AI applications connect to external tools and data sources and provide context to LLMs.

Both APIs and MCP enable system integration, but they serve different roles.

## What Is MCP?

The **Model Context Protocol (MCP)** is an open protocol that standardizes communication between AI applications and external systems.

MCP can be compared to a **USB-C port for AI applications**:
- USB-C provides a common connection standard for different peripherals, regardless of manufacturer.
- MCP provides a common integration standard for AI applications to access different tools, data sources, and services, regardless of their implementation.

For example, an AI application can connect to separate MCP servers that provide access to a database, a code repository, and an email service.

### MCP Architecture

MCP uses a client-server architecture consisting of three main components:

- **MCP Host:** The AI application that coordinates interactions with language models and MCP clients.
- **MCP Client:** A component within the host that establishes and manages a connection to an MCP server.
- **MCP Server:** A component that exposes capabilities, such as tools, resources, and prompts, to compatible clients.

MCP communication uses **JSON-RPC 2.0** messages. Depending on the transport, communication can occur through mechanisms such as standard input/output (stdio) or HTTP-based transport.

### MCP Primitives

MCP servers can expose three main primitives:

#### 1. Tools

- Executable functions or actions that an AI application can invoke.
- Allow AI agents to interact with external systems and perform operations.
- Each tool can provide a name, description, input schema, and structured output.

**Examples:**
- A weather server exposing a `get_weather` tool.
- A calendar server exposing a `create_event` tool.
- A database server exposing a query tool.

When a tool is invoked, the MCP server executes the underlying function and returns the result.

#### 2. Resources

- Read-oriented data items that an MCP server makes available to clients.
- Provide contextual information that an AI application can retrieve when needed.

**Examples:**
- Text files and document contents.
- Database schemas.
- Knowledge base information.

#### 3. Prompts

- Reusable prompt templates exposed by an MCP server.
- Provide predefined instructions or suggested prompt structures for particular tasks.

**Example:** A code repository server might provide a prompt template for reviewing code changes.

Not every MCP server exposes all three primitives. Many focus primarily on tools.

### Runtime Capability Discovery

MCP allows clients to discover the capabilities exposed by a server at runtime through standardized operations, including:

- `tools/list`
- `resources/list`
- `prompts/list`

This enables compatible clients to discover available functionality without requiring a custom integration for every individual tool.

However, discovering a tool does not automatically grant permission to execute it. Access controls and application policies still apply.

## What Is an API?

An **Application Programming Interface (API)** defines a set of rules and conventions that allow one software system to interact with another system's functionality or data.

APIs provide an abstraction layer between the requesting application and the service being accessed. The client does not need to understand the server's internal implementation; it only needs to know how to format requests and interpret responses.

**Example:** An e-commerce application can use a payment API to process transactions without implementing the payment provider's internal payment infrastructure.

### RESTful APIs

One of the most common API styles is REST (Representational State Transfer), which typically uses HTTP methods to interact with resources.

| HTTP Method | Typical Purpose | Example |
|---|---|---|
| `GET` | Retrieve data | `GET /books/123` |
| `POST` | Create a resource or submit an operation | `POST /loans` |
| `PUT` | Replace or update a resource | `PUT /books/123` |
| `DELETE` | Delete a resource | `DELETE /books/123` |

REST APIs commonly exchange data in JSON format.

For example:
- `GET /books/123` retrieves details about book 123.
- `POST /loans` submits a request to create a book loan.

APIs are also widely used to provide access to LLMs. An application can send a JSON request containing a prompt or messages to an LLM service and receive a JSON response.

AI agents can likewise use REST APIs to perform web searches, access internal business services, and retrieve external data.

## MCP vs. APIs

| Aspect | MCP | APIs |
|---|---|---|
| Primary purpose | Standardizes how AI applications discover and interact with external capabilities and context | Defines how software systems expose and access functionality or data |
| Scope | Specifically designed for AI context and capability integration | General-purpose software integration |
| Architecture | Host, client, and server | Varies by API design and implementation |
| Capability discovery | Supports standardized discovery of tools, resources, and prompts | Depends on the API and its documentation or discovery mechanisms |
| Communication | Uses JSON-RPC 2.0 messages over supported transports | Depends on the API style; REST commonly uses HTTP |
| Tool execution | Exposes tools through standardized MCP operations | Exposes functionality through API-specific operations or endpoints |
| Data access | Can expose resources and tools for retrieving information | Can provide data through endpoints or other interface operations |
| Reusability | MCP-compatible clients can reuse server integrations | API clients can reuse integrations when they follow the API's specifications |
| Typical use cases | AI agents, context retrieval, tool discovery, and standardized AI integrations | Web services, payment processing, databases, enterprise systems, and many other applications |

## How MCP and APIs Work Together

MCP does not replace APIs. Instead, an MCP server can act as a standardized interface over existing APIs and services.

For example, an AI agent that needs current weather information can use the following workflow:

1. The user asks for the current weather.
2. The MCP client discovers a `get_weather` tool exposed by an MCP server.
3. The LLM determines that the tool is appropriate and requests its invocation.
4. The MCP server calls an external weather API.
5. The weather API returns the current weather data.
6. The MCP server returns the result through MCP.
7. The LLM uses the returned data to generate a response.

This architecture allows the AI application to interact with the weather service through MCP without needing to implement the weather provider's API integration directly.

## Key Takeaways

- **MCP is a protocol for standardized AI integration**, while APIs are interfaces through which software systems expose functionality and data.
- MCP uses a host-client-server architecture and JSON-RPC 2.0 messages.
- MCP servers can expose tools, resources, and reusable prompt templates.
- Runtime discovery allows compatible clients to identify available server capabilities.
- REST APIs commonly use HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
- MCP and APIs are complementary: MCP servers can use existing APIs to provide standardized capabilities to AI agents.

**Core concept:** APIs enable software systems to communicate, while MCP standard