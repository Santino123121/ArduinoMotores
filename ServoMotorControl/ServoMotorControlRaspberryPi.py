
# este programa trata de controlar la velocidad de un ServoMotor
import RPi.GPIO as GPIO
import time

# Establecer el modo de numeración GPIO
GPIO.setmode(GPIO.BOARD)

# Configura el pin 11 como salida y configura servo1 como pin 11 como PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) #11 es el pin y 50 = pulso de 50 Hz

# Define la variable duty y Fin 
duty = 2 # el 2 equivale a 0 grados
Fin = 12 # el 12 equivale a 180 grados
# Los ciclos de trabajo estan en un bucle de 2 a 12 (0 a 180 grados)
while duty <= Fin:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1) #cambiando el tiempo y la variable 0.5 se lograra ir ajustando la velocidad
    duty = duty + 0.5

#Limpiar las cosas al final.
servo1.stop()
GPIO.cleanup()
print ("Goodbye")
