from fastapi import FastAPI
from app.routers import songs, auth, recommend

app = FastAPI(title="MoodMusic")

app.include_router(auth.router, prefix="/auth")
app.include_router(songs.router, prefix="/songs")
app.include_router(recommend.router, prefix="/mood")
