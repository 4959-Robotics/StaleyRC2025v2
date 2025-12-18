from commands2 import Subsystem
from wpilib import RobotState
from ntcore import NetworkTable, NetworkTableInstance
from rev import SparkMax, SparkMaxConfig

class CoralManipulator(Subsystem):
    # Variable Type Declaration
    logging:NetworkTable = None

    def __init__(self, pivotMotorID:int, coralIOMotorID:int) -> None:
        ## Logging inits
        self.logging = NetworkTableInstance.getDefault().getTable("/Logging/CoralManipulator")

        ## Motor Inits
        # Pivot Motor
        self.pivotMotor = SparkMax(pivotMotorID, SparkMax.MotorType.kBrushless)

        pivMotorConfig = SparkMaxConfig()
        pivEncoderConfig = pivMotorConfig.absoluteEncoder.inverted(False)
        pivEncoderConfig = pivEncoderConfig.zeroOffset(0.0)

        self.coralIOMotor = SparkMax(coralIOMotorID, SparkMax.MotorType.kBrushless)

    def periodic(self) -> None:
        # Logging: Write Current Subsystem State
        self.logging.putNumber( "SubsystemData", 0.0 )

        # Run Subsystem: Set New State To Subsystem
        if RobotState.isDisabled():
            self.stop()
        else:
            self.run()
        
        # Logging: Write Post Operation Information
        self.logging.putNumber( "Setpoint", self.getSetpoint() )

    def run(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def setSetpoint(self, value:float) -> None:
        """
        Set Desired State value
        """
        self.value = value

    def getSetpoint(self) -> float:
        """
        Get Desired State value
        """
        return self.value
    
    def atSetpoint(self) -> bool:
        return False