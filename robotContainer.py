import wpilib
from wpilib.interfaces import GenericHID
from constants import *
import commands2
import rev
from rev import CANSparkMaxLowLevel
from ctre import TalonSRX
from ctre import VictorSPX
from ctre import TalonFX
from ctre import StatorCurrentLimitConfiguration
from rev import CANSparkMax
from wpilib import VictorSP
from wpilib import Joystick
from wpilib import XboxController
from wpilib import DoubleSolenoid
from wpilib import Encoder
from wpilib import Solenoid
from subsytems.drive import Drive
from commands.teleop import TeleOp
from commands.setDrivePos import SetDrivePos
import ctre


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self.Controller = wpilib.XboxController(main)
        self.side = wpilib.Joystick(side)

        # Drive Motors
        self.rgtFrontDrive = TalonFX(rgtFMotor)
        self.rgtMidDrive = TalonFX(rgtMMotor)
        self.rgtBackDrive = TalonFX(rgtBMotor)
        self.lftFrontDrive = TalonFX(lftFMotor)
        self.lftMidDrive = TalonFX(lftMMotor)
        self.lftBackDrive = TalonFX(lftBMotor)

        # Winch Motors
        self.lftWinch = TalonFX(lftWinchMotor)
        self.rgtWinch = TalonFX(rgtWinchMotor)

        # Shooter Motors
        self.rgtFly = TalonFX(rgtFlyMotor)
        self.lftFly = TalonFX(lftFlyMotor)

        # Conveyor + intake Motors
        self.intake = CANSparkMax(intake, CANSparkMaxLowLevel.MotorType.kBrushless)
        self.botConveyor = TalonSRX(botConveyor)
        self.indexer = TalonSRX(indexerMotor)

        # Reverse Motors
        self.rgtFrontDrive.setInverted(True)
        self.rgtMidDrive.setInverted(True)
        self.rgtBackDrive.setInverted(True)
        self.lftWinch.setInverted(True)
        self.lftFly.setInverted(True)

        # Pneumatic Stuff
        self.gearShift = DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 4, 7)
        self.angler = DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 1, 6)
        self.lftFlyAngle = 2
        self.rgtFlyAngle = 5

        # Subsytem stuff
        self.drive = Drive()
        # Autonomous Stuff
        self.chooser = wpilib.SendableChooser

        self.simple = SetDrivePos(self.drive, 0.5, 100, 0)
        self.tele = TeleOp(self.drive)


    def getAutonomousCommand(self) -> commands2.Command:
        # return chosen auto from chooser
        return self.chooser.getSelected()
