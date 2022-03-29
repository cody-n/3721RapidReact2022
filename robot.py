import wpilib
import typing
from wpilib import SmartDashboard
from commands2 import CommandScheduler
from commands2 import RunCommand
import commands2
from commands.teleop import TeleOp
from robotContainer import RobotContainer


class compRobot(commands2.TimedCommandRobot):

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        # Initialize utility and subsystem classes
        self.container = RobotContainer()

    def disabledInit(self) ->  None:
        """ This function is called once each time robot enters disabled mode"""

    def disabledPeriodic(self) -> None:
        """ This function is called periodically when disabled"""

    def log(self):
        pass

    def autonomousInit(self):
        self.autonomousCommand = self.container.getAutonomousCommand()
        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        """ This function is called periodically during autonomous"""

    def teleopInit(self):
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self):
        self.container.tele.execute()


    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == '__main__':
    wpilib.run(compRobot)

