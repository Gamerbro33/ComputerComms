# Server side for communication between computer
#import eventlet
import socketio
import random
import os

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './public/'
})
client_count = 0
a_count = 0
b_count = 0


@sio.event
async def confirmation(sid, data):
    #confirmation that it connect to client
    return "OK", 123

@sio.event
async def connect(sid, environ):
    global client_count
    global a_count
    global b_count
    client_count += 1
    print('connect ', sid)
    await sio.emit('client_count', client_count)
    num = random.random()
    print(num)
    if num > 0.5:
        print('enter room a')
        await sio.enter_room(sid, 'a')
        a_count += 1
        await sio.emit('room_count', a_count, to='a')
    else:
        print('enter room b')
        await sio.enter_room(sid, 'b')
        b_count += 1
        await sio.emit('room_count', b_count, to='b')

@sio.event
async def message(sid, data):
    print(f"message From {sid}:, {data}")

    sio.emit('reponse', data)


@sio.event
async def disconnect(sid):
    global client_count
    global a_count
    global b_count
    client_count -= 1
    await sio.emit('client_count', client_count)
    print('disconnect ', sid)
    if 'a' in sio.rooms(sid): 
        a_count -= 1
        await sio.emit('room_count', a_count, to='a')
    else:
        b_count -= 1
        await sio.emit('room_count', b_count, to='b')

@sio.event
async def sum(sid, data):
    print(sid, data)
    result = data['number'][0] + data['number'][1]
    await sio.emit('sum_result', {'result': result}, to=sid)

#@sio.event
#async def command(sid, data):
 #   os.system(data)