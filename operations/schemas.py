from pydantic import BaseModel
from datetime import datetime

class OperationCreate(BaseModel):
  id: int
  quantity: str
  type: str
  instrument_type: str
  figi: str
  date: datetime
