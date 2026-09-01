import inspect
class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, name, function, description):
        self.tools[name] = {
            "function": function,
            "description": description
        }

    def get(self, name):
        return self.tools.get(name)

    def execute(self, name, arguments):
        tool = self.tools.get(name)

        if tool is None:
            raise ValueError(f"No such tool: {name}")

        func = tool["function"]

        return func(**arguments)
    def get_schema(self, name):
        tool = self.tools.get(name)

        if tool is None:
            raise ValueError(f"No such tool: {name}")

        func = tool["function"]
        signature = inspect.signature(func)

        type_mapping = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean"
        }

        properties = {}

        for param_name, parameter in signature.parameters.items():
            properties[param_name] = {
                "type": type_mapping[parameter.annotation]
            }

        return {
            "name": name,
            "description": tool["description"],
            "input_schema": {
                "type": "object",
                "properties": properties,
                "required": list(signature.parameters.keys())
            }
        }