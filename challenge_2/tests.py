#!/usr/sbin/env python
#encoding: utf-8

import pytest
from walker_robot import WalkerRobot, Ground
from main import Parser

def test_ground_size():
    g = Ground(10,10)
    assert g.max_x == 10
    assert g.max_y == 10

def test_walker_bot_creation():
    g = Ground(10,10)
    bot = WalkerRobot("E", 1, 1, g)
    assert type(bot) == WalkerRobot

def test_walker_bot_turn():
    g = Ground(10,10)
    bot = WalkerRobot("E", 1, 1, g)
    bot.turn("R")
    assert bot.curr_direction == "S"
    bot.turn("R")
    assert bot.curr_direction == "W"
    bot.turn("R")
    assert bot.curr_direction == "N"
    bot.turn("R")
    assert bot.curr_direction == "E"
    bot.turn("L")
    assert bot.curr_direction == "N"
    bot.turn("L")
    assert bot.curr_direction == "W"
    bot.turn("L")
    assert bot.curr_direction == "S"
    bot.turn("L")
    assert bot.curr_direction == "E"

def test_walker_bot_move():
    g = Ground(10,10)
    bot = WalkerRobot("E",1,1,g)
    bot.move()
    assert bot.x == 2
    bot.move()
    assert bot.x == 3
    bot.turn("R")
    bot.move()
    assert bot.y == 2
    bot.move()
    assert bot.y == 3

def test_walker_bot_teleport():
    g = Ground(10,10)
    bot = WalkerRobot("E",1,1,g)
    bot.teleport(4,4)
    assert bot.x == 4
    assert bot.y == 4

def test_walker_bot_teleport_to_wrong_place():
    g = Ground(10,10)
    bot = WalkerRobot("E", 1, 1,g)
    with pytest.raises(Exception):
        bot.teleport(1000,10000)

def test_walker_bot_move_to_wrong_place():
    g = Ground(1,1)
    bot = WalkerRobot("E", 1,1,g)
    with pytest.raises(Exception):
        bot.move()

def test_parser_creation():
    p = Parser("commands.txt")
    assert type(p) == Parser

def test_parser_get_ground_size_and_robot_first_pos():
    p = Parser("commands.txt")
    ground_size = p.get_ground_size()
    assert (10,10) == ground_size
    robot_first_pos = p.get_robot_first_pos()
    assert ("N", 2, 5) == robot_first_pos

