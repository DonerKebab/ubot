#!/usr/bin/python
import re
import sys


def move(command, current_state):

    current_direction = current_state['current_direction']
    x = current_state['x']
    y = current_state['y']

    steps = re.findall(r'\d+', command)

    if steps:
        steps = int(steps[0])
        if current_direction == 'N':
            y += steps
        elif current_direction == 'S':
            y -= steps
        elif current_direction == 'W':
            x -= steps
        elif current_direction == 'E':
            x += steps

    return {'x': x, 'y': y, 'current_direction': current_direction}

def change_direction(command, current_direction):

    direction_mapping = {
        'NR': 'E',
        'NL': 'W',
        'WR': 'N',
        'WL': 'S',
        'ER': 'S',
        'EL': 'N',
        'SR': 'W',
        'SL': 'E'
    }

    for char in command:
        if char == 'W':
            return current_direction

        current_direction = direction_mapping[current_direction + command[-1]]

    return current_direction



def process_command(input):
    current_state = {
        'x': 0,
        'y': 0,
        'current_direction': 'N'
    }
    temp = ''
    for charactor in input:

        if charactor in ['L', 'R']:
            if temp:
                current_state = move(temp, current_state)
                temp = ''
            current_state['current_direction'] = change_direction(charactor, current_state['current_direction'])
            continue

        temp += charactor

    if temp:
        current_state = move(temp, current_state)

    return current_state


if __name__ == '__main__':

    input = sys.argv[1]
    direction = {
        'S': 'South',
        'N': 'North',
        'W': 'West',
        'E': 'East'
    }
    current_state = process_command(input)

    print('X: {X} Y: {Y} Direction: {DIRECTION}'.format(X=current_state['x'], Y=current_state['y'], DIRECTION=direction[current_state['current_direction']]))
