from tkinter import*
from PIL import Image, ImageTk


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital  Management System")
        self.root.geometry("1550X800+0+0")


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

