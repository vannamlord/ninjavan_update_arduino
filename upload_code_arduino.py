import subprocess
import os

# install lib
# sudo apt-get install avrdude python3-serial
# Replace '/dev/ttyACM0' with the actual port where your Arduino is connected
arduino_port_1 = '/dev/ttyACM0'
arduino_port_2 = '/dev/ttyACM1'

# Path to the hex file (compiled Arduino sketch)
hex_file = '/home/admin1/Desktop/dws_record/show_size.ino.hex'

def upload_code():
    try:
        # Upload the code using avrdude
        if(os.path.exists(arduino_port_1)):
            subprocess.check_call(['avrdude', '-v', '-patmega328p', '-carduino', '-P' \
                + arduino_port_1, '-b115200', '-D', '-Uflash:w:' + hex_file + ':i'])
        else:
            subprocess.check_call(['avrdude', '-v', '-patmega328p', '-carduino', '-P' \
                + arduino_port_2, '-b115200', '-D', '-Uflash:w:' + hex_file + ':i'])
        print("Code uploaded successfully.")
    except:
        print("No connection with Arduino")
        pass

if os.path.exists(arduino_port_1) or os.path.exists(arduino_port_2):
    upload_code()
