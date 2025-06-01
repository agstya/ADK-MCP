from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


# Define the MCP agent

root_agent = Agent(
    name="mcp_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are an MCP agent that can perform a veriety of tasks
    """,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="python",
                args=["absolute_path_to_server.py"]
            )
        ),

        # https://github.com/makenotion/notion-mcp-server

        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "notionhq/notion-mcp-server"]
            )
        ),

        # https://github.com/modelcontextprotocol/servers/tree/main/src

        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem-adapter"]
            )
        ),

        # https://github.com/github/github-mcp-server
        
        MCPToolset(
            connection_params=StdioServerParameters(
                command="docker",
                args=["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
                env={"GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_.."},  # Replace with your GitHub token
            )
        ),
    ],
)
