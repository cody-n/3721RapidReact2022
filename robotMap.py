import wpilib


class RobotMap:
    def __init__(self, robot):
        self.robot = robot
        self.motorMap = MotorMap()
        self.PneumaticMap = PneumaticMap()
        self.ControlMap = ControlMap()

        # add this!
        self.currentConfig = {
            'Fly': {
                'state': True,
                'currentLimit': 25,
                'triggerThresh': 35,
                'time': 0.5
            },
            'Drive': {
                'state': True,
                'currentLimit': 35,
                'triggerThresh': 40,
                'time': 0.5
            }}


class MotorMap:
    def __init__(self):
        self.motors = {}
        self.PWMMotor = {}

        """
        Drive
        """
        # make sure motors have master ports filled
        self.motors['RFDrive'] = {
            'port': 0,
            'inverted': True,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['RMDrive'] = {
            'port': 2,
            'inverted': True,
            'jobType': 'slave',
            'masterPort': 0,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['RBDrive'] = {
            'port': 1,
            'inverted': True,
            'jobType': 'slave',
            'masterPort': 0,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['LFDrive'] = {
            'port': 5,
            'inverted': False,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['LMDrive'] = {
            'port': 4,
            'inverted': False,
            'jobType': 'slave',
            'masterPort': 5,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['LBDrive'] = {
            'port': 3,
            'inverted': False,
            'jobType': 'slave',
            'masterPort': 5,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        """
        Climber Motors
        """
        self.motors['rgtWinch'] = {
            'port': 6,
            'inverted': False,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['lftWinch'] = {
            'port': 7,
            'inverted': True,
            'jobType': 'slave',
            'masterPort': 6,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        """
        Shooter Motors
        """
        """
        self.motors['rgtFly'] = {
            'port': 8,
            'inverted': False,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        self.motors['lftFly'] = {
            'port': 9,
            'inverted': True,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        """


class PneumaticMap:
    def __init__(self):
        self.pistons = {}
        self.OUT = wpilib.DoubleSolenoid.Value.kForward
        self.IN = wpilib.DoubleSolenoid.Value.kReverse
        self.CLOSE = wpilib.DoubleSolenoid.Value.kOff

        """
        Drive Pistons
        """
        self.pistons['dShifter'] = {'portA': 4, 'portB': 7, 'moduleType': 'ctre','Type': 'Double'}      # add module type

        """
        Climber Pistons
        """
        # self.pistons['rgtClimber'] = {'portA': 4, 'portB': 5, 'Type': 'Double'}
        # self.pistons['lftClimber'] = {'portA': 6, 'portB': 7, 'Type': 'Double'}
        """
        Intake Pistons
        """


class ControlMap:
    def __init__(self):

        self.Controller = {}

        self.Controller['xbox'] = {'Id': 0, 'Type': 'xbox', 'jobType': 'main'}
        self.Controller['board'] = {'Id': 1, 'Type': 'custom', 'jobType': 'side'}   # change name here
