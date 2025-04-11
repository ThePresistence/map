import pymupdf4llm
from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("markdowngiver")


@mcp.tool()
def give_markdown(input_path: str) -> str: 

    """
    This function does ocr for pdf and gives markfown format output so end user can start using it for chunking 

    parameters: 
    ----------
    input_path: str 

    return: 
    --------
    output: str 
        contains the markdown text of input file 

    """
    md_text = pymupdf4llm.to_markdown(input_path)

    return md_text 


if __name__ == "__main__": 
    mcp.run(transport="stdio")


# {
#     "mcpServers": {
#         "markdowngiver": {
#             "command": "uv", 
#             "args": [
#                 "run", 
#                 "--with", 
#                 "mcp[cli]", 
#                 "mcp", 
#                 "run", 
#                 "<pura-path>"
#             ]
#         }
#     }
# }


