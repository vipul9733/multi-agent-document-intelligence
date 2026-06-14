from pydantic import BaseModel
class DocumentRequest(BaseModel):
    document_text:str
