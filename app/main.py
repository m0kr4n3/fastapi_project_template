import uvicorn
import logging

from src.db.init_db import init_db
from src.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




if __name__ == "__main__":
        
    logger.info("Creating initial data")
    db = SessionLocal()
    init_db(db)
    logger.info("Initial data created")
    
    uvicorn.run("src.api.api:api_router", host="0.0.0.0", port=8080, reload=True)
