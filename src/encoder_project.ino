int analogPin0 = A0; 
int analogPin1 = A1;
int analogPin2 = A2; 
int analogPin3 = A3; 
int analogPin4 = A4;
int analogPin5 = A5;   
int val0 = 0;
int val1 = 0;
int val2 = 0;
int val3 = 0;
int val4 = 0;
int val5 = 0;
float angles[6];

void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {
  val0 = analogRead(analogPin0);  // read the input pin
  val1 = analogRead(analogPin1);  // read the input pin
  val2 = analogRead(analogPin2);  // read the input pin
  val3 = analogRead(analogPin3);  // read the input pin
  val4 = analogRead(analogPin4);  // read the input pin
  val5 = analogRead(analogPin5);  // read the input pin
  angles[0] = 0.36*val0;
  angles[1] = 0.36*val1;
  angles[2] = 0.36*val2;
  angles[3] = 0.36*val3;
  angles[4] = 0.36*val4;
  angles[5] = 0.36*val5;
  // Send the angles array as a comma-separated string
  Serial.print(angles[0]);
  Serial.print(",");
  Serial.print(angles[1]);
  Serial.print(",");
  Serial.print(angles[2]);
  Serial.print(",");
  Serial.print(angles[3]);
  Serial.print(",");
  Serial.print(angles[4]);
  Serial.print(",");
  Serial.println(angles[5]);
}
