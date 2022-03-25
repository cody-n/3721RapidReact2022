import wpilib
from commands2 import CommandBase


class SetDrivePos(CommandBase):
    def __init__(self, robot, speed, dist, turnDeg):
        super().__init__()
        self.robot = robot

        self.speed = speed
        self.distance = dist
        self.speed = speed
        self.angle = turnDeg
        self.i = 0
        self.s = 0

    def initialize(self) -> None:
        self.robot.drive.resetHeading()
        self.robot.drive.resetEnc()
        self.robot.drive.DrivePID.setPt(0)
        self.robot.drive.DrivePID.limitVal(self.speed)

    def execute(self) -> None:
        turn = self.Drive.DrivePID.outVal(self.Drive.getHeading())
        forward = self.Drive.DrivePID.outVal(self.Drive.getEnc())

    def isFinished(self):
        return False

    def end(self, interrupted: bool) -> None:
        self.i = 0
        self.robot.Drive.stop()
        self.robot.Drive.resetEnc()
