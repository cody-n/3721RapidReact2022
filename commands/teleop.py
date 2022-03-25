import wpilib
from commands2 import CommandBase


class TeleOp(CommandBase):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot

        self.controller = robot.oi.getMainController()
        self.sideCon = robot.oi.getSideController()

    def execute(self):
        y = -self.controller.getY(self.controller.Hand.kLeftHand)
        x = -self.controller.getX(self.controller.Hand.kRightHand)

        rgtArc = y - x
        lftArc = y + x

        if abs(rgtArc) < 0.05:
            rgtArc = 0
        if abs(lftArc) < 0.05:
            lftArc = 0

        # self.robot.Drive.set(lftArc, rgtArc)

    def isFinished(self):
        return False


