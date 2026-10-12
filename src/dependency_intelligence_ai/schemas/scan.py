from pydantic import BaseModel

class ScanRequest(BaseModel):
    package: str
    version: str