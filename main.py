#!/usr/bin/env python3

import aioesphomeapi
import asyncio
import os
import boto3
from datetime import datetime

hostname = os.getenv('ESPHOST', 'localhost')
port = os.getenv('ESPPORT', 6053)
password = os.getenv('ESPPASSWORD')
bucket = os.getenv('S3BUCKET')


async def main(s3):
    loop = asyncio.get_running_loop()
    cli = aioesphomeapi.APIClient(loop, hostname, port, password, keepalive=1)

    await cli.connect(login=True)

    def cb(state):
        time = datetime.now().strftime('%s')
        print(f"[{time}] Capturing to {bucket}/{time}.png")
        object = s3.Object(bucket, f"{time}.png")
        object.put(Body=state.image)

    await cli.subscribe_states(cb)

loop = asyncio.get_event_loop()
s3 = boto3.resource('s3')
try:
    asyncio.ensure_future(main(s3))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
