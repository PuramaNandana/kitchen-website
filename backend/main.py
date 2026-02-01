from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import contact, designs, services

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Kitchen Studio API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(contact.router)
app.include_router(designs.router)
app.include_router(services.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Kitchen Studio API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
