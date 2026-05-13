#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  Serial.begin(9600); // Python sobat bolnyasathi port suru kara
  lcd.begin(16, 2);
  lcd.print("System Online");
  delay(1000);
  lcd.clear();
  lcd.print("Waiting for Data");
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read(); // Python kadhun alela character vacha
    lcd.clear();

    if (data == 'V') { // V = Verified
      lcd.print("Voter Verified");
      lcd.setCursor(0, 1);
      lcd.print("Access Granted");
    } 
    else if (data == 'F') { // F = Fraud
      lcd.print("FRAUD ATTEMPT!");
      lcd.setCursor(0, 1);
      lcd.print("Buzzer Active");
    }
  }
}