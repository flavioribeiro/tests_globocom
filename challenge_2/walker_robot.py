#!/usr/sbin/env python
#encoding: utf-8

#L - Virar 90 graus para a esquerda;
#R - Virar 90 graus para a direita;
#M - Mover um ponto para frente;
#T - Se tele transportar para um determinado ponto.

#Considerações:
#east ou west -> move no eixo x
#north ou south -> move no eixo y
# 

class WalkerRobot(object):
    '''
    WalkerRobot can teleport and move on a cartesian plane.
    '''
    def __init__(self, infos, ground):
        self.x, self.y, self.curr_direction = infos
        self.x, self.y = int(self.x), int(self.y)
        self.ground = ground

    def turn(self, command):
        if command == 'L':
            if self.curr_direction == "E": self.curr_direction = "N"
            elif self.curr_direction == "B": self.curr_direction = "W"
            elif self.curr_direction == "W": self.curr_direction = "S"
            elif self.curr_direction == "S": self.curr_direction = "E"
        elif command == 'R':
            if self.curr_direction == "E": self.curr_direction = "S"
            elif self.curr_direction == "S": self.curr_direction = "W"
            elif self.curr_direction == "W": self.curr_direction = "N"
            elif self.curr_direction == "N": self.curr_direction = "E"

    def move(self):
        if self.curr_direction == 'E' or self.curr_direction == 'W':
            if self.can_move((self.x+1, self.y)):
                self.x+=1

        elif self.curr_direction == 'N' or self.curr_direction == 'S':
            if self.can_move((self.x, self.y+1)):
                self.y+=1

    def teleport(self, position):
        self.x = int(position[0])
        self.y = int(position[1])

    def can_move(self, position):
        if position[0] < self.ground.max_x and position[1] < self.ground.max_y:
            return True
        return False

class Ground(object):
    def __init__(self, infos):
        self.max_x, self.max_y = infos
