import asyncio
import websockets
import json
 
async def chat(message):
    async with websockets.connect('ws://127.0.0.1:8000/ws/chat/room/1/') as websocket:
        await websocket.send(json.dumps({'message': message}))
        response = await websocket.recv()
        return response
 
asyncio.get_event_loop().run_until_complete(chat('hello'))
