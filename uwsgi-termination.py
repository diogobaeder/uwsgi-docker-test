#!/usr/bin/env python
import signal
import time


ITERATION_SLEEP = .1
WAIT_BEFORE_FINISH = 3


running = True


def main():
    print(f'Starting main')
    signal.signal(signal.SIGTERM, handle)
    signal.signal(signal.SIGINT, handle)
    signal.signal(signal.SIGQUIT, handle)
    while running:
        time.sleep(ITERATION_SLEEP)
    print('Stopping now.')


def handle(signum, frame):
    global running
    if not running:
        print(f'Not running anymore')
        return
    print(f'Handling signal: {signum}')
    running = False
    print(f'Waiting for {WAIT_BEFORE_FINISH} before finishing to handle')
    time.sleep(WAIT_BEFORE_FINISH)


if __name__ == '__main__':
    main()
