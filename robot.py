import wpilib
import typing
from wpilib import SmartDashboard
from commands2 import CommandScheduler
from commands2 import RunCommand
import commands2
from robotMap import RobotMap
from helper import Creator
from commands.teleop import TeleOp
from subsytems.drive import Drive
from oi import OI


class compRobot(commands2.TimedCommandRobot):

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:

        # Initialize utility and subsystem classes
        self.Creator = Creator
        self.RobotMap = RobotMap(self)
        self.oi = OI(self)
        self.drive = Drive(self)
        self.chooser = wpilib.SendableChooser()

        # Initialize commands
        self.teleop = TeleOp(self)

    def getAutonomousCommand(self) -> commands2.Command:
        # return chosen auto from chooser
        return self.chooser.getSelected()

    def disabledInit(self) ->  None:
        """ This function is called once each time robot enters disabled mode"""

    def disabledPeriodic(self) -> None:
        """ This function is called periodically when disabled"""

    def log(self):
        pass

    def autonomousInit(self):
        self.autonomousCommand = self.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        """ This function is called periodically during autonomous"""

    def teleopInit(self):
        if self.autonomousCommand:
            self.autonomousCommand.cancel()
        self.teleop.schedule()

    def teleopPeriodic(self):
        self.teleop.execute()

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == '__main__':
    wpilib.run(compRobot)

