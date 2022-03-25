import ctre
import wpilib
from wpilib import DoubleSolenoid
from commands2 import SubsystemBase
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from utilities.PID import PID


class Drive(SubsystemBase):
    def __init__(self, robot):

        super().__init__()

        self.robot = robot

        motors = {}
        pistons = {}

        self.map = self.robot.botMap
        self.rEnc = Encoder(0, 1, False, Encoder.EncodingType.k4X)
        self.lEnc = Encoder(2, 3, False, Encoder.EncodingType.k4X)
        self.Gyro = ADXRS450_Gyro

        for name in self.map.motorMap.motors:
            motors[name] = self.robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.robot.botMap.PneumaticMap.pistons:
            if name == 'dShifter':
                pistons[name] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons[name])
        self.driveMotors = motors
        self.dPistons = pistons

        for name in self.driveMotors:
            self.driveMotors[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.driveMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.motorMap.motors[name]['CurLimit'] is True:
                self.driveMotors[name].configStatorCurrentLimit(self.robot.Creator.CreateCurrentConfig(
                    self.robot.botMap.currentConfig['Drive']), 40)

        self.kP = 0.0
        self.kI = 0.0
        self.kD = 0.0

        self.DrivePID = PID(self.kP, self.kI, self.kD)

    def log(self):
        wpilib.SmartDashboard.putNumber('rDrive', self.rEnc.get())
        wpilib.SmartDashboard.putNumber('lDrive', self.lEnc.get())

    def set(self, rgt, lft):
        self.driveMotors['RFDrive'].set(ctre.ControlMode.PercentOutput, rgt)
        self.driveMotors['LFDRIVE'].set(ctre.ControlMode.PercentOutput, lft)

    def setGearing(self, mode):
        self.dPistons['dShifter'].set(mode)

    def stop(self):
        self.set(0, 0)

    def getEnc(self):
        left = self.lEnc.get()
        right = self.rEnc.get()
        return (left + right) / 2

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

