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
        self.x, self.y, self.current_direction = infos
        self.ground = ground
        print 'criando um robô com a posicao', self.x, self.y, self.current_direction

    def turn(self, direction):
        print "turnin'", direction

    def move(self):
        print "movin'"

    def teleport(self, position):
        print "wooooP teleportin'", position


class Ground(object):
    def __init__(self, infos):
        self.max_x, self.max_y = infos
