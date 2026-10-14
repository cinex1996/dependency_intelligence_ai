import httpx


def build_osv_payload(package: str, version: str) -> dict:
    package_info = {
        "name": package,
        "ecosystem": "PyPI"
    }
    data = {
        "version": version,
        "package": package_info,
    }
    return data

async def query_osv(name: str, version: str, client: httpx.AsyncClient) -> dict:
    data = build_osv_payload(name, version)
    query = await client.post("https://api.osv.dev/v1/query", json=data)
    query.raise_for_status()
    return query.json()

def extract_vulnerability_ids(data: dict) -> list[str]:
    vulnerability_ids = []
    vulnerabilities = data.get("vulns",[])
    for vulnerability in vulnerabilities:
        vulnerability_ids.append(vulnerability["id"])
    return vulnerability_ids


