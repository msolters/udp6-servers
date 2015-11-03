var PORT = 8808;
var HOST = '';//'fe80::3a2c:4aff:fe6e:19f3%eth0';

var dgram = require('dgram');
var server = dgram.createSocket('udp6');

server.on('listening', function () {
    var address = server.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', function (message, remote) {
    console.log(remote.address + ':' + remote.port +' - ' + message);
});

server.bind(PORT, HOST);
