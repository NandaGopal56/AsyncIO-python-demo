import time, asyncio, uvicorn
from fastapi import FastAPI
from datetime import datetime
from anyio import CapacityLimiter
from anyio.lowlevel import RunVar

app = FastAPI()

# https://github.com/tiangolo/fastapi/issues/4221#issuecomment-982260467
@app.on_event("startup")
def startup():
   print("App started...")
   RunVar("_default_thread_limiter").set(CapacityLimiter(1))

@app.get("/sync")
def sync_endpoint():
    '''
    https://github.com/tiangolo/fastapi/discussions/4358
    '''
    print(f'Sync request received!: {datetime.now().strftime("%I:%M:%S %p")}')
    time.sleep(10)
    return {"message": "This is a synchronous endpoint!"}


@app.get("/async")
async def async_endpoint():
    print(f'Async request received!: {datetime.now().strftime("%I:%M:%S %p")}')
    await asyncio.sleep(10)
    # time.sleep(10)
    return {"message": "This is an asynchronous endpoint!"}


@app.get("/async-syncIO")
async def async_endpoint():
    '''
    https://github.com/tiangolo/fastapi/issues/4221#issuecomment-982260467
    '''
    print(f'async-syncIO request received!: {datetime.now().strftime("%I:%M:%S %p")}')
    time.sleep(10) #represent sync IO in async function
    return {"message": "This is an async-syncIO endpoint!"}

if __name__ == "__main__":
    uvicorn.run("main:app", workers=1, reload=True)



'''
python3 -m daphne -b 127.0.0.1 -p 8000 main:app 
python3 -m uvicorn main:app --workers=1 --reload
'''



















