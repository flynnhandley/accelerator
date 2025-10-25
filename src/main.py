from src.handlers.function_handler import process_event


def handle_request(event: dict) -> dict:
    """
    Generic function-app entrypoint.
    Accepts an event dict and returns a dict response.
    """
    return process_event(event)
