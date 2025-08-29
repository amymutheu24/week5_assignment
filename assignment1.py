# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Call parent constructor
        self.os = os
        self.storage = storage
        self.battery = 100  # default battery level

    def make_call(self, number):
        print(f" Calling {number} using {self.info()}...")

    def charge(self):
        self.battery = 100
        print(f" {self.info()} is fully charged.")

    def use_app(self, app_name):
        if self.battery > 10:
            self.battery -= 10
            print(f" Using {app_name} on {self.info()}... Battery: {self.battery}%")
        else:
            print(f" Low battery! Please charge {self.info()}.")


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", "iOS", "128GB")
phone2 = Smartphone("Samsung", "Galaxy S23", "Android", "256GB")

phone1.make_call("123-456-7890")
phone2.use_app("YouTube")
phone1.charge()
