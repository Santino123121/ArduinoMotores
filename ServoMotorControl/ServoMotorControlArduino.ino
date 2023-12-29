#include <Servo.h>

// este programa trata de controlar la velocidad de un ServoMotor

Servo myServo;
void setup() {
  myServo.attach(9);
}

void loop() {
  giroizq(0, 90, 3);//se pone primero donde iniciara el Motor, donde terminara y la velocidad(recomiendo usar multiplos del numero en donde terminara el motor)
  delay(500);
  giroder(90, 0, 3);
  delay(500);
}
void giroizq(int inicio,int fin,int speedy){
  while(inicio<=fin){//se compara donde vaya a iniciar el ServoMotor y donde terminara
    myServo.write(inicio); //si el ServoMotor no llego al fin asignado ira hacia donde la variable inicio este
    delay(100);
    inicio = inicio + speedy;// se suma la variable speed hasta que inicio sea igual a la variable fin y su programa termine
    }
}
void giroder(int inicio,int fin,int speedy){
  while(inicio>=fin){//se compara donde vaya a iniciar el ServoMotor y donde terminara
    myServo.write(inicio); //si el ServoMotor no llego al fin asignado ira hacia donde la variable inicio este
    delay(100);
    inicio = inicio - speedy;// se resta la variable speed hasta que inicio sea igual a la variable fin y su programa termine
    }
}
