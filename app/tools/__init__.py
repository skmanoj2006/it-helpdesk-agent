from app.tools.mock_tools import check_network, search_kb, provision_software
from app.tools.registry import ToolRegistry

def create_tool_registry():
    registry = ToolRegistry()
    registry.register("check_network", check_network, "Check whether a host is reachable.")
    registry.register("search_kb", search_kb, "Search for the query in the Knowledge Base")
    registry.register("provision_software",provision_software,"Provision approved software for a user.")
    return registry