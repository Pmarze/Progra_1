#define t 125
#define PAM 2
#define PAZ 3
#define PVE 4
#define PRO 5
#define AM 6
#define AZ 7
#define VE 8
#define RO 9
#define BUZZ 10
int a=0;
int b=0;
int c=0;
int d=0;
void setup(){
  pinMode(PAM,INPUT);
  pinMode(PAZ,INPUT);
  pinMode(PVE,INPUT);
  pinMode(PRO,INPUT);

  pinMode(AM,OUTPUT);
  pinMode(RO,OUTPUT);
  pinMode(VE,OUTPUT);
  pinMode(AZ,OUTPUT);
  pinMode(BUZZ,OUTPUT);
}

void loop(){
 a=digitalRead(PAM);
 b=digitalRead(PAZ);
 c=digitalRead(PVE);
 d=digitalRead(PRO);
}

void amarillo(){
  digitalWrite(AM,HIGH);
  tone(BUZZ, 250);
  delay(t);
  noTone(BUZZ);
  digitalWrite(AM,LOW);
  delay(t);
}
void azul(){
  digitalWrite(AZ,HIGH);
  tone(BUZZ, 500);
  delay(t);
  noTone(BUZZ);
  digitalWrite(AZ,LOW);
  delay(t);
}
void verde(){
  digitalWrite(VE,HIGH);
  tone(BUZZ, 750);
  delay(t);
  noTone(BUZZ);
  digitalWrite(VE,LOW);
  delay(t);
}
void rojo(){
  digitalWrite(RO,HIGH);
  tone(BUZZ, 1000);
  delay(t);
  noTone(BUZZ);
  digitalWrite(RO,LOW);
  delay(t);
}
