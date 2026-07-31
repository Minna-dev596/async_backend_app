from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
import crud, schemas

app = FastAPI()

# Create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Background task
async def send_email(email: str):
    import asyncio
    await asyncio.sleep(5)
    print(f"Email sent to {email}")


# Create user (Async + Background)
@app.post("/users/", response_model=schemas.UserResponse)
async def create_user(
    user: schemas.UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    new_user = await crud.create_user(db, user)
    background_tasks.add_task(send_email, new_user.email)
    return new_user


# Get users
@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)


# Test async performance
@app.get("/fast-response/")
async def fast_response(background_tasks: BackgroundTasks):

    async def heavy_task():
        import asyncio
        await asyncio.sleep(10)
        print("Heavy task done")

    background_tasks.add_task(heavy_task)

    return {"message": "Response sent immediately!"}