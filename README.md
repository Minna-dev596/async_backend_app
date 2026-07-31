Today Task:
Implement Async Routes & Background Tasks

Explanation:
Converted synchronous FastAPI routes (def) into asynchronous (async def) to enable non-blocking operations.
Configured SQLAlchemy AsyncSession with create_async_engine for non-blocking database queries.
Implemented FastAPI BackgroundTasks to handle heavy operations like email sending and logging without blocking API responses.
Ensured API responses return immediately (200/202) while tasks execute in the background.
Performed concurrency testing using parallel requests to verify low latency and non-blocking performance.
Followed event-loop safety rules by avoiding blocking calls like time.sleep() inside async routes.

Implemented async FastAPI routes, integrated AsyncSession for non-blocking DB queries, and used BackgroundTasks to handle heavy operations without delaying API responses.

Run the Project
pip install fastapi uvicorn sqlalchemy aiosqlite
uvicorn app.main:app --reload

Test Endpoints
Create user:
POST /users/
{
  "name": "Minna",
  "email": "minna@example.com"
}
Get users:
GET /users/
Test async:
GET /fast-response/

📁 Project Structure
async_backend_app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
 ├── crud.py
