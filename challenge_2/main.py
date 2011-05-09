#!/usr/sbin/env python
#encoding: utf-8

import sys
from walker_robot import WalkerRobot, Ground

class Parser(object):
    def __init__(self, input_file):
        self.input_file = open(input_file)

    def get_ground_size(self):
        ground = self.input_file.readline()
        ground = ground.replace('\n','')
        ground = ground.split()
        return (int(ground[0]), int(ground[1]))

    def get_robot_first_pos(self):
        first_pos = self.input_file.readline()
        first_pos = first_pos.replace('\n','')
        first_pos = first_pos.split()
        return (first_pos[2], int(first_pos[0]), int(first_pos[1]))

    def get_command(self):
        for line in self.input_file:
            line = line.replace('\n','')

            if line.startswith("T"):
                line = line.split()
                yield ("T", int(line[1]), int(line[2]))
            else:
                for command in line:
                    if command == "L" or command =="R" or command == "M":
                        yield (command,)

def main():
    if len(sys.argv) < 2:
        raise Exception("missing file")

    p = Parser(sys.argv[1])
    
    ground_size = p.get_ground_size()
    ground = Ground(ground_size[0], ground_size[1])
    
    robot_first_pos = p.get_robot_first_pos()
    robot = WalkerRobot(robot_first_pos[0], robot_first_pos[1], 
                    robot_first_pos[2], ground)

    commands = p.get_command()

    for command in commands:
        if command[0] == 'T':
            robot.teleport(command[1], command[2])
        elif command[0] == 'M':
            robot.move()
        elif command[0] == 'L' or command[0] == 'R':
            robot.turn(command[0])

    print 'final pos:', robot.x, robot.y, robot.curr_direction

if __name__ == "__main__":
    main()
