# Server side for communication between computer
#import eventlet
import socketio
import subprocess
import os

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)



@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.event
def sum(sid, data):
    print(sid, data)
    result = data['number'][0] + data['number'][1]
    sio.emit('sum_result', {'result': result}, to=sid)