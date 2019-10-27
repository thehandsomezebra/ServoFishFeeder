import schedule
import time
import RPi.GPIO as GPIO
import time

#warnings are sometimes irritating
GPIO.setwarnings(False)
############################## SETUP #########################################
###### CHANGE THIS IF YOU ARE GOING TO USE A DIFFERENT PIN SLOT ##############
servoPIN = 17
##############################################################################
################### CHANGE THIS TO False IF YOU ARE READY ####################
#test = False
test = True
##############################################################################
################ SET THE TIME IN 24 HR FORMAT ################################
#whattime = "22:00" # 10pm
whattime = "09:00" # 9am
##############################################################################

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO for PWM with 50Hz
p.start(2)
p.ChangeDutyCycle(0)

def wedjob():
	print("Wednesday Position")
	p.ChangeDutyCycle(2)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	time.sleep(1)
	p.ChangeDutyCycle(4)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters

def thursjob():
	print("Thursday Position")
	p.ChangeDutyCycle(4)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	time.sleep(1)
	p.ChangeDutyCycle(6)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	
def frijob():
	print("Friday Position")
	p.ChangeDutyCycle(6)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	time.sleep(1)
	p.ChangeDutyCycle(8)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	
def satjob():
	print("Saturday Position")
	p.ChangeDutyCycle(8)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	time.sleep(1)
	p.ChangeDutyCycle(10)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	
def sunjob():
	print("Sunday Position")
	p.ChangeDutyCycle(10)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters
	time.sleep(1)
	p.ChangeDutyCycle(12)
	time.sleep(1)
	p.ChangeDutyCycle(0) #this stops the jitters

def reset():
	print("resetting")
	#We're slowly walking it back to day one
	p.ChangeDutyCycle(12)
	time.sleep(1)
	p.ChangeDutyCycle(11)
	time.sleep(1)
	p.ChangeDutyCycle(10)
	time.sleep(1)
	p.ChangeDutyCycle(9)
	time.sleep(1)
	p.ChangeDutyCycle(8)
	time.sleep(1)
	p.ChangeDutyCycle(7)
	time.sleep(1)
	p.ChangeDutyCycle(6)
	time.sleep(1)
	p.ChangeDutyCycle(5)
	time.sleep(1)
	p.ChangeDutyCycle(4)
	time.sleep(1)
	p.ChangeDutyCycle(3)
	time.sleep(1)
	p.ChangeDutyCycle(2)
	time.sleep(1)
	#then stopping any/all signal from being sent to the servo
	p.stop()
	#cleaning up the gpio before we exit out
	GPIO.cleanup()
	
##used to test...use to set to zero position##
def runtest():
	wedjob()
	time.sleep(1)
	thursjob()
	time.sleep(1)
	frijob()
	time.sleep(1)
	satjob()
	time.sleep(1)
	sunjob()
	time.sleep(1)
	reset()



schedule.every().wednesday.at(whattime).do(wedjob)
schedule.every().thursday.at(whattime).do(thursjob)
schedule.every().friday.at(whattime).do(frijob)
schedule.every().saturday.at(whattime).do(satjob)
schedule.every().sunday.at(whattime).do(sunjob)


try:
	if test == True:
		print "running test and setup"
	else:
		print "SCHEDULE RUNNING"
		print "press ctrl + c to end program"
		
	while True:
		if test == True:
			print "running test and setup"
			runtest()
			print "FEEDER READY TO BE FILLED"
			break
		else:
			schedule.run_pending()
			time.sleep(1)
		pass 
except KeyboardInterrupt:
	print "\nPROGRAM ENDED"
	p.stop()
	GPIO.cleanup()
	pass # do cleanup here
