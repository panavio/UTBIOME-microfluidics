// Arduino Digital Pins
const int dirPin = 2;
const int stepPin = 3;

// Change flowrate
// this delay is in ms 
// Lower number = faster motor = higher flow rate.
// Higher number = slower motor = lower flow rate.

int speedDelay = 1000; 

/* Some Math
Nema 17 takes 200 steps to complete one full revolution (1.8 degrees per step).
We have an 8mm lead, one full revolution of the motor moves the nut exactly 8.0 mm forward.
So, Linear Resolution: 8.0 mm / 200 steps = 0.04 mm per step.
=> Every single time the stepMotor() function runs one loop, the syringe plunger is pushed exactly 0.04 mm.
*/

void setup() {
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
}

// Function to handle the stepping math
void stepMotor(int numSteps, int pulseDelay) {
  for(int x = 0; x < numSteps; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(pulseDelay); // wait
    digitalWrite(stepPin, LOW);
    delayMicroseconds(pulseDelay); // wait
  }
}

void loop() {
  // set direction
  digitalWrite(dirPin, HIGH);
  
  // test speed
  // Moves 800 steps at the speed defined by speedDelay
  stepMotor(800, speedDelay); 
  
  delay(1000); // wait 1 s

  // reverse spin direction
  digitalWrite(dirPin, LOW);
  stepMotor(800, speedDelay); 
  
  delay(2000); // wait before repeating
}
