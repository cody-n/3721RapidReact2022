import wpilib
from commands2 import CommandBase
from subsytems.drive import Drive

class TeleOp(CommandBase):
    def __init__(self, drive: Drive):
        super().__init__()

        self.drive = Drive
        self.con = Drive.getController(self)
        self.side = Drive.getSideCon(self)

    def execute(self):

        y = -self.controller.getY(self.controller.Hand.kLeftHand)
        x = -self.controller.getX(self.controller.Hand.kRightHand)

        rgtArc = y - x
        lftArc = y + x

        if abs(rgtArc) < 0.05:
            rgtArc = 0
        if abs(lftArc) < 0.05:
            lftArc = 0

        self.drive.set(rgtArc, lftArc)


    def isFinished(self):
        return False


