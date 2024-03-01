from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        
        # Load images from the same path
        img_path = "project_images/"
        img = Image.open(img_path + "student.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        img1 = Image.open(img_path + "image 2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img3 = Image.open(img_path + "7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Create and place labels for images
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        bg_lbl = Label(self.root, image=self.photoimg3)
        bg_lbl.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        # Right label frame
        right_frame = LabelFrame(main_frame , bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=690, height=580)

        # Left inside frame
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=10, width=710, height=555)

        # Labels and Entry Widgets
        labels = ["AttendanceID:","RollNo", "Name:", "Date:", "Department:", "Time:"]
        for i, label_text in enumerate(labels):
            label = Label(left_inside_frame, text=label_text, font=("times new roman", 12, "bold"), bg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky=W)
    
            entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=W)

        # Attendance Status Combobox
        attendance_status_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        attendance_status_values = ["status", "present", "absent"]
        attendance_status_combobox = ttk.Combobox(left_inside_frame, values=attendance_status_values, state="readonly", font=("times new roman", 13, "bold"))
        attendance_status_combobox.set("status")  # Set the default value
        attendance_status_combobox.grid(row=5, column=1, padx=10, pady=5, sticky=W)
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=715, height=35)
        
        save_btn = Button(btn_frame, text="Import csv", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white",width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="update", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=680, height=500)

# ===============================scroll bas and tables===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","name","rollno","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("id",text="AttendanceID:")
        self.AttendanceReportTable.heading("Roll",text="RollNo")
        self.AttendanceReportTable.heading("Name",text="Name:")
        self.AttendanceReportTable.heading("Department",text="Department:")
        self.AttendanceReportTable.heading("time",text="Time:")
        self.AttendanceReportTable.heading("Date",text="Date:")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("time",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
