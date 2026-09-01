from app.tools import create_tool_registry


def main():
    tools = create_tool_registry()

    result = tools.execute(
        "check_network",
        {"host": "vpn.company.internal"}
    )

    print(result)


if __name__ == "__main__":
    main()