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
    def __init__(self, robot) -> None:
        super().__init__()

        self.robot = robot
        motors = {}
        pistons = {}

        self.map = self.robot.botMap()
        self.rEnc = Encoder(0, 1, False, Encoder.EncodingType.k4X)
        self.lEnc = Encoder(2, 3, False, Encoder.EncodingType.k4X)
        self.Gyro = ADXRS450_Gyro

        for name in self.map.motorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.robot.botMap.PneumaticMap.pistons:
            if name == 'Shifter':
                pistons[name] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons[name])

        self.dMotors = motors
        self.dPistons = pistons

        for name in self.dMotors:
            self.dMotors[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.dMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.motorMap.motors[name]['CurLimit'] is True:
                self.dMotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Drive']), 40)


        self.kP = 0.0
        self.kI = 0.0
        self.kD = 0.0

        self.DrivePID = PID(self.kP, self.kI, self.kD)

    def log(self):
        wpilib.SmartDashboard.putNumber('rDrive', self.rEnc.get())
        wpilib.SmartDashboard.putNumber('lDrive', self.lEnc.get())

    def set(self, rgt, lft):
        self.dMotors['RFDrive'].set(ctre.ControlMode.PercentOutput, rgt)
        self.dMotors['LFDrive'].set(ctre.ControlMode.PercentOutput, lft)

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

