

void setup() {
  Serial.begin(9600); //Open serial connection
}

void loop() {
  
  int sensorVal = analogRead(A3); //Read value from analog ping A3
  float voltage = (sensorVal/1024.0) * 5.0; //Calculate voltage
  float temperature = (voltage - 0.5) * 100; //Calculate temperature
  Serial.println(temperature); // Write temperature to serial connection
  delay(100); // Wait for 100 ms
}
