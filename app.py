import os
import redis
import uvicorn
from fastapi import FastAPI

cache = redis.Redis(host="redis", port=6379)
app = FastAPI()
hits = 0

def get_counter_from_cache():
    """
    Checks for the Hits Counter from Redis Cache,
    :return int: count of hits
    :exception str: Description of Error
    """
    retries = 3
    while True:
        try:
            return cache.incr("hits")
        except:
            if retries == 0:
                return "ERROR in Redis"
            retries = retries - 1
            print("retries")

# Create Home Route
@app.get("/")
def get_home():
    return {"api_version":"1.0"}

# Get Environment Variables
@app.get("/envs")
def get_envs():
    return {
        "USERNAME":os.environ.get("DB_USERNAME"),
        "PASSWORD":os.environ.get("DB_PASSWORD"),
        "DB_URL":os.environ.get("DB_URL"),
        }

# Route to Get Page Visits/Hits Count
@app.get("/hits_count")
def get_hits_count():
    # global hits
    # Retries Counter
    
    hits = get_counter_from_cache()
    if isinstance(hits, str) and "ERROR" in hits:
        return {"response":"I am Facing en Error  ::  ".format(str(hits))}
    else:
        return {"response":"I have been seen {} times".format(str(hits))}

# Run Server
uvicorn.run(app, host="0.0.0.0", port=80)