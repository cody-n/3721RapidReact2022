class OI:
    def __init__(self, robot):
        super().__init__()

        self.robot = robot

        mainCon = {}
        sideCon = {}

        for name in self.robot.botMap.ControlMap.Controller:
            if self.robot.botMap.ControlMap.Controller[name]['jobType'] == 'main':
                mainCon[name] = self.robot.Creator.createControllers(self.robot.botMap.ControlMap.Controller[name])
            if self.robot.botMap.ControlMap.Controller[name]['jobType'] == 'side':
                sideCon[name] = self.robot.Creator.createControllers(self.robot.botMap.ControlMap.Controller[name])

            self.mainController = mainCon
            self.sideController = sideCon

    def getMainController(self):
        return self.mainController['xbox']

    def getSideController(self):
        return self.sideController['board']

