void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  Serial.begin(9600);


  
  Serial1.begin(9600);
  Serial1.setTX(1);
  Serial1.setRX(0);
  

}

void loop() {
  // put your main code here, to run repeatedly:


  
  Serial.println(Serial1.read());
  digitalWrite(13,HIGH);
  delay(500);
  

}
