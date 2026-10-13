from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    def show_device(self):
        print(f"Device: {self.name}")

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is on. The room is now bright.")


class SmartFan(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is on. The blades are spinning to cool the room.")


class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is on. Music is now playing.")


class SmartTV(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is on. Loading your streaming apps.")


class SecurityCamera:
    def check_status(self):
        print("Security Camera: Online and recording.")


class DoorLock:
    def check_status(self):
        print("Door Lock: Locked and secure.")


print("--- Smart Devices (Abstraction and Overriding) ---")
light = SmartLight("Smart Light")
fan = SmartFan("Smart Fan")
speaker = SmartSpeaker("Smart Speaker")
tv = SmartTV("Smart TV")

for device in [light, fan, speaker, tv]:
    device.show_device()
    device.turn_on()
    print()

print("--- Security Devices (Polymorphism Without Inheritance) ---")
security_devices = [SecurityCamera(), DoorLock()]

for item in security_devices:
    item.check_status()