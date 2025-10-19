
from PyPDF2 import PdfReader
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("PDF-reader")

@mcp.tool()
def pdf_to_page_list(pdf_path):
    """
    Reads a PDF file and returns a list of strings, one per page.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        list[str]: List where each element is the text of a page.
    # """
    reader = PdfReader(pdf_path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text())
    return pages

if __name__ == "__main__":
    mcp.run(transport="stdio")