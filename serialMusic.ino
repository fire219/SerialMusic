/* Arduino SerialMusic Synthesizer Sketch
 *  Created by Matthew Petry (fire219/fireTwoOneNine), June 2018
 *  Licensed under the GPLv3 license -- see LICENSE file
 */
 
byte inNote1;
byte inNote2;
int freq;
int volume;
String note;
int timeout;

#include "Volume3.h" 

int MultiplicationCombine(unsigned int x_high, unsigned int x_low)
{
  int combined;
  combined = x_high;
  combined = combined*256; 
  combined |= x_low;
  return combined;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() == 2) {
    inNote1 = Serial.read();
    inNote2 = Serial.read();
    freq = MultiplicationCombine(inNote1, inNote2);
    if (freq == 0) {
      vol.noTone();   
    }
    volume = 1023;
    timeout = 3000;
    vol.tone(9, freq,volume);
  }
  else {
    if (freq != 0) {
      vol.tone(9, freq,volume);
      volume = volume * 0.99 + 2;
      timeout--;
    }
    if (timeout <= 0) {
      vol.noTone();
      timeout = 0;
    }
  }
  delay(1);

}
