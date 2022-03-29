import wpilib
import math
from commands2 import CommandBase
from subsytems.drive import Drive


class SetDrivePos(CommandBase):
    def __init__(self, drive: Drive, speed, dist, turnDeg):
        super().__init__()
        self.drive = drive
        self.speed = speed
        self.distance = dist
        self.speed = speed
        self.angle = turnDeg
        self.i = 0
        self.s = 0

    def initialize(self) -> None:
        self.drive.resetHeading()
        self.drive.resetEnc()
        self.drive.DrivePID.setPt(0)
        self.drive.DrivePID.limitVal(self.speed)

    def execute(self) -> None:
        turn = self.drive.DrivePID.outVal(self.Drive.getHeading())
        forward = self.Drive.DrivePID.outVal(self.Drive.getEnc())

        rgt = forward - turn
        lft = forward + turn

        self.drive.set(rgt, lft)

        if abs(rgt) < 0.1 or rgt:
            self.i += 1

    def isFinished(self) -> bool:
        if self.i > 10:
            return True
        else:
            return False

    def end(self, interrupted: bool) -> None:
        self.i = 0
        self.drive.stop()
        self.drive.resetEnc()
