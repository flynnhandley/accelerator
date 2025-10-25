def validate_input(data) -> bool:
    """Very small validator used by the example handler.

    Accepts basic primitives and collection types; returns False for None.
    """
    if data is None:
        return False
    return isinstance(data, (str, int, float, dict, list, tuple))
