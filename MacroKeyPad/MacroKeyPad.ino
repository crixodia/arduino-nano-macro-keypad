#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;

//Your Keypad distribution
const char hexaKeys[ROWS][COLS] = {
  {'D', '*', '0', '#'},
  {'C', '3', '2', '1'},
  {'B', '6', '5', '4'},
  {'A', '9', '8', '7'}
};

//Digital pins for Rows and Cols
byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2};

//Creates keypad object
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char customKey = customKeypad.getKey();
  if (customKey) {
    //Print de key char from hexaKeys matrix
    Serial.println(customKey);
  }
}
