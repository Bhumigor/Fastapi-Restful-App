from fastapi import FastAPI
from routes.user import user  
import uvicorn

app = FastAPI()

# Include the User Router
app.include_router(user, prefix="/users", tags=["Users"])




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)