import RPi.GPIO as GPIO
import gpiozero
import smtplib
import datetime
import dropbox

   
TO_EMAIL = "receiver email goes here"
FROM_EMAIL = "sender email goes here"
FROM_PASSWORD = "sender password goes here"
SUBJECT = "INTRUDER!!"
DROPBOX_TOKEN = "dropbox token goes here"

# PIR GPIO set up
PIR_PIN = 7 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)     

# infinite loop -> always running
while True:
    time.sleep(0.1)
    previous_state = current_state
	current_state = GPIO.input(PIR_PIN)
	# check if current state has changed
	if current_state != previous_state:
	    if current_state:
			
			# set up time and video file info
			timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
            videoname = timestamp + ".mp4"			
			filename = "/home/pi/" + videoname
			
			# take 10 second video
			camera.start_recording(filename)
			sleep(10)
			camera.stop_recording()
			
			# upload video to Dropbox
			vid = open(filename)
			dropB = dropbox.Dropbox(DROPBOX_TOKEN)
			dropB.files_upload(vid, videoname)
			vid.close()
    
	        # set up gmail 
	        server = smtplib.SMTP(FROM_EMAIL, 587)         
	        server.starttls                                
	        server.login(FROM_EMAIL, FROM_PASSWORD)
			
			BODY = "\r\n".join([
            "TO: %s" % TO_EMAIL,
            "From: %s" % FROM_EMAIL,
            "Subject: %s" % SUBJECT,
            "",
            "Intruder has been spotted at %s" % timestamp,
			"",
			"Please see Dropbox Account for video"
            ])
	
	        # send gmail message 
	        server.sendmail(FROM_EMAIL, TO_EMAIL, BODY)
		    server.quit
    	