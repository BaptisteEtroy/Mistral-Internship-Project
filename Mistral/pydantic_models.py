from pydantic import BaseModel, constr


class QueryRequest(BaseModel):
    question: constr(min_length=1, strip_whitespace=True)
    db_name: str


class QueryResponse(BaseModel):
    question: str
    answer: str
