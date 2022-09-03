from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str] = Field(None, max_length=10)


# orm_mode = True флаг чтоб получать записи в БД через ORM
class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase):
    pass
