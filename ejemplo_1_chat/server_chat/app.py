import asyncio
import websockets

# Lista de conexiones activas
active_connections = set()

async def echo(websocket, path):
    # Cuando un cliente WebSocket se conecta, lo agregamos a la lista de conexiones activas.
    active_connections.add(websocket)
    try:
        async for message in websocket:
            # Iteramos sobre todas las conexiones activas y enviamos el mensaje a cada una.
            for connection in active_connections:
                await connection.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # Cuando un cliente WebSocket se desconecta, lo eliminamos de la lista de conexiones activas.
        active_connections.remove(websocket)

# Iniciar el servidor WebSocket
start_server = websockets.serve(echo, "localhost", 8082)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
