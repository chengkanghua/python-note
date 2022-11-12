# coding=utf-8

from twisted.internet import reactor
from robot import RobotClient


if __name__ == '__main__':
    # input_thread.start()
    # reactor.suggestThreadPoolSize(100)
    for i in range(0, 1):
        user_id = 1
        robot = RobotClient("robot_4.json")
        # reactor.callInThread(robot.run)
        reactor.callInThread(robot.run)
    reactor.run()

