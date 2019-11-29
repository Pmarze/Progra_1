#define t 250                //TIEMPO DEL DELAY
#define PAM 2                //PUSH BOTTON AMARILLO
#define PAZ 3                //PUSH BOTTON AZUL
#define PVE 4                //PUSH BOTTON VERDE
#define PRO 5                //PUSH BOTTON ROJO
#define AM 6                 //LED AMARILLO
#define AZ 7                 //LED AZUL
#define VE 8                 //LED VERDE
#define RO 9                 //LED ROJO
#define BUZZ 10              //BUZZER
int a=0;                     //VARIABLE PARA LEER PAM
int b=0;                     //VARIABLE PARA LEER PAZ
int c=0;                     //VARIABLE PARA LEER PVE
int d=0;                     //VARIABLE PARA LEER PRO
int e=0;                     //VARIABLE PARA ENTRADA
int lose=0;
boolean estado= true;        //VARIABLE BOOLEANA DE ESTADO DEL JUEGO TRUE=AÚN EN JUEGO FALSE=TERMINADO
int nivel=1;
int lista[50];

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
  aleatorio();                //Generamos una lista aleatoria para el primer juego
  Serial.begin(9600);
}

void loop(){
  ganar();
  secuencia();
  entrada();  
  
  if (lose==1);
    nivel=1;
    aleatorio();
  estado=true; 
}

void amarillo(){             //FUNCIÓN DEL LED AMARILLO
  digitalWrite(AM,HIGH);
  tone(BUZZ, 4000);
  delay(t);
  noTone(BUZZ);
  digitalWrite(AM,LOW);
  delay(t);
  }
void azul(){                 //FUNCIÓN DEL LED AZUL
  digitalWrite(AZ,HIGH);
  tone(BUZZ, 5000);
  delay(t);
  noTone(BUZZ);
  digitalWrite(AZ,LOW);
  delay(t);
  }
void verde(){                //FUNCIÓN DEL LED VERDE
  digitalWrite(VE,HIGH);
  tone(BUZZ, 6000);
  delay(t);
  noTone(BUZZ);
  digitalWrite(VE,LOW);
  delay(t);
  }
void rojo(){                 //FUNCIÓN DEL LED ROJO
  digitalWrite(RO,HIGH);
  tone(BUZZ, 6750);
  delay(t);
  noTone(BUZZ);
  digitalWrite(RO,LOW);
  delay(t);
  }
void aleatorio(){            //GENERA UNA LISTA DE 50 ELEMENTOS ALEATORIOS
  randomSeed(analogRead(A0));
  for (int i=0;i<50;i++){
  lista[i]=random(1,5);  
  }
  }
void secuencia(){           //FUNCIÓN PARA MOSTRAR LA SECUENCIA DESDE 1 HASTA EL NIVEL ACTUAL
  for (int i=0;i< nivel;i++){ //AL TENER VALORES ENTRE 0 Y 4 SOLO TENEMOS 4 POSIBLES CASOS
    if (lista[i]==1){       //SI EL ELEMENTO i DE LA LISTA ES UN 1, SE ENCIENDE EL LED AMARILLO
      amarillo();
      }
    if (lista[i]==2){
      azul();
      }
    if (lista[i]==3){
      verde();
      }  
    if (lista[i]==4){
      rojo();
      } 
  }
  }
void entrada(){
  e=0;
  while (estado==true){
    while (e<=nivel){
    a=digitalRead(PAM);        //LEER EL ESTADO DE PAM
    b=digitalRead(PAZ);        //LEER EL ESTADO DE PAZ
    c=digitalRead(PVE);        //LEER EL ESTADO DE PVE
    d=digitalRead(PRO);        //LEER EL ESTADO DE PRO
      Serial.println(e);
      if (e==nivel+1){
        estado=false;
        
        break;
        }
      if (a==LOW){
        if (lista[e]==1){
          amarillo();
          e+=1;
          }
        else{
          estado=false;
          perder();
          lose=1;
          break;
          }
        }  
      if (b==LOW){
        if (lista[e]==2){
          azul();
          e+=1;
          }
        else{
          estado=false;
          perder();
          lose=1;
          break;
          }
        }  
      if (c==LOW){
        if (lista[e]==3){
          verde();
          e+=1;
          }
        else{
          estado=false;
          perder();
          lose=1;
          break;
          }
        }  
      if (d==LOW){
        if (lista[e]==4){
          rojo();
          e+=1;
          }
        else{
          estado=false;
          perder();
          lose=1;
          break;
          }
        }  
    }
  }
  nivel+=1;
}
  
void ganar(){
  for (int a=0;a<5;a++){
  digitalWrite(AM,HIGH);
  digitalWrite(AZ,HIGH);
  digitalWrite(VE,HIGH);
  digitalWrite(RO,HIGH);
  delay(75);
  digitalWrite(AM,LOW);
  digitalWrite(AZ,LOW);
  digitalWrite(VE,LOW);
  digitalWrite(RO,LOW);
  delay(75);
}}
void perder(){
  for (int b=0;b<5;b++){
  digitalWrite(AM,HIGH);
  digitalWrite(AZ,LOW);
  digitalWrite(VE,LOW);
  digitalWrite(RO,HIGH);
  delay(75);
  digitalWrite(AM,LOW);
  digitalWrite(AZ,HIGH);
  digitalWrite(VE,HIGH);
  digitalWrite(RO,LOW);
  delay(75);
  digitalWrite(AZ,LOW);
  digitalWrite(VE,LOW);
  }}
