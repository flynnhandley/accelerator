from src.main import handle_request


def test_handle_request_success():
    event = {"data": "hello"}
    resp = handle_request(event)
    assert resp["status"] == "success"
    assert resp["result"]["input"] == "hello"


def test_handle_request_invalid():
    event = {"data": None}
    resp = handle_request(event)
    assert resp["status"] == "error"
