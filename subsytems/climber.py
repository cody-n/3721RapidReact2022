import wpilib
import ctre
from wpilib.command import Subsystem
from wpilib import DigitalInput


class Climber(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(robot, "Climber")

        self.robot = robot

        motors = {}
        pistons = {}

        self.map = self.robot.RobotMap

        for name in self.map.motorMap.motors:
            motors[name] = self.robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.map.PneumaticMap.pistons:
            pistons[name] = robot.Creator.createPistons(self.map.PneumaticMap.pistons[name])

        self.climbMotors = motors
        self.climbPistons = pistons

        for name in self.climbMotors:
            self.climbMotors[name].setInverted(self.robot.RobotMap.motorMap.motors[name]['setInverted'])
            self.climbMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.motorMap.motors[name]['CurLimit'] is True:
                self.climbMotors[name].configStatorCurrentLimit(self.robot.Creator.CreateCurrentConfig(
                    self.robot.RobotMap.currentConfig['Climber']), 40)

        self.iOut = wpilib.DoubleSolenoid.Value.kForward
        self.iIn = wpilib.DoubleSolenoid.Value.kReverse

    def setClimber(self, power):
        self.climbMotors['rgtWinch'].set(ctre.ControlMode.PercentOutput, power)

    def actuateClimber(self, mode):
        self.climbPistons['rgtClimber'].set(mode)
        self.climbPistons['lftClimber'].set(mode)
