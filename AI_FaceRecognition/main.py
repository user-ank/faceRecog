from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

from tkinter import *
from PIL import Image, ImageTk

class Face_recognition_System:
    def __init__(self, root):
        self.root = root

        # self.root.attributes('-fullscreen', True)
        # self.root.geometry("1280x650+0+0")
        self.root.title("Face Recognition system")
        self.create_widgets()

    def create_widgets(self):
        bg_frame = Text(self.root)

        v = Scrollbar(self.root)
        v.pack(side = RIGHT, fill = Y)
   
        # bg_frame.pack(fill=BOTH, expand=True)
        bg_frame.pack(side=TOP, fill=X) #ank
        v.config(command=bg_frame.yview)       #ank


        title_lbl = Label(bg_frame, text="FACE RECOGNITION SYSTEM", font=("times new roman", 35, "bold"), bg="#efd9b4", fg="#292522")
        title_lbl.grid(row=0, column=0, columnspan=4, sticky="ew")

        buttons_data = [
            ("Student Details", "student.jpeg", self.student_details),
            ("Face Detector", "face detector.jpeg", self.face_data),
            ("Train Data", "traindata.jpeg", self.Train_data),
            ("Photos", "photos.jpeg", self.openImg),
            ("Attendance", "attendance.jpeg", None),
            ("Developer", "developer.jpeg", None),
            ("Help Desk", "help desk.jpeg", None),
            ("Exit", "exit.jpeg", None)
        ]

        row = 1
        col = 0
        for label_text, img_filename, command in buttons_data:
            img = Image.open(f"project_images/{img_filename}")
            img = img.resize((220, 220), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)

            button = Button(bg_frame, image=photo_img, text=label_text, font=("times new roman", 15, "bold"),
                            bg="#a39081", fg="#292522", cursor="hand2", compound="top", command=command, pady=10)
            button.image = photo_img

            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

            bg_frame.columnconfigure(col, weight=1)
            bg_frame.rowconfigure(row, weight=1)

        bg_frame.columnconfigure(0, weight=1)
        bg_frame.columnconfigure(1, weight=1)
        bg_frame.columnconfigure(2, weight=1)
        bg_frame.columnconfigure(3, weight=1)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def openImg(self):
        import os
        os.startfile("data")

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    # root.geometry("%dx%d" % (width, height))

    obj = Face_recognition_System(root)
   
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
    