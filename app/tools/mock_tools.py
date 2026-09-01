from typing import Any


def reset_password(user_id: str) -> dict[str, Any]:
    return {
        "success": True,
        "user_id": user_id,
        "message": "Password reset successfully."
    }


def get_asset_info(asset_tag: str) -> dict[str, Any]:
    return {
        "success": True,
        "asset_tag": asset_tag,
        "device_type": "laptop",
        "status": "active"
    }


def search_kb(query: str) -> dict[str, Any]:
    return {
        "success": True,
        "query": query,
        "results": [
            "Restart the VPN client.",
            "Verify network connectivity.",
            "Check whether the VPN gateway is reachable."
        ]
    }


def check_network(host: str) -> dict[str, Any]:
    return {
        "success": True,
        "host": host,
        "reachable": True
    }


def provision_software(user_id: str, name: str) -> dict[str, Any]:
    return {
        "success": True,
        "user_id": user_id,
        "software": name,
        "message": f"{name} provisioned successfully."
    }


def update_ticket(ticket_id: str, status: str) -> dict[str, Any]:
    return {
        "success": True,
        "ticket_id": ticket_id,
        "status": status
    }


def escalate_ticket(ticket_id: str, reason: str) -> dict[str, Any]:
    return {
        "success": True,
        "ticket_id": ticket_id,
        "reason": reason,
        "status": "escalated"
    }


def notify_user(requester_id: str, message: str) -> dict[str, Any]:
    return {
        "success": True,
        "requester_id": requester_id,
        "message": message
    }