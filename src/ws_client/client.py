import asyncio
import websockets
import json
 
async def test():
    async with websockets.connect('ws://127.0.0.1:8000/ws/chat/room/1/') as websocket:
        await websocket.send(json.dumps({'message': 'hello'}))
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())
