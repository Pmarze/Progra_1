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
int lose=0;                  //LOSE=0 SI SE PUEDE SEGUIR JUGANDO LOSE=1 SI YA PERDIO
boolean estado= true;        //VARIABLE BOOLEANA DE ESTADO DEL JUEGO TRUE=AÚN EN JUEGO FALSE=TERMINADO
int nivel=1;                 //VARIABLE PARA INDICAR EL NIVEL DE JUEGO
int lista[50];               //LISTA DE LONGITUD 50

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
  aleatorio();                //GENERAMOS UNA LISTA ALEATORIA INICIAL
  ganar();                    //SECUENCIA DE LEDS INICIAL
}

void loop(){
  
  secuencia();                //SE MUESTRA LA SECUENCIA HASTA EL NIVEL ACTUAL
  entrada();                  //FUNCIÓN PARA LEER LOS PUSH BOTTON
  
  if (lose==1){               //SI LA FUNCIÓN ENTRADA DEVUELVE LOSE=1 ES QUE HUBO UNA CONFUCIÓN
    nivel=1;                  //SI PERDIMOS VOLVEMOS AL NIVEL 1
    aleatorio();              //GENERAMOS UNA NUEVA LISTA DE NÚMEROS ALEATORIOS
    lose=0;                   //LOOSE=0 PARA VOLVER A EMPEZAR DE NUEVO
    }
  if (nivel==50){             //SI LLEGAMOS AL NIVEL 50 YA NO TENEMOS MAS ELEMENTOS Y ES CUANDO GANAMOS
    ganar();                  //SECUENCIA INDICANDO QUE GANAMOS
    nivel=1;                  //VOLVEMOS AL NIVEL UNO
    aleatorio();              //GENERAMOS UNA NUEVA LISTA DE NÚMEROS ALEATORIOS              
    }
  estado=true;                //CUANDO TERMINA entrada() TIENE COMO SALIDA estado=false, CAMBIAMOS EL ESTADO PARA QUE VUELVA A FUNCIONAR
  delay(500);                                  
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
  lista[i]=random(1,5);      //GENERA NÚMEROS ENTRE 1 Y 4
  }   
  }
void secuencia(){           //FUNCIÓN PARA MOSTRAR LA SECUENCIA DESDE 1 HASTA EL NIVEL ACTUAL
  for (int i=0;i< nivel;i++){ //AL TENER VALORES ENTRE 0 Y 4 SOLO TENEMOS 4 POSIBLES CASOS
    if (lista[i]==1){       //SI EL ELEMENTO i DE LA LISTA ES UN 1, SE ENCIENDE EL LED AMARILLO
      amarillo();
      }
    if (lista[i]==2){       //SI EL ELEMENTO i DE LA LISTA ES UN 2, SE ENCIENDE EL LED AZUL
      azul();
      }
    if (lista[i]==3){       //SI EL ELEMENTO i DE LA LISTA ES UN 3, SE ENCIENDE EL LED VERDE
      verde();
      }  
    if (lista[i]==4){       //SI EL ELEMENTO i DE LA LISTA ES UN 4, SE ENCIENDE EL LED ROJO
      rojo();
      } 
  }
  }
void entrada(){             //FUNCIÓN PARA LEER LOS PUSH BOTTON
  e=0;                      //e=0 PARA EMPEZAR LA CUENTA DESDE 0
  while (estado==true){     
    while (e<=nivel){       //SI e<=nivel NOS MANTENEMOS CONTANDO AVANZANDO EN LA LISTA 
    a=digitalRead(PAM);        //LEER EL ESTADO DE PAM
    b=digitalRead(PAZ);        //LEER EL ESTADO DE PAZ
    c=digitalRead(PVE);        //LEER EL ESTADO DE PVE
    d=digitalRead(PRO);        //LEER EL ESTADO DE PRO
      if (e==nivel){           //SI e=nivel YA LLEGAMOS AL ULTIMO ELEMENTO DE LA LISTA
        estado=false;          //CAMBIAMOS A ESTADO FALSE
        break;                 //SALIMOS DEL CICLO
        }
      if (a==LOW){             // SI PRESIONAMOS PAM TENEMOS DOS CASOS, SI COINCIDE CON LA MUESTRA O NOS EQUIVOCAMOS
        if (lista[e]==1){      //SI EL BOTÓN PRESIONADO COINCIDE CON LA MUESTRA
          amarillo();          //SE MUESTRA NUESTRA SELECCIÓN DE LED
          e+=1;                //POR ACERTAR AHORA ANALIZAMOS EL SIGUIENTE CASO
          }
        else{                  //CUALQUIER OTRO VALOR DE LA LISTA QUE NO COINCIDA
          estado=false;        //CAMBIA EL ESTADO
          perder();            //MUESTRA LA SECUENCIA MOSTRANDO QUE PERDIMOS
          lose=1;              //REGRESA EL VALOR lose=q PARA REINICIAR EL JUEGO EN VOID LOOP
          break;               //SALIMOS DEL CICLO
          }
        }  
      if (b==LOW){             //IDEM CON LED AZUL
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
      if (c==LOW){             //IDEM CON LED VERDE
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
      if (d==LOW){              //IDEM CON LED ROJO
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
  nivel+=1;                     //AL TERMINAR EL CICLO AVANZAMOS AL SIGUIENTE NIVEL, SI HEMOS PERDIDO NO IMPORTA, ESTA CORRECIÓN SUCEDE EN VOID LOOP
} 
void ganar(){                   //SECUENCIA DE LEDS SI GANAMOS
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
void perder(){                  //SECUENCIA DE LEDS SI HEMOS PERDIDO
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
