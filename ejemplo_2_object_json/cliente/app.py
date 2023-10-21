import asyncio
import websockets
import json
 
async def recv():
    async with websockets.connect('ws://localhost:8080') as websocket:
        response = await websocket.recv()
        print(response)

async def send():
    async with websockets.connect('ws://localhost:8080') as websocket:
        while(True):
            mensaje=input("mensaje:")
            data={'IDmensaje':1, 'usuario': "fernando", 'mensaje':mensaje}
            await websocket.send(json.dumps(data))
            print("enviado")        
 
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(send(), recv()))