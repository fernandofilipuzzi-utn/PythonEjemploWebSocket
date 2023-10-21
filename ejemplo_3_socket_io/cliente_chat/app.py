import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Conectado al servidor")

@sio.event
def disconnect():
    print("Desconectado del servidor")

@sio.on("chat_message")
def on_chat_message(data):
    print(f"Mensaje del servidor: {data}")

# Conéctate al servidor
sio.connect("http://localhost:8080")

while True:
    message = input("Mensaje: ")
    if message == "exit":
        break
    sio.emit("chat_message", message)

sio.disconnect()
