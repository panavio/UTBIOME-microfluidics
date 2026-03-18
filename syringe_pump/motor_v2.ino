// Arduino Digital Pins
const int dirPin = 2;
const int stepPin = 3;

// Change flowrate
// this delay is in microseconds (us) 
// Lower number = faster motor = higher flow rate.
// Higher number = slower motor = lower flow rate.

int speedDelay = 200; 

/* Some Math (Updated for 1/16 Microstepping)
Nema 17 takes 3200 steps to complete one full revolution (1/16 microsteps).
We have an 8mm lead, one full revolution of the motor moves the nut exactly 8.0 mm forward.
So, Linear Resolution: 8.0 mm / 3200 steps = 0.0025 mm per step.
=> Every single time the stepMotor() function runs one loop, the syringe plunger is pushed exactly 0.0025 mm.
*/

void setup() {
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  
  // set direction once so it spins continuously in one direction
  digitalWrite(dirPin, HIGH);
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
  // test speed smoothly and continuously
  // Moves 3200 steps (1 full revolution) at the speed defined by speedDelay
  stepMotor(3200, speedDelay); 
}
