import machine
import time

print("Start")

for pin_num in range(48):
    try:
        current_pin = machine.Pin(pin_num, machine.Pin.OUT)
        
        print(f"GP{pin_num}: HIGH")
        current_pin.value(1)
        
        time.sleep(1)
        
        print(f"GP{pin_num}: LOW")
        current_pin.value(0)
        
    except ValueError as e:
        # if something goes that terribly wrong
        # (if it doesnt let you use all the gpios)
        print(f"Could not configure GP{pin_num}: {e}")

print("Done")