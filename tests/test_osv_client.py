import json

import httpx
import pytest

from services.osv_client import build_osv_payload, extract_vulnerability_ids, query_osv


def handler(request):
    return httpx.Response(200, json={"vulns": [
        {"id": "GHSA-example-1"},
        {"id": "GHSA-example-2"}]})

def date_return():
    return {
    "version": "0.1.0",
    "package": {
        "name": "Django",
        "ecosystem": "PyPI"
    }
    }
class TestOSVPayload:
    def test_build_osv_payload(self):

        result = build_osv_payload("Django","0.1.0")
        assert isinstance(result, dict)
        assert result == date_return()

    def test_extract_vulnerability_ids(self):
        data = {
            "vulns": [
                {"id": "GHSA-example-1"},
                {"id": "GHSA-example-2"}
            ]
        }
        result = extract_vulnerability_ids(data)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] == "GHSA-example-1"
        assert result[1] == "GHSA-example-2"

    def test_extract_vulnerability_ids_empty(self):
        data = {"vulns": []}
        result = extract_vulnerability_ids(data)
        assert isinstance(result, list)
        assert len(result) == 0
        assert result == []

    @pytest.mark.asyncio
    async def test_query_osv_success(self):

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            result = await query_osv("Django","0.1.0",client)
            assert isinstance(result, dict)
            assert "vulns" in result
            assert result["vulns"] == []







