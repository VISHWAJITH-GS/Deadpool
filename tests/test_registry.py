import pytest
from app.tools.registry import ToolRegistry

def test_registry_registration():
    registry = ToolRegistry()
    
    @registry.register("test_tool", "A test", {"type": "object", "properties": {}})
    def test_func():
        return "success"
        
    schemas = registry.get_schemas()
    assert len(schemas) == 1
    assert schemas[0]["name"] == "test_tool"
    
def test_registry_execution():
    registry = ToolRegistry()
    
    @registry.register("echo", "Echos input", {"type": "object", "properties": {"val": {"type": "string"}}})
    def echo(val: str):
        return val
        
    result = registry.execute("echo", {"val": "hello"})
    assert result == "hello"
