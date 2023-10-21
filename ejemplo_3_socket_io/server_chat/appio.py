import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# Lista de usuarios conectados
connected_users = set()

@sio.event
def connect(sid, environ):
    print(f"Usuario conectado: {sid}")
    connected_users.add(sid)

@sio.event
def disconnect(sid):
    print(f"Usuario desconectado: {sid}")
    connected_users.discard(sid)

@sio.on("chat_message")
def handle_message(sid, data):
    print(f"Mensaje recibido de {sid}: {data}")
    # Enviar el mensaje a todos los usuarios, excepto al remitente
    for user in connected_users:
        if user != sid:
            sio.emit("chat_message", data, room=user)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), app)
