from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import Depends
from auth.database import get_async_session
from  sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete
from .models import operation
from .schemas import OperationCreate

router=APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("")
async def get_specific_operation(operation_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
      query= await session.get(operation, operation_id)
      return {
        "status":"success",
        "data":query,
        "details":None
      }
    except Exception:
      raise HTTPException(status_code=500, detail={
        "status":"error",
        "data":None,
        "details":None
      })

@router.post("/")
async def add_specific_operation(new_operation:OperationCreate, session:AsyncSession=Depends(get_async_session)):
  stmt=insert(operation).values(**new_operation.dict())
  await session.execute(stmt)
  await session.commit()
  return {'message':"Operation created"}

@router.delete("/")
async def get_specific_operations(operation_id: int, session: AsyncSession = Depends(get_async_session)):
  query = await session.get(operation, operation_id)
  if not query:
      raise HTTPException(status_code=404, detail="Operation not found")
  await session.delete(query)
  await session.commit()
  return {"message": "Operation deleted"}


@router.put("/")
async def update_operation(operation_id: int,new_operation: OperationCreate,session: AsyncSession = Depends(get_async_session)):
    operation1 = await session.get(operation, operation_id)
    
    if not operation1:
        raise HTTPException(status_code=404, detail="Operation not found")
    
    operation_data = new_operation.dict()
    
    for key, value in operation_data.items():
        setattr(operation1, key, value)

    await session.commit()
    return {"message": "Operation updated"}