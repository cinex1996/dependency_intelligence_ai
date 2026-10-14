from unittest.mock import Mock

mock_basic = Mock()
mock_basic.status_code = 200
mock_basic.json.return_value = {
    "vulns": [
        {"id": "Test_first"},
        {"id": "Test_second"}
    ]
}

class TestMockBasic:
    def test_mock_response(self):
        assert mock_basic.status_code == 200
        assert isinstance(mock_basic.status_code, int)
        assert isinstance(mock_basic.json.return_value, dict)
        assert len(mock_basic.json.return_value) == 1
        assert len(mock_basic.json.return_value["vulns"]) == 2
        assert mock_basic.json.return_value["vulns"][0]["id"] == "Test_first"
        assert mock_basic.json.return_value["vulns"][1]["id"] == "Test_second"
        assert mock_basic.json() == mock_basic.json.return_value