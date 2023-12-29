#Este codigo busca controlar los Motores DC con el driver L298N
import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()
#Declara diversas variables
Forward=26
Backward=20
sleeptime=1
# Establecer el modo de numeración GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
    GPIO.output(Forward, GPIO.HIGH) # los motores avanzaran por un segundo y luego van a parar
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH) # los motores retrocederan por un segundo y luego van a parar
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

while (1):
    forward(5)
    reverse(5)

GPIO.cleanup()