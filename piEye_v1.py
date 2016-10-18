import RPi.GPIO as GPIO
import smtplib
import datetime

   
TO_EMAIL = "receiver email goes here"
FROM_EMAIL = "sender email goes here"
FROM_PASSWORD = "sender password goes here"
SUBJECT = "INTRUDER!!

# PIR GPIO set up
PIR_PIN = 7 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN,)    

# infinite loop -> always running
while True:
    time.sleep(0.1)
    previous_state = current_state
	current_state = GPIO.input(PIR_PIN)
	# check if current state has changed
	if current_state != previous_state:
	    if current_state:
			
			timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S") 
    
	        # set up gmail 
	        server = smtplib.SMTP(smtp.gmail.com, 587)         
	        server.starttls                                
	        server.login(FROM_EMAIL, FROM_PASSWORD)
			
			BODY = "\r\n".join([
            "TO: %s" % TO_EMAIL,
            "From: %s" % FROM_EMAIL,
            "Subject: %s" % SUBJECT,
            "",
            "Intruder has been spotted at %s" % timestamp
            ])
	
	        # send gmail message 
	        server.sendmail(FROM_EMAIL, TO_EMAIL, BODY)
		    server.quit
    	
