from unittest.mock import AsyncMock
import pytest
asyncmock_dict = {
    "vulns": [
        {
            "id": "Test_first",
        },
        {
            "id": "Test_second",
        }
    ]}
async_mock = AsyncMock(return_value=asyncmock_dict)

class TestAsyncMock:
    @pytest.mark.asyncio
    async def test_async_mock(self):
        test_asyncmock_dict = {
            "vulns": [
                {
                    "id": "Test_first",
                },
                {
                    "id": "Test_second",
                }
            ]}
        test = AsyncMock(return_value=test_asyncmock_dict)
        result = await test()
        test.assert_awaited_once()
        assert result == test_asyncmock_dict
        assert result["vulns"][0]["id"] == "Test_first"
        assert result["vulns"][1]["id"] == "Test_second"



