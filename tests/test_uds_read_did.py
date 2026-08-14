def test_read_did_0xF190():
    response = hil.send_uds_request("22 F1 90")
    assert response.startswith("62 F1 90")