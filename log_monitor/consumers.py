import os
import asyncio
import aiofiles
from channels.generic.websocket import AsyncWebsocketConsumer
from collections import deque

LOG_FILE_PATH = "logfile.log"


class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("log_watchers", self.channel_name)
        await self.accept()

        last_lines = await self.get_last_lines(LOG_FILE_PATH, 10)
        await self.send(text_data=last_lines)

        asyncio.create_task(self.monitor_log_file(LOG_FILE_PATH))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("log_watchers", self.channel_name)

    async def monitor_log_file(self, filepath):
        async with aiofiles.open(filepath, mode="r") as f:
            await f.seek(0, os.SEEK_END)  
            while True:
                line = await f.readline()
                if line:
                    await self.channel_layer.group_send(
                        "log_watchers",
                        {
                            "type": "log.message",
                            "message": line
                        }
                    )
                else:
                    await asyncio.sleep(0.1)  

    async def log_message(self, event):
        message = event["message"]
        await self.send(text_data=message)

    async def get_last_lines(self, filepath, num_lines=10):
        async with aiofiles.open(filepath, mode="r") as f:
            lines = deque(await f.readlines(), maxlen=num_lines)
        return "".join(lines)
