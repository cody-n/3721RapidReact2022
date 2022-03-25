
class PID(object):
    def __init__(self, kp, ki, kd, kf = 0):
        super().__init__()

        # Initialize Class variables

        self.kp = kp    # Constants
        self.ki = ki
        self.kd = kd
        self.kf = kf

        self.pastErr = 0

        self.p = 0  # P I D components
        self.i = 0
        self.d = 0

        self.output = 0
        self.outputVel = 0
        self.Des = 0
        self.Error = 0
        self.aError = 0
        self.limit = 0
        self.maxIn = 0
        self.maxOut = 0

    def setPt(self, setpoint):
        """
        set the setpt of your pid object
        :param setpoint: where you want to go
        :return: setpoint
        """
        self.Des = setpoint
        return self.Des

    def MaxInput(self, maxIn):
        """
        Sets the Maximum input power
        :param maxIn: in between 0 - 1
        :return: maximum input power
        """
        self.maxIn = maxIn

    def MaxOutput(self, maxOut):
        """
        Sets max. outPut power
        :param maxOut: ""
        :return: maximum output power
        """
        self.maxOut = maxOut

    def getError(self, inputVal):
        """
        Gets the error (goal value - current value)
        :param inputVal: some sensor value
        :return: returns error
        """
        self.Error = self.des - inputVal
        return self.Error

    def getp(self, inputVal):
        """
        'proportional', error * kp
        :param inputVal: some sensor value
        :return: returns proportional component of PID
        """
        self.p = self.getError(inputVal) * self.kp
        return self.p

    def geti(self, inputVal):
        """
        Calculates Integral in PID; (error + I) * kI
        :param inputVal: some sensor value
        :return: returns I component
        """
        if self.Error == 0:
            self.i = 0
        else:
            self.i = (self.Error + self.i) * self.ki
        return self.i

    def getd(self, inputVal):
        """
        gets
        :param inputval:
        :return:
        """
        self.d = (self.getError(inputVal) - self.pastErr) * self.kd
        return self.d

    def EstF(self):
        """
        measures possible disturbances and tries to prevent them from happening
        :return: F constant in PIDF (velocity control)
        """
        self.F = ((self.maxOut / self.maxIn) * self.Des) * self.kf
        return self.F

    def limitVal(self, limitVal):
        self.limit = limitVal

    def outVel(self, inputVal):
        """

        :param inputval:
        :return:
        """

        self.outputvel = self.getp(inputVal) + self.geti(inputVal) + self.getd(inputVal)
        if self.outputvel > self.limit:
            self.outputvel = self.limit

        elif self.outputvel < 0:
            self.outputvel = 0

        self.pastErr = self.getError(inputVal)

        return self.EstF() + self.outputvel

    def outVal(self, inputval):
        """

        :param inputval:
        :return:
        """
        self.output = self.getp(inputval) + self.geti(inputval) + self.getd(inputval)

        if self.output > self.limit:
            self.output = self.limit
        elif self.output < -self.limit:
            self.output = -self.limit
        return self.output

    def UpdateCon(self, kP, kI, kD):
        """

        :param kP:
        :param kI:
        :param kD:
        :return:
        """
        self.kp = kP
        self.ki = kI
        self.kd = kD

        return self.kp, self.ki, self.kd
