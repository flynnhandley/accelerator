from src.utils.helpers import validate_input


def process_event(event: dict) -> dict:
    """
    Process an incoming event dict and return a simple response.

    Expected event shape: {"data": <any>}
    """
    data = event.get("data") if isinstance(event, dict) else None

    if not validate_input(data):
        return {"status": "error", "message": "Invalid input", "code": 400}

    # Example business logic: echo the input and include a derived property
    result = {"input": data, "length": len(str(data))}
    return {"status": "success", "result": result}
