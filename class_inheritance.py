class Device:
    def __init__(self,name,conn_by):
        self.name=name
        self.conn_by=conn_by
        self.connected=True
    def __str__(self):
        return f"Device {self.name!r} ({self.conn_by})"
    
    def disconnected(self):
        self.connected=False
        print("Device is disconnected")

    
# printer=Device("printer","usb")
# print(printer)
# printer.disconnected()
class Printer(Device):
    def __init__(self,name, conn_by,capacity):
        super().__init__(name,conn_by)
        self.capacity=capacity
        self.remaining_pages=capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self,pages):
        if not self.connected:
            print("your printer is connected")
            return

        print(f"printing {pages} pages")
        self.remaining_pages-=pages
        
printer=Printer("printer","usb",600)
printer.print(50)
printer.print(50)
print(printer)
printer.disconnected()

    

     


