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

    if not robot.base.startup():
  	  exit() # failed to start base!

    robot.base.translate_by(x_m=0.03) 
    robot.push_command()
    print("init successful")

    time.sleep(1)
    while True:

        cc=str(ser.readline())
        #ccdata=(cc[:4][:])
        #xx = float(ccdata)
	#cmd = float(cc
	#print(cc)

        if '1' in cc:
            print("f")
            robot.base.set_velocity(0.05, 0.1)
            robot.base.push_command()
            robot.base.translate_by(x_m=0.03) 
            robot.push_command()


        if '2' in cc:
            print("b")
            robot.base.set_velocity(0.05, 0.1)
            robot.base.push_command()
            robot.base.translate_by(x_m=-0.03) 
            robot.push_command()

        if '3' in cc:
            print("l")
 	    robot.base.set_velocity(0.05, 0.1)
            robot.base.push_command()
            robot.base.rotate_by(0.05)
            robot.push_command()

        if '4' in cc:
            print("r")
 	    robot.base.set_velocity(0.05, 0.1)
    	    robot.base.push_command()
            robot.base.rotate_by(-0.05)
            robot.push_command()

        if '5' in cc:
            print("s")	
    	    robot.base.set_velocity(0, 0)
	    robot.base.push_command()


         
    # robot.base.translate_by(x_m=1) 
    # robot.push_command()
    # time.sleep(4.0) #wait

    # robot.base.set_rotational_velocity(v_r=0.5) #switch to velocity controller
    # robot.push_command()
    # time.sleep(4.0) #wait

    # robot.base.set_rotational_velocity(v_r=0.0) #stop motion
    # robot.push_command()
    # time.sleep(2.0)
    # robot.stop()
