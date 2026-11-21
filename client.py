
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# Path to our existing MCP server
SERVER_PATH = r"C:\Users\shali\Desktop\mcp app\mini-mcp-server\server.py"


async def main():

    # 1. Configure the server process
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[SERVER_PATH]
    )

    # 2. Establish STDIO connection
    async with stdio_client(server_params) as (read, write):

        # 3. Create MCP client session
        async with ClientSession(read, write) as session:

            # 4. Initialize the connection
            await session.initialize()

            print("\nConnected to MCP Server!")

            # 5. Discover available tools
            print("\n========== TOOLS ==========")

            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"\nName: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Input Schema: {tool.inputSchema}")

            # 6. Call the add tool
            print("\n========== TOOL EXECUTION ==========")

            result = await session.call_tool(
                "add",
                arguments={"a": 10, "b": 20}
            )

            for content in result.content:
                if hasattr(content, "text"):
                    print("Addition Result:", content.text)

            # 7. Discover resources
            print("\n========== RESOURCES ==========")

            resources = await session.list_resources()

            for resource in resources.resources:
                print(resource.name, resource.uri)

            # 8. Read a resource
            print("\n========== RESOURCE CONTENT ==========")

            resource_result = await session.read_resource(
                "notes://welcome"
            )

            for content in resource_result.contents:
                if hasattr(content, "text"):
                    print(content.text)

            # 9. Discover prompts
            print("\n========== PROMPTS ==========")

            prompts = await session.list_prompts()

            for prompt in prompts.prompts:
                print(prompt.name, prompt.description)

            # 10. Retrieve a prompt
            print("\n========== PROMPT CONTENT ==========")

            prompt_result = await session.get_prompt(
                "explain_mcp",
                arguments={"topic": "MCP Client"}
            )

            for message in prompt_result.messages:
                if hasattr(message.content, "text"):
                    print(message.content.text)


if __name__ == "__main__":
    asyncio.run(main())
