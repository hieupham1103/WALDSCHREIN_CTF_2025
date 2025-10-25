import sys
import socket
import re
import argparse

QUESTION_RE = re.compile(rb"Question\s+\d+:\s*(-?\d+)\s*([+\-*])\s*(-?\d+)")


def compute_answer(a: int, op: bytes, b: int) -> int:
    if op == b'+':
        return a + b
    if op == b'-':
        return a - b
    if op == b'*' or op == b'x':
        return a * b
    raise ValueError(f"unknown op: {op!r}")


def interact(host: str, port: int, timeout: float = 5.0):
    with socket.create_connection((host, port), timeout=timeout) as s:
        s.settimeout(8.0)
        buf = b""
        # receive loop
        while True:
            try:
                data = s.recv(4096)
            except socket.timeout:
                print("Socket timeout, exiting", file=sys.stderr)
                break
            if not data:
                break
            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()

            # append incoming data and only process new bytes
            old_len = len(buf)
            buf += data
            # look for question lines and answer them as soon as possible
            for m in QUESTION_RE.finditer(buf):
                if m.start() < old_len:
                    # this match was already processed in a previous recv
                    continue
                a = int(m.group(1))
                op = m.group(2)
                b = int(m.group(3))
                ans = compute_answer(a, op, b)
                # send answer (as decimal with newline)
                out = (str(ans) + "\n").encode()
                s.sendall(out)
                print(f"=> answered: {a} {op.decode()} {b} = {ans}")
            # trim buffer to last 1024 bytes to avoid unbounded growth while
            # keeping enough context for regexp matches that cross recv boundaries
            if len(buf) > 1024:
                buf = buf[-1024:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    try:
        interact(args.host, args.port)
    except KeyboardInterrupt:
        print('\nInterrupted')


if __name__ == '__main__':
    main()
