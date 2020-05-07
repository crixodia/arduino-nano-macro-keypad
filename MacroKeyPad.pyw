#! python3
import pyautogui, sys, time, serial

port = 'COM4'   #Windows COMX | Linux /dev/ttyUSBX or /dev/ttyACMX
baud = 9600

NanoSerial = serial.Serial(port, baud)
time.sleep(1)

print("MacroKeyPad:", port, baud)

while 1:
    data = str(NanoSerial.readline())[2]
    if data == '7':
        pyautogui.press('prevtrack')    #Previous track
    elif data == '8':
        pyautogui.press('playpause')    #Play/Pause
    elif data == '9':
        pyautogui.press('nexttrack')    #Next track
    elif data == '4':
        pyautogui.press('volumedown')   #Turn volume down
    elif data == '5':
        pyautogui.press('volumemute')   #Turn volume on/off
    elif data == '6':
        pyautogui.press('volumeup')     #Turn volume up
    elif data == '1':
        pyautogui.hotkey('ctrl', 'b', '"')
    elif data == '2':
        pyautogui.hotkey('ctrl', 'b', '%')
    elif data == '3':
        pyautogui.hotkey('ctrl', 'b', 'c')
    elif data == '*':
        pyautogui.hotkey('ctrl', 'b', 'p')
    elif data == '0':
        pyautogui.hotkey('ctrl', 'b', 'n')
    elif data == '#':
        pyautogui.hotkey('ctrl', 'b', 'x')
    elif data == 'A':
        pyautogui.hotkey('ctrl', 'alt','g')
    elif data == 'B':
        pyautogui.hotkey('ctrl', 'alt', 'h')
    elif data == 'C':
        pyautogui.hotkey('ctrl', 'alt','i')
    elif data == 'D':
        pyautogui.hotkey('ctrl', 'alt','del')
