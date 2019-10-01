class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} is connected by {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print("Disconnect")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining = capacity

    def __str__(self):
        return f"{super().__str__()} (pages remaining : {self.remaining})"


    def print(self, pages):
        if self.connected != True:
            return "The printer is not connected"

        else:
            print(f"printing {pages} pages")
            self.remaining -= pages


printer = Printer("HP", "USB", 500)

printer.print(30)
print(printer)
