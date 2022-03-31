
import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

import typing

if typing.TYPE_CHECKING:
    from robot import compRobot


class PhysicsEngine:
    """
    Simulates motor movement
    """

    def __init__(self, physics_controller: PhysicsInterface, robot: "compRobot"):
        super().__init__()
        self.physController = physics_controller
        self.bumperw = 3.25 * units.inch

        self.lf_motor = wpilib.simulation.PWMSim(robot.botMap.motorMap.motors['LFDrive']['port'])      # new system dont use hal
        self.rf_motor = wpilib.simulation.PWMSim(robot.botMap.motorMap.motors['RFDrive']['port'])

        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_FALCON_500,    # motor type
            115 * units.lbs,                    # mass
            10.71,                              # drive gear ratio
            3,                                  # motors per side
            (24 * units.inch + 2 * self.bumperw),   # width
            (20 * units.inch + 2 * self.bumperw),   # length
            6 * units.inch,                     # wheel diameter
        )

        # self.gyro = ADXRS450_GyroSim()


    def update_sim(self, now, tm_diff):
        # Simulate the drivetrain (only front motors used because read should be in sync)
        lf_motor = self.lf_motor.getSpeed()
        rf_motor = self.rf_motor.getSpeed()

        transform = self.drivetrain.calculate(lf_motor, rf_motor, tm_diff)
        pose = self.physController.move_robot(transform)

        # Update the gyro simulation
        # -> FRC gyros are positive clockwise, but the returned pose is positive
        #    counter-clockwise
        # self.gyro.setAngle(-pose.rotation().degrees())