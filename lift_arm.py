import time
import stretch_body.robot
import serial
ser = serial.Serial("/dev/ttyUSB3", 9600)


if __name__ == '__main__':

    robot = stretch_body.robot.Robot()
    robot.startup()
    robot.stow() #blocking
    robot.base.set_velocity(0.05, 0.1)
    robot.base.push_command()
    robot.lift.set_soft_motion_limit_min(0.2,limit_type='user')
    robot.lift.set_soft_motion_limit_max(0.98,limit_type='user') 

    if not robot.base.startup():
  	  exit() # failed to start base!

    robot.base.translate_by(x_m=0.03) 
    robot.push_command()
    print("init successful")

    time.sleep(1)
    while True:

        cc=str(ser.readline())


        if '1' in cc:
            print("f")
            robot.lift.move_by(x_m=-0.05) 
            robot.push_command()


        if '2' in cc:
            print("b")
            robot.lift.move_by(x_m=0.05) 
            robot.push_command()

        if '3' in cc:
            print("l")
	    robot.arm.move_by(-0.05)
            robot.push_command()

        if '4' in cc:
            print("r")
 	    robot.arm.move_by(0.05)
            robot.push_command()

        if '5' in cc:
            print("s")	
