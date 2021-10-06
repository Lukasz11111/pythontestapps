#!/usr/bin/env python3

#     \\
#     (o>
#     //\
# ____V_/____
#     ||
#     ||

# Its not dead, its just resting.

import threading
import os
import select
import socket
import struct
import sys

MAX_RECV_SIZE = 4096 * 1024 * 1024


class Record:
    def serve(self, connect, listen, fnm, num):
        with socket.socket() as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(listen)
            sock.listen()

            idx = 0

            try:
                while True:
                    threading.Thread(target = self.handle, args = (*sock.accept(), connect, f'{fnm}_{idx:04d}.cracker')).start()

                    idx += 1

                    if idx == num:
                        break

            except KeyboardInterrupt:
                pass

    def handle(self, clt, addr, connect, fnm):  # unnecessary async stuff, but easier than select
        with clt, socket.socket() as svr, open(fnm, 'wb') as file:
            svr.connect(connect)

            while True:
                rd, _, err = select.select((clt, svr), (), (clt, svr))

                if err:
                    pass  # TODO: this

                if clt in rd:
                    data = clt.recv(MAX_RECV_SIZE)

                    file.write(struct.pack('<is', len(data), b'C'))
                    file.write(data)

                    if not data:
                        break

                    svr.sendall(data)

                if svr in rd:
                    data = svr.recv(MAX_RECV_SIZE)

                    file.write(struct.pack('<is', len(data), b'S'))
                    file.write(data)

                    if not data:
                        break

                    clt.sendall(data)

            # TODO: handle exceptions

            try:
                clt.shutdown(socket.SHUT_RDWR)
            except (socket.error, OSError, ValueError):
                pass

            clt.close()

            try:
                svr.shutdown(socket.SHUT_RDWR)
            except (socket.error, OSError, ValueError):
                pass

            svr.close()


class Replay(threading.Thread):
    def __init__(self, connect, fnm):
        threading.Thread.__init__(self)

        self.connect = connect
        self.fnm     = fnm
        self.success = False

        self.start()

    def run(self):
        with open(self.fnm, 'rb') as file, socket.socket() as svr:
            svr.connect(self.connect)

            while True:
                size, side = struct.unpack('<ic', file.read(5))

                if not size:
                    if not file.read():
                        self.success = True

                    break

                fdata = file.read(size)

                if side == b'C':  # client send to server
                    svr.sendall(fdata)

                else:  # side == b'S'
                    data = b''

                    while len(data) != size:
                        data += svr.recv(size - len(data))

                    if data != fdata:
                        break

            # TODO: handle exceptions

            try:
                svr.shutdown(socket.SHUT_RDWR)
            except (socket.error, OSError, ValueError):
                pass

            svr.close()



if __name__ == '__main__':
    import argparse

    def parse_addr(addr, default_host, default_port):
        host, port = addr.rsplit(':', 1)

        return (host or default_host), ((port and int(port)) or default_port)

    parser  = argparse.ArgumentParser(description = 'record a revdebug client / server connection(s) or replay to the server to verify')

    parser.add_argument('file', nargs = '*', help = 'if these are present then they are the files to attempt to replay to the server, otherwise records')

    parser.add_argument('-c', '--connect', default = ':', help = 'address of revdebug devops server, default: 127.0.0.1:42734')
    parser.add_argument('-l', '--listen', default = ':', help = 'address to listen on for incoming client connections, default: 0.0.0.0:42730')
    parser.add_argument('-f', '--fnm', default = 'recording', help = 'set filename for recording(s)')
    parser.add_argument('-n', '--num', default = 0, type = int, help = 'set number of recordings to receive before exit, default: 0 (infinity)')

    args    = parser.parse_args()
    listen  = parse_addr(args.listen, '0.0.0.0', 8998)
    connect = parse_addr(args.connect, '20.199.127.147', 42734)

    listen  = (os.environ.get('POLLY_LISTEN_HOST', listen[0]), int(os.environ.get('POLLY_LISTEN_PORT', listen[1])))
    connect = (os.environ.get('POLLY_CONNECT_HOST', connect[0]), int(os.environ.get('POLLY_CONNECT_PORT', connect[1])))

    exit    = 0

    if not args.file:
        Record().serve(connect, listen, args.fnm, args.num)

    else:
        replays = [Replay(connect, fnm) for fnm in args.file]

        for replay in replays:
            replay.join()

            if not replay.success:
                print(f'failed to verify: {replay.fnm}')

                exit = 1

    sys.exit(exit)
