from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Mini MCP Server")

#Tool 1
@mcp.tool()
def add(a:float,b:float)->float:
    """Add Two numbers"""
    return a+b

@mcp.tool()
def multiply(a:float,b:float)->float:
    "multiply numbers"
    return a*b

@mcp.tool()
def subtract(a:float,b:float)->float:
    """subtract numbers"""
    return a-b

@mcp.tool()
def divide(a:float,b:float)->float:
    """Divide Numbers"""
    return a/b

#Resouurces
@mcp.resource("notes://welcome")
def get_notes()->str:
    """Return some learning notes."""
    return """
    Welcome to the Mini MCP Server!
    
    MCP Stands for model context protocol
    
    It allows AI applications to communicate
    with external tools and data sources."""

#PRompt
@mcp.prompt()
def explain_mcp(topic:str)->str:
    "Generate a prompt to explain the MCP topic."
    return f"""
    Explain {topic} in simple Language
    
    Include:
    1.Defination
    2.How it Works
    3.A practical example
    4.Common Interview Questions
    """
if __name__=="__main__":
    mcp.run(transport="stdio")