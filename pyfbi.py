import struct
import os
import sys
import socket
import shutil
import argparse


def argparser():
    parser = argparse.ArgumentParser(description='A Python FBI client to install .cia files to 3DS via network')
    parser.add_argument('ip', help='Destination 3DS IP address with FBI listening')
    parser.add_argument('file', nargs='*', help='CIA file to be sent')
    parser.add_argument('-p', '--port', help='Custom FBI listening port, default to be 5000')
    return parser


def send_file(file_list, ip, port):
    file_count = len(file_list)
    file_count_msg = struct.pack('>L', file_count)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(file_count_msg)
    for file_name in file_list:
        ack = sock.recv(1)
        if ack == b'\x01':
            file_size = os.path.getsize(file_name)
            file_size_msg = struct.pack('>Q', file_size)
            sock.send(file_size_msg)
            with open(file_name, 'rb') as f:
                # sock_file = sock.makefile('wb')
                # shutil.copyfileobj(f, sock_file)
                while True:
                    chunk = f.read(131072)
                    if not chunk:
                        break
                    yield (file_name, sock.send(chunk) / file_size * 100)
        else:
            sys.exit('Operation cancelled by FBI')


def progress_bar(msg, progress):
    sys.stdout.write('%-71s%3d%%\r' % (msg, progress))
    sys.stdout.flush()
    if progress >= 100:
        sys.stdout.write('\n')


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()
    file_list = args.file
    DEVICE_IP = args.ip
    if args.port:
        FBI_PORT = args.port
    else:
        FBI_PORT = 5000
    try:
        # send_file(file_list, DEVICE_IP, FBI_PORT)
        progress = 0
        for chunk_report in send_file(file_list, DEVICE_IP, FBI_PORT):
            progress += chunk_report[1]
            progress_bar(chunk_report[0], progress)
    except ConnectionRefusedError as e:
        sys.exit('%s\nIs FBI running?' % e)
    except ConnectionResetError as e:
        sys.exit('%s\nConnection was closed by FBI.' % e)
    except OSError as e:
        sys.exit('%s\nNo route to host.' % e)
