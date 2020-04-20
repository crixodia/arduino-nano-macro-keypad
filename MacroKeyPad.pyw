#! python3
import pyautogui, sys, time, serial

port = 'COM6'   #Windows COMX | Linux /dev/ttyUSBX or /dev/ttyACMX
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
        pyautogui.hotkey('ctrl', 'alt', 'c')    #Chatting
    elif data == '2':
        pyautogui.hotkey('ctrl', 'alt', 'd')    #Gaming
    elif data == '3':
        pyautogui.hotkey('ctrl', 'alt', 'f')    #Waiting
    elif data == '*':
        pyautogui.hotkey('ctrl', 'alt','a')     #Start/Stop streaming OBS
    elif data == '0':
        pyautogui.hotkey('ctrl', 'alt','b')     #Start/Stop recording OBS
    elif data == '#':
        pyautogui.hotkey('ctrl', 'alt','e')     #Transition OBS
    elif data == 'A':
        pyautogui.hotkey('ctrl', 'alt','g')     #Mute/Unmute desktop
    elif data == 'B':
        pyautogui.hotkey('ctrl', 'alt', 'h')    #Mute/Unmute headset
    elif data == 'C':
        pyautogui.hotkey('ctrl', 'alt','i')     #Mute/Unmute mic
    elif data == 'D':
        pyautogui.hotkey('ctrl', 'alt','del')