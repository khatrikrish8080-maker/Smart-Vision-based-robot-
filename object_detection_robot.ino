

#define IN1 3
#define IN2 4
#define IN3 5
#define IN4 6
#define ENA 10
#define ENB 9


unsigned long last=0;
void setup() {
  Serial.begin(9600);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  digitalWrite(ENA,HIGH);
  digitalWrite(ENB,HIGH);

  

  stopMotors();
}

void loop() {
  if(millis()-last>10000){
    stopMotors();
  }
  if (Serial.available()>0) {
    char command = Serial.read();
    last=millis();

    if (command == 'F') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
    }

    else if (command == 'L') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
    }

    else if (command == 'R') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
    }
    else  {
      stopMotors();
    }
  }
}
void stopMotors(){
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
      
      
}