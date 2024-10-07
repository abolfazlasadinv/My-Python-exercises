import time
import random

def read_temperatur():

    return random.uniform(5, 15)

def turn_on_cooler():
    print("cooler is ON")
    
def turn_off_cooler():
    print("cooler is OFF")
    
    
cooler_status = False

target_temperatur = 10

while True:
    temperatur = read_temperatur()
    print(f"current temperature: {temperatur: .2f}°c")
    
    if temperatur > target_temperatur:
        if not cooler_status:
            turn_on_cooler()
            cooler_status = True
    elif temperatur < target_temperatur:
    
        if cooler_status:
            turn_off_cooler()
            cooler_status = False
            
        time.sleep(5)
            
