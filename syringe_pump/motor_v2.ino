// Hardware pins
const int dirPin = 2;
const int stepPin = 3;

// Adjustable parameters
const float targetFlowRate_mL_hr = 0.01; 
const float syringeID_mm = 4.69; // Default for 1mL syringe
const float leadPitch_mm = 8.0; 
const float stepsPerRev = 3200.0; // 200 steps * 1/16 microstepping

// Timing variables
unsigned long stepIntervalMicros = 0;
unsigned long previousMicros = 0;
int stepState = LOW;

void setup() {
  Serial.begin(9600);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  
  // Set initial spin direction
  digitalWrite(dirPin, HIGH); 
  
  // Convert flow rate to mm^3 / sec
  float flowRate_mm3_sec = (targetFlowRate_mL_hr * 1000.0) / 3600.0;
  
  // Calc cross-sectional area
  float radius = syringeID_mm / 2.0;
  float area_mm2 = PI * sq(radius);
  
  // Calc required linear speed
  float linearSpeed_mm_sec = flowRate_mm3_sec / area_mm2;
  
  // Calc steps per second
  float mmPerStep = leadPitch_mm / stepsPerRev; 
  float stepsPerSec = linearSpeed_mm_sec / mmPerStep;
  
  // Calc toggle interval
  if (stepsPerSec > 0) {
    stepIntervalMicros = 1000000.0 / (stepsPerSec * 2.0); 
  }

  // Print diagnostics
  Serial.print("Target Flow Rate (mL/hr): "); 
  Serial.println(targetFlowRate_mL_hr, 4);
  Serial.print("Pulse Interval (us): "); 
  Serial.println(stepIntervalMicros);
}

void loop() {
  unsigned long currentMicros = micros();

  // Check if time to step
  if (currentMicros - previousMicros >= stepIntervalMicros) {
    previousMicros = currentMicros;
    
    // Toggle step pin
    stepState = !stepState;
    digitalWrite(stepPin, stepState);
  }
}
