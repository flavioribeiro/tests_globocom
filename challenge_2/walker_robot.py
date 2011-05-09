#!/usr/sbin/env python
#encoding: utf-8

#L - Virar 90 graus para a esquerda;
#R - Virar 90 graus para a direita;
#M - Mover um ponto para frente;
#T - Se tele transportar para um determinado ponto.

#Considerações:
#east ou west -> move no eixo x
#north ou south -> move no eixo y

class WalkerRobot(object):
    '''
    WalkerRobot can teleport and move on a cartesian plane.
    '''
    def __init__(self, direction, x, y, ground):
        self.curr_direction, self.x, self.y  = direction, x, y
        self.ground = ground

    def turn(self, command):
        if command == 'L':
            if self.curr_direction == "E": self.curr_direction = "N"
            elif self.curr_direction == "N": self.curr_direction = "W"
            elif self.curr_direction == "W": self.curr_direction = "S"
            elif self.curr_direction == "S": self.curr_direction = "E"
        elif command == 'R':
            if self.curr_direction == "E": self.curr_direction = "S"
            elif self.curr_direction == "S": self.curr_direction = "W"
            elif self.curr_direction == "W": self.curr_direction = "N"
            elif self.curr_direction == "N": self.curr_direction = "E"

    def move(self):
        if self.curr_direction == 'E' or self.curr_direction == 'W':
            if self.can_move(x=self.x+1):
                self.x+=1
            else:
                raise Exception("Could not move to that position")

        elif self.curr_direction == 'N' or self.curr_direction == 'S':
            if self.can_move(y=self.y+1):
                self.y+=1
            else:
                raise Exception("Could not move to that position")

    def teleport(self, to_x, to_y):
        if self.can_move(x=to_x, y=to_y):
            self.x = to_x
            self.y = to_y
        else:
            raise Exception("Could not teleport to that position")

    def can_move(self, x=None, y=None):
        if x and x <= self.ground.max_x or y and y <= self.ground.max_y:
            return True
        return False

class Ground(object):
    def __init__(self, x, y):
        self.max_x = x
        self.max_y = y
