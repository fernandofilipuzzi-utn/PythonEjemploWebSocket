import asyncio
import websockets
import json

# Lista de conexiones activas
active_connections = set()

async def echo(websocket, path):
   
    active_connections.add(websocket)

    print("on conectado")

    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                print(data)
                await websocket.send(json.dumps(data))
                print("enviado....")
            except:
                print("error", message)
    except:
        print("error") 
    finally:
        print("cerrando conexión")
        active_connections.remove(websocket)

    # data = {
    #     'id': 1        
    # }

    # websocket.send(json.dumps(data))

    # try:
    #     async for message in websocket:
    #         try:
    #             data = json.loads(message)
                
    #             #if 'usuario' in data and 'mensaje' in data and 'IDmensaje' in data:
    #                 # enviando mensajes a todos los clientes

    #             print(data)

    #             for connection in active_connections:
    #                 await connection.send(json.dumps(data))

    #         except json.JSONDecodeError:
    #             print("Mensaje no válido:", message)

    # except websockets.exceptions.ConnectionClosedError:
    #     pass
    # finally:
    #     # se cierran las conexiones activas
    #     active_connections.remove(websocket)

# inicio del servicio
start_server = websockets.serve(echo, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
