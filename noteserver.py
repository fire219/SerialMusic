# Arduino SerialMusic Note Server
# Created by Matthew Petry (fire219/fireTwoOneNine), June 2018
# Licensed under the GPLv3 license -- see LICENSE file


import serial
import time
import sys
import os

serialport = "COM6"

print("Arduino SerialMusic Note Server")
	
def sendIntByte(intval):
	print(intval)
	ser.write(intval.to_bytes(2, 'big'))

def sendIntByteSilent(intval):
	ser.write(intval.to_bytes(2, 'big'))

def stopNote():
	ser.write(b'\00\00')
	
def help():
	print("")
	print("Serial-driven square wave synth on Arduino boards")
	print("")
	print("Usage:")
	print("-------")
	print(sys.argv[0] + " <serial port> <command> [filename]")
	print("")
	print("demo        - Plays built in demo tune (Partial 'Your Reality' from Doki Doki Literature Club)")
	print("test        -  Test chosen serial port for connectivity")
	print("play <file> - Plays music file")
	sys.exit()

def connectSerial():
	print("Connecting to serial port: " + serialport)	
	try:	
		testserial = serial.Serial(
			port=serialport,\
			baudrate=38400,\
			parity=serial.PARITY_NONE,\
			stopbits=serial.STOPBITS_ONE,\
			bytesize=serial.EIGHTBITS,\
				timeout=0.1)
		return testserial		
	except serial.serialutil.SerialException:
		print("Serial device on "+serialport+" was not found. Please confirm that Arduino is connected and port is correct.")
		sys.exit()

def readFile():
	if os.path.isfile(os.getcwd()+"/"+filename) == True:
		musicfile = open(os.getcwd()+"/"+filename, 'r')
		print("File opened!")
	else:
		print("Music file '"+filename+"' not found.")
		sys.exit()
	bpm = int(musicfile.readline())
	ticklength = 60 / bpm / 4
	sendIntByteSilent(1)
	time.sleep(0.5)
	while True:
		line = musicfile.readline()
		if not line: break
		linecomp = line.split()
		try:
			sendIntByte(globals()["NOTE_"+linecomp[0]])
		except IndexError:
			break
		time.sleep(ticklength * int(linecomp[1]))
		
	
def demoTune():
	stopNote()
	time.sleep(1.0)
	sendIntByte(NOTE_C4)
	time.sleep(0.75)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(1.0)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
	sendIntByte(NOTE_F4)
	time.sleep(0.125)
	sendIntByte(NOTE_E4)
	time.sleep(0.375)
	sendIntByte(NOTE_E4)
	time.sleep(0.25)
	sendIntByte(NOTE_F4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_E4)
	time.sleep(0.375)
	sendIntByte(NOTE_D4)
	time.sleep(0.75)
	sendIntByte(NOTE_C4)
	time.sleep(0.375)
	sendIntByte(NOTE_D4)
	time.sleep(0.375)
	sendIntByte(NOTE_E4)
	time.sleep(0.375)
	sendIntByte(NOTE_C4)
	time.sleep(0.375)
	sendIntByte(NOTE_G3)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
	sendIntByte(NOTE_A4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
	sendIntByte(NOTE_A4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_C5)
	time.sleep(1.125)
	sendIntByte(NOTE_C5)
	time.sleep(0.375)
	sendIntByte(NOTE_A4)
	time.sleep(0.25)
	sendIntByte(NOTE_B4)
	time.sleep(0.375)	
	sendIntByte(NOTE_A4)
	time.sleep(0.125)
	sendIntByte(NOTE_B4)
	time.sleep(0.375)	
	sendIntByte(NOTE_C5)
	time.sleep(0.375)	
	sendIntByte(NOTE_A4)
	time.sleep(0.375)
	sendIntByte(NOTE_C4)
	time.sleep(0.75)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_A4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(1.0)
	sendIntByte(NOTE_E4)
	time.sleep(0.25)
	sendIntByte(NOTE_F4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)	
	sendIntByte(NOTE_F4)
	time.sleep(0.25)
	sendIntByte(NOTE_E4)
	time.sleep(0.125)
	sendIntByte(NOTE_D4)
	time.sleep(0.375)
	sendIntByte(NOTE_A3)
	time.sleep(0.375)
	sendIntByte(NOTE_G3)
	time.sleep(0.75)
	sendIntByte(NOTE_F3)
	time.sleep(0.375)
	sendIntByte(NOTE_A3)
	time.sleep(0.375)
	sendIntByte(NOTE_G3)
	time.sleep(.375)
	sendIntByte(NOTE_E4)
	time.sleep(0.375)
	sendIntByte(NOTE_C4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
	sendIntByte(NOTE_A4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.375)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
	sendIntByte(NOTE_A4)
	time.sleep(0.125)
	sendIntByte(NOTE_G4)
	time.sleep(0.25)
		
NOTE_B0 = 31
NOTE_C1 = 33
NOTE_CS1 = 35
NOTE_D1 = 37
NOTE_DS1 = 39
NOTE_E1 = 41
NOTE_F1 = 44
NOTE_FS1 = 46
NOTE_G1 = 49
NOTE_GS1 = 52
NOTE_A1 = 55
NOTE_AS1 = 58
NOTE_B1 = 62
NOTE_C2 = 65
NOTE_CS2 = 69
NOTE_D2 = 73
NOTE_DS2 = 78
NOTE_E2 = 82
NOTE_F2 = 87
NOTE_FS2 = 93
NOTE_G2 = 98
NOTE_GS2 = 104
NOTE_A2 = 110
NOTE_AS2 = 117
NOTE_B2 = 123
NOTE_C3 = 131
NOTE_CS3 = 139
NOTE_D3 = 147
NOTE_DS3 = 156
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_FS3 = 185
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_FS4 = 370
NOTE_G4 = 392
NOTE_GS4 = 415
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_CS5 = 554
NOTE_D5 = 587
NOTE_DS5 = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_FS5 = 740
NOTE_G5 = 784
NOTE_GS5 = 831
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_CS6 = 1109
NOTE_D6 = 1175
NOTE_DS6 = 1245
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_FS6 = 1480
NOTE_G6 = 1568
NOTE_GS6 = 1661
NOTE_A6 = 1760
NOTE_AS6 = 1865
NOTE_B6 = 1976
NOTE_C7 = 2093
NOTE_CS7 = 2217
NOTE_D7 = 2349
NOTE_DS7 = 2489
NOTE_E7 = 2637
NOTE_F7 = 2794
NOTE_FS7 = 2960
NOTE_G7 = 3136
NOTE_GS7 = 3322
NOTE_A7 = 3520
NOTE_AS7 = 3729
NOTE_B7 = 3951
NOTE_C8 = 4186
NOTE_CS8 = 4435
NOTE_D8 = 4699
NOTE_DS8 = 4978

try:
	serialport = sys.argv[1]
except IndexError:
	help()

if ("COM" not in sys.argv[1]) and ("/dev/" not in sys.argv[1]):
	print("Serial port was not provided. Printing help:")
	help()
	
if (sys.argv[2].lower() == "test"):
		ser = connectSerial()
		print(serialport + " is functioning properly.")

if (sys.argv[2].lower() == "demo"):
		ser = connectSerial()
		print("Connected to Arduino!")
		demoTune()
		print("Demo Done!")
		sys.exit()
		
if (sys.argv[2].lower() == "play"):
	try:
		filename = sys.argv[3]
	except IndexError:
		print("Error: no file supplied.")
		sys.exit()
	ser = connectSerial()
	print("Connected to Arduino!")
	readFile()
	print("Music Playback Done!")
		

	