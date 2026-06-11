const sio =  io();

sio.on('connect', () => {
    console.log("connected");
    sio.emit('sum', {number : [1 , 2]});
    //sio.emit('command', "vim");
});
sio.on('disconnect', () => {
    console.log("disconnected");
});

sio.on('sum_result', (data) => {
    console.log(data);
});

sio.on('client_count', (count)=> {
    console.log('There are ' +count+ ' connected client.');
})

sio.on('room_count', (count)=> {
    console.log('There are ' +count+ ' clients in my room');
})

sio.on('terminal_output', (data) => {
    console.log(data.data);
})

socket.emit('terminal_input', { input: 'i' });