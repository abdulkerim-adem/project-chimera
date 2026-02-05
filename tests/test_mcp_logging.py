def test_mcp_startup_logged_with_200():
    # We expect a successful startup code 200; if proxy returns 401 we want the test to fail.
    with open("mcp_sense.log", "r", encoding="utf-8") as fh:
        data = fh.read()
    assert '"event": "startup"' in data
    # This assertion intentionally expects 200 to cause a failing test if proxy demands auth (401).
    assert '"code": 200' in data