# start.py
import os
import uvicorn

if __name__ == "__main__":
    # Get port from environment variable or use 8000 as default
    port = int(os.environ.get("PORT", 8000))
    
    # Print startup information
    print(f"Starting server on port {port}")
    
    # Start the FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=port)