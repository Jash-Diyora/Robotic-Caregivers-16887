#robocare
import time
import stretch_body.robot

import serial
ser = serial.Serial("/dev/ttyUSB3", 115600)

# First port to left is usb3 or use lsusb
if __name__ == '__main__':

    robot = stretch_body.robot.Robot()
    robot.startup()
    robot.stow() #blocking

    while True:

        cc=str(ser.readline())
        ccdata=(cc[:4][:])
        xx = float(ccdata)
        print(xx)

        if 8 < xx < 10:
            print("here")
            robot.base.translate_by(x_m=0.1) 
            robot.push_command()
            #robot.arm.move_to(0.2)
            #robot.push_command()


        if -8 > xx > -10:
            print("there")
            robot.base.translate_by(x_m=-0.1) 
            robot.push_command()
            #robot.arm.move_to(0.0)
            #robot.push_command()


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
