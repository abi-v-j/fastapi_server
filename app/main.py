from app.routes import user_routes  # Import user routes
from fastapi import FastAPI
from app.database import connect_to_mongo, close_mongo_connection
from mangum import Mangum  # For AWS Lambda/ASGI compatibility with Vercel

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/api/v1/users", tags=["Users"])

# Connect to MongoDB on app startup
@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

# Close MongoDB connection on app shutdown
@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}


handler = Mangum(app)
