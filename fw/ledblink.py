import machine
import time

led_pin = machine.Pin(29, machine.Pin.OUT)

print("Blinking onboard LED2, ctrl-c to stop")

try:
    while True:
        led_pin.value(1)
        time.sleep(0.5)
        led_pin.value(0)
        time.sleep(0.5)

except KeyboardInterrupt:
    led_pin.value(0)
    print("Stopped")