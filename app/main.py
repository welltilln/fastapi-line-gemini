import os
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from app.bank_parser import parse_bank_message
from app.mail_sniffer import monitor_email
import sys

# Path to Yosafe project for database models
yosafe_path = os.getenv("YOSAFE_PATH", "/Users/welltilln/Projects/Yosafe")
sys.path.append(yosafe_path)
import database as yosafe_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    try:
        yosafe_db.initialize_db()
        print("📁 Yosafe database initialized.")
        
        # Start Silent Mail Sniffer in background
        sniffer_task = asyncio.create_task(monitor_email())
        yield
        # Shutdown logic (optional)
        sniffer_task.cancel()
        try:
            await sniffer_task
        except asyncio.CancelledError:
            pass
    except Exception as e:
        print(f"⚠️ Error during startup: {e}")
        yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Yosafe Silent Input Engine is running"}

if __name__ == "__main__":
    import uvicorn
    import logging

    # Disable uvicorn access logs for cleaner terminal output
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
    port = 8000
    print("\n" + "="*60)
    print("🚀 YOSAFE SILENT INPUT ENGINE STARTED!")
    print(f"🕵️ Monitoring emails and updating {yosafe_db.DB_PATH}")
    print("="*60 + "\n")
    
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")
