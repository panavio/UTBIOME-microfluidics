const byte step_pin = 3; 
const byte dir_pin = 2; 
 
void setup() {

    pinMode(step_pin,OUTPUT); 
    pinMode(dir_pin,OUTPUT);
    
}

void loop() {

	//Set direction to clockwise.
    digitalWrite(dir_pin,HIGH);

    for(byte i=0;i<200;i++) {
    
        digitalWrite(step_pin,HIGH); 
        delayMicroseconds(500); 
        digitalWrite(step_pin,LOW); 
        delayMicroseconds(500); 
        
    }

}