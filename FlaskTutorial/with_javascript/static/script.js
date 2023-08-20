//let socket = io.connect('http://localhost:5000')
const socket = io('http://localhost:5000')

socket.on('connect' function{
        socket.send('I am working');
});
