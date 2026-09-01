from app.models.ticket import Ticket, TicketPriority
from app.tools.mock_tools import search_kb, check_network


def main():
    ticket = Ticket(
        ticket_id="INC001",
        requester_id="USER123",
        description="My VPN is not connecting.",
        priority=TicketPriority.P2
    )

    print("Ticket:")
    print(ticket)

    print("\nSearching knowledge base...")

    kb_result = search_kb(ticket.description)

    print(kb_result)

    print("\nChecking VPN network...")

    network_result = check_network("vpn.company.internal")

    print(network_result)


if __name__ == "__main__":
    main()