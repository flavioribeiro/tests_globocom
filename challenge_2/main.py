#!/usr/sbin/env python
#encoding: utf-8

import sys
from walker_robot import WalkerRobot, Ground

def main():
    if len(sys.argv) < 2:
        raise Exception("missing file")

    _input = open(sys.argv[1])
    ground = Ground(_input.readline().replace("\n","").split())
    robot = WalkerRobot(_input.readline().replace("\n","").split(), ground)

    for line in _input:
        line = line.replace("\n","")

        if line.startswith("T"):
            robot.teleport(line.split()[1:])

        else:
            for command in line:
                if command == "L" or command == "R":
                    robot.turn(command)
                elif command == "M":
                    robot.move()
                else:
                    raise Exception("Deu águia")
    print 'Posicao final:', robot.x, robot.y, robot.curr_direction

if __name__ == "__main__":
    main()
