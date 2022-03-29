import ctre
import wpilib
from ctre import TalonFX
from wpilib import DoubleSolenoid
from wpilib import PneumaticsModuleType
from commands2 import SubsystemBase
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from utilities.PID import PID
from constants import *


class Drive(SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.rgtMid = TalonFX(rgtMMotor)
        self.rgtBack = TalonFX(rgtBMotor)
        self.lftFront = TalonFX(lftFMotor)
        self.lftMid = TalonFX(lftMMotor)
        self.lftBack = TalonFX(lftBMotor)

        self.dShifter = 1   # DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 4, 7)

        self.rEnc = Encoder(0, 1, False, Encoder.EncodingType.k4X)
        self.lEnc = Encoder(2, 3, False, Encoder.EncodingType.k4X)
        self.Gyro = ADXRS450_Gyro

        self.con = wpilib.XboxController(0)
        self.side = wpilib.Joystick(1)

        self.kP = 0.0
        self.kI = 0.0
        self.kD = 0.0

        self.DrivePID = PID(self.kP, self.kI, self.kD)

    def log(self):
        wpilib.SmartDashboard.putNumber('rDrive', self.rEnc.get())
        wpilib.SmartDashboard.putNumber('lDrive', self.lEnc.get())

    def set(self, rgt, lft):
        self.rgtFront.set(ctre.ControlMode.PercentOutput, rgt)
        self.rgtMid.set(ctre.ControlMode.PercentOutput, rgt)
        self.rgtBack.set(ctre.ControlMode.PercentOutput, rgt)
        self.lftFront.set(ctre.ControlMode.PercentOutput, lft)
        self.lftMid.set(ctre.ControlMode.PercentOutput, lft)
        self.lftBack.set(ctre.ControlMode.PercentOutput, lft)

    def setGearing(self, mode):
        self.dShifter.set(mode)

    def stop(self):
        self.set(0, 0)

    def getEnc(self):
        left = self.lEnc.get()
        right = self.rEnc.get()
        return (left + right) / 2

    def getController(self):
        return self.con

    def getSideCon(self):
        return self.side

    def getHeading(self):
        x = self.Gyro.getAngle()
        if x < 360 or x < -360:
            self.Gyro.reset()

        return self.Gyro.getAngle()

    def resetHeading(self):
        self.Gyro.reset()

    def resetEnc(self):
        self.rEnc.reset()
        self.lEnc.reset()

