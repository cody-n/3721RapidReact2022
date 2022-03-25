
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

        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_FALCON_500,    # motor type
            115 * units.lbs,                    # mass
            10.71,                              # drive gear ratio
            3,                                  # motors per side
            (24 * units.inch + 2 * self.bumperw),   # width
            (20 * units.inch + 2 * self.bumperw),   # length
            6 * units.inch,                     # wheel diameter
        )

    def update_sim(self, hal_data, now, tm_dif):
        lf_motor = -hal_data['CAN'][0]['value']
        rf_motor = hal_data['CAN'][3]['value']