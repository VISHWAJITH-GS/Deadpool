from app.applications.registry import tool_registry
from app.applications.resolver import app_web_registry
import webbrowser
import urllib.request
import urllib.parse
import re

@tool_registry.register(
    name="web_search",
    description="Searches the web for current information.",
    schema={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query"
            }
        },
        "required": ["query"]
    }
)
def web_search(query: str) -> str:
    """Real web search using DuckDuckGo HTML."""
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    # Use a standard browser User-Agent to avoid immediate blocks
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    try:
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            
            # Extract snippets using regex
            snippets = re.findall(r'<a class="result__snippet[^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
            
            if not snippets:
                return f"No results found for '{query}'."
                
            results = []
            for i, snippet in enumerate(snippets[:3]): # Top 3 results
                # Clean up HTML tags (like <b> tags for bolding)
                clean_text = re.sub(r'<[^>]+>', '', snippet)
                # Decode basic HTML entities
                clean_text = clean_text.replace('&#x27;', "'").replace('&quot;', '"').replace('&amp;', '&')
                results.append(f"{i+1}. {clean_text.strip()}")
                
            return "Search Results:\n" + "\n".join(results)
    except Exception as e:
        return f"Web search failed: {e}"

@tool_registry.register(
    name="open_url",
    description="Opens a website. Pass the raw URL or a known alias (e.g., 'leetcode').",
    schema={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL or known website alias."
            }
        },
        "required": ["url"]
    }
)
def open_url(url: str) -> str:
    """Opens a URL, checking the registry first."""
    # Check registry for alias
    resolved_url = app_web_registry.find_website(url)
    final_url = resolved_url if resolved_url else url
    
    if not final_url.startswith("http"):
        final_url = "https://" + final_url

    try:
        webbrowser.open(final_url)
        return f"Successfully opened URL: {final_url}"
    except Exception as e:
        return f"Failed to open URL: {str(e)}"
