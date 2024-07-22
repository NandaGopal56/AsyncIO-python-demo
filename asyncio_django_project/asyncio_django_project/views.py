from django.http import JsonResponse
from datetime import datetime
import asyncio, time
import threading

def sync_view(request):
    print(f'Sync request received at {threading.get_ident()}!: {datetime.now().strftime("%I:%M:%S %p")}')
    data = {
        "message": "This is a synchronous endpoint"
    }
    time.sleep(10)
    return JsonResponse(data)

async def async_view(request):
    print(f'Async request received at {threading.get_ident()}!: {datetime.now().strftime("%I:%M:%S %p")}')
    data = {
        "message": "This is an asynchronous endpoint",
    }
    # Simulate an asynchronous operation
    await asyncio.sleep(10)
    return JsonResponse(data)


async def async_syncIO_endpoint(request):
    print(f'async-syncIO request received at {threading.get_ident()}!: {datetime.now().strftime("%I:%M:%S %p")}')
    time.sleep(10) #represent sync IO in async function
    data = {"message": "This is an async-syncIO endpoint!"}
    return JsonResponse(data)