import time #IMPORTS TIME FUNCTION NECESSARY FOR TIME.SLEEP
import RPi.GPIO as GPIO #SETS UP PINS ON THE BOARD AS GPIO.
time.sleep(1) #USED AS A PAUSE WHEN CODE BOOTS ON START UP
GPIO.setmode(GPIO.BOARD)#LABELS PINS ON BOARD AS 1-40
GPIO.setup(7,GPIO.OUT) #PIN 7 OUTPUT TO CONTROL PWM1 ON CONTROLLER
GPIO.setup(11,GPIO.OUT) #PIN 11 OUTPUT TO CONTROL DIR1 ON CONTROLLER
GPIO.setup(35,GPIO.OUT) #PIN 35 OUTPUT TO CONTROL DIR2 ON CONTROLLER
GPIO.setup(37,GPIO.OUT) #PIN 37 OUTPUT TO CONTROL PWM2 ON CONTROLLER
GPIO.setup(38,GPIO.OUT) #OUTPUT FEEDS INTO PUSH BUTTON
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Gas in
GPIO.output(38,1) #OUTPUTS TRUE INTOPUSH BUTTON
GPIO.output(11,True) #Direction start forward (True) #SETS DIR1 TO TRUE
GPIO.output(35,True) #Direction start forward (True) #SETS DIR2 TO TRUE

m = GPIO.PWM(7,1000) # SETS PIN 7 AS A PWM OUTPUT @1000 Hz
n = GPIO.PWM(37,1000) # SETS PIN 37 AS A PWM OUTPUT @1000 Hz

d = 0     #SETS PWM AT 0, MOTOR SPEED 0

m.start(d)   #STARTS PWM1
n.start(d)   #STARTS PWM2
# Molly setup looks fine but I also don't really know much about GPIO. 

try:  # Why is this in a try statement? What do you want done if it throws an error? 
    while True: # LOOP FOREVER
        if (GPIO.input(40) == 1):           #IF BUTTON IS PUSHED, INCREMENT          SPEED POSITIVE
            if d < 96:
                d += 5
                print(d)
                m.ChangeDutyCycle(d)
                n.ChangeDutyCycle(d)
                time.sleep(.075)
        elif (GPIO.input(40) == 0) :   #IF BUTTON IS NOT PUSHED,           INCREMENT SPEED NEGATIVE
            if d > 4:
                d -= 5
                print(d)
                m.ChangeDutyCycle(d)
                n.ChangeDutyCycle(d)
                time.sleep(.075)

# How is this finally getting reached? Seems like you have two scenarios accounted for and it will never get here
finally: #FINAL CLEAN-UP  
  GPIO.cleanup(); m.stop(); n.stop()

 
# Ok so most of this looks ok. Do you want to have some sort of safeguard for the value of d? what happens if d is equal to -99999999999999999999? 
# Also what do you want to happen if d is greater than 96? So if the button is pushed and d is 105 what do you expect to happen? it will never enter your elif statement as long as they keep the button pushed? Maybe you want to reset it if d is greater than 96?
# Lastly wanted to remphasize why you have a try/finally I don't see any way this finally statement could get hit.
