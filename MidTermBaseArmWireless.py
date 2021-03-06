import time
import stretch_body.robot
import serial
import os
from stretch_body.hello_utils import *
ser = serial.Serial("/dev/ttyUSB3", 9600)


if __name__ == '__main__':

    robot = stretch_body.robot.Robot()
    robot.startup()
    robot.stow() #blocking
    robot.base.set_velocity(0.05, 0.1)
    robot.base.push_command()
    robot.lift.set_soft_motion_limit_min(0.2,limit_type='user')
    robot.lift.set_soft_motion_limit_max(0.98,limit_type='user')
    v_des=stretch_body.wrist_yaw.WristYaw().params['motion']['default']['vel']
    a_des=stretch_body.wrist_yaw.WristYaw().params['motion']['default']['accel']
    setflagArm = setflagWrist = setflagBase = setflagGripper = True

    if not robot.base.startup():
  	  exit() # failed to start base!

    robot.base.translate_by(x_m=0.03) 
    robot.push_command()
    print("init successful")

	

    x =  robot.end_of_arm.status['wrist_yaw']['pos']
    robot.end_of_arm.move_to('wrist_yaw', float((x-deg_to_rad(5))),v_des, a_des)
    robot.end_of_arm.move_by('stretch_gripper', 100)
    robot.push_command()
    time.sleep(2)
    mode = ' '
    os.system('paplay --device=alsa_output.pci-0000_00_1f.3.analog-stereo /home/hello-robot/ready.ogg')
    while True:

        cc=str(ser.readline())
        print(cc)

        if '1' in cc:
            #print("1/f")

            if mode == 'arm':
                robot.lift.move_by(x_m=-0.05) 
                robot.push_command()

            if mode == 'base':
                robot.base.set_velocity(0.05, 0.1)
                robot.base.push_command()
                robot.base.translate_by(x_m=0.02) 
                robot.push_command()

            if mode == 'wrist':
		x =  robot.end_of_arm.status['wrist_pitch']['pos']
        	robot.end_of_arm.move_to('wrist_pitch', float((x-deg_to_rad(2))),v_des, a_des)
        	robot.push_command()


            if mode == 'gripper':

		#robot.end_of_arm.move_by('stretch_gripper',0)
        	#robot.push_command()
		pass

#############################################

        if '2' in cc:
            #print("2/b")

            if mode == 'arm':
                robot.lift.move_by(x_m=0.05) 
                robot.push_command()

            if mode == 'base':
                robot.base.set_velocity(0.05, 0.1)
                robot.base.push_command()
                robot.base.translate_by(x_m=-0.02) 
                robot.push_command()

            if mode == 'wrist':
		x =  robot.end_of_arm.status['wrist_pitch']['pos']
        	robot.end_of_arm.move_to('wrist_pitch', float((x+deg_to_rad(2))),v_des, a_des)
                robot.push_command()


            if mode == 'gripper':

		#robot.end_of_arm.move_by('stretch_gripper',-100)
        	#robot.push_command()
		pass
	

#############################################

        if '3' in cc:
            #print("3/l")

            if mode == 'arm':
                robot.arm.move_by(-0.05)
                robot.push_command()

            if mode == 'base':
                robot.base.set_velocity(0.05, 0.1)
                robot.base.push_command()
                robot.base.rotate_by(0.05)
                robot.push_command()

            if mode == 'wrist':
		x =  robot.end_of_arm.status['wrist_yaw']['pos']
        	robot.end_of_arm.move_to('wrist_yaw', float((x+deg_to_rad(2))),v_des, a_des)
        	robot.push_command()

            if mode == 'gripper':

 		robot.end_of_arm.move_by('stretch_gripper', 100)
	        robot.push_command()
	

#############################
        if '4' in cc:
            #print("4/r")

            if mode == 'arm':
                robot.arm.move_by(0.05)
                robot.push_command()

            if mode == 'base':
                robot.base.set_velocity(0.05, 0.1)
                robot.base.push_command()
                robot.base.rotate_by(-0.05)
                robot.push_command()

            if mode == 'wrist':
		x =  robot.end_of_arm.status['wrist_yaw']['pos']
        	robot.end_of_arm.move_to('wrist_yaw', float((x-deg_to_rad(2))),v_des, a_des)
        	robot.push_command()


            if mode == 'gripper':
 		robot.end_of_arm.move_by('stretch_gripper', -5)
	        robot.push_command()
	

#################################

        if '5' in cc:
            #print("5/s")

            if mode == 'base':
                robot.base.set_velocity(0, 0)
                robot.base.push_command()

##################################

        if '6' in cc and setflagBase is True:
            mode = 'base'
	    os.system('paplay --device=alsa_output.pci-0000_00_1f.3.analog-stereo /home/hello-robot/base.ogg')
	    cc = '0'
	    setflagBase = False
	    setflagArm = setflagWrist = setflagGripper = True

####################################

        if '7' in cc and setflagArm is True:
            mode = 'arm'
	    os.system('paplay --device=alsa_output.pci-0000_00_1f.3.analog-stereo /home/hello-robot/arm.ogg')
	    cc = '0'
	    setflagArm = False
	    setflagBase = setflagWrist = setflagGripper = True

###################################

	if '8' in cc and setflagWrist is True:
	    mode = 'wrist'
	    os.system('paplay --device=alsa_output.pci-0000_00_1f.3.analog-stereo /home/hello-robot/wrist.ogg')
	    cc = '0'
	    setflagWrist = False
	    setflagArm = setflagBase = setflagGripper = True

##################################

	if '9' in cc and setflagGripper is True:
	    mode = 'gripper'
	    os.system('paplay --device=alsa_output.pci-0000_00_1f.3.analog-stereo /home/hello-robot/gripper.ogg')
	    cc = '0'
	    setflagGripper = False
	    setflagArm = setflagWrist = setflagBase = True
