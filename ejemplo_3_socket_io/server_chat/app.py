import asyncio
import websockets
import json

active_connections = set()

async def handle_connection(websocket, path):
    active_connections.add(websocket)

    print("conectando un cliente")

    try:
        async for message in websocket:
    
            # mensajes entrantes
            data = json.loads(message)
            print(data)

            if 'event' in data:
                if data['event'] == 'chat_message':
                    await broadcast_message(data['data'], websocket)
            else:
                print(f"Mensaje no válido: {message}")

    except websockets.exceptions.ConnectionClosedError:
        print("error!")

    finally:
        print("cerrando conexiones")
        active_connections.remove(websocket)

async def broadcast_message(data, sender):
    # Envía el mensaje a todos los clientes, excepto al remitente
    for connection in active_connections:
        if connection != sender:
            await connection.send(json.dumps(data))

if __name__ == "__main__":
    server = websockets.serve(handle_connection, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
