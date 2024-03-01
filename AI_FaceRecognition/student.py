from tkinter import*
from tkinter import ttk
# powerful GUI application software
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x790+0+0")
        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        #setting tkinter window size
        self.root.geometry("%dx%d" % (width, height))

        
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # ===================Variables==============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

       # first image
        # img = Image.open(r"project_images/student.jpeg")
        # # high level image to low level image
        # img = img.resize((500, 130), Image.Resampling.LANCZOS)
        # # save image
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=500, height=130)

        # # second image
        # img1 = Image.open(r"project_images/image 2.jpeg")
        # img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl.place(x=500, y=0, width=500, height=130)

        # # third image
        # img2 = Image.open(r"project_images/image 3.jpeg")
        # img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl.place(x=1000, y=0, width=560, height=130)

        # bg image
        img3 = Image.open(
            r"project_images/7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl = Label(self.root, image=self.photoimg3)
        bg_lbl.place(x=0, y=0, width=1530, height=710)

        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Text(bg_lbl, bd=2, bg="white")
        main_frame.place(x=-20, y=50, width=1480, height=600)

        v = Scrollbar(self.root)
        v.pack(side = RIGHT, fill = Y)
   
        # bg_frame.pack(fill=BOTH, expand=True)
        # main_frame.pack(side=TOP, fill=X) #ank
        v.config(command=main_frame.yview)       #ank

        # left lable frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(
            r"project_images/IMG_20230308_114906.jpeg")
        img_left = img_left.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # current course
        current_course_frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        dep_label = Label(current_course_frame, text="Discipline", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "ECE", "ME", "SM", "Design")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # course
        dep_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Course", "B.tech",
                               "B.des", "M.tech", "PHD")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        dep_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Year", "2022",
                               "2021", "2020", "2019", "2018")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        dep_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Semester", "Semester 1", "Semester 2")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

#       student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=720, height=300)

        # student id
        studentId_label = Label(class_student_frame, text="StudentId:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=(
            "times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll no.

        Roll_no_label = Label(class_student_frame, text="Roll no", font=(
            "times new roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 13, "bold"))
        Roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender

        gender_label = Label(class_student_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DoB

        dob_label = Label(class_student_frame, text="Dob", font=(
            "times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # EMAIL

        email_label = Label(class_student_frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no

        phoneno_label = Label(class_student_frame, text="Phone number", font=(
            "times new roman", 12, "bold"), bg="white")
        phoneno_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phoneno_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 13, "bold"))
        phoneno_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name

        Teacher_label = Label(class_student_frame, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg="white")
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 13, "bold"))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white",command=self.update_data,width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="delete", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", command=self.delete_data, width=17)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="reset", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", command=self.reset_data, width=17)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        takephotosample_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=35)
        takephotosample_btn.grid(row=1, column=0)

        updatephoto_btn = Button(btn_frame1, text="Update Photo Sample", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=35)
        updatephoto_btn.grid(row=1, column=1)

        # Right lable frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=690, height=580)

        img_right = Image.open(
            r"project_images/IMG_20230308_114906.jpeg")
        img_right = img_right.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ==============Search System=======================
        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=700, height=70)

        search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 12, "bold"), width=14, state="readonly")
        search_combo["values"] = ("Select", "Roll No", "PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(
            Search_frame, width=20, font=("times new roman", 13, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Update", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=10)
        search_btn.grid(row=0, column=3, padx=4)

        delete_btn = Button(Search_frame, text="delete", font=(
            "times new roman", 13, "bold"), bg="blue", fg="white", width=10)
        delete_btn.grid(row=0, column=4, padx=4)

        # ========================table frame====================
        Table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, font=(
            "times new roman", 12, "bold"))
        Table_frame.place(x=5, y=210, width=680, height=350)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "RollNo", "Gender",
                                          "dob", "email", "phone", "adrress", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Discipline")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId:")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Class Division:")
        self.student_table.heading("RollNo", text="Roll no")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone number")
        self.student_table.heading("adrress", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("RollNo", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("adrress", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =====================function decration============

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Sucess", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

# ===========================fetch data=================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="", database="face_recognition_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # =============get cursor============
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])



# update function


    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Classdiv=%s,RollNo=%s,Gender=%s,Dob=%s,Email=%s,Phone_number=%s,Address=%s,Teacher_Name=%s,PhotoSamplestatus=%s where StudentId=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Upadate:
                        return
                    # reset nhi hai shayad
                messagebox.showinfo("success", "Student details successfull update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)
    # delete function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentId=%s"
                    val = self.var_std_id.get()
                    my_cursor.execute(sql, (val, ))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Succesfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set("Select Division"),
        self.var_gender.set(""),
        self.var_dob.set("Male"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        self.var_std_id.set("")

# generate dataset or take photo samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Classdiv=%s,RollNo=%s,Gender=%s,Dob=%s,Email=%s,Phone_number=%s,Address=%s,Teacher_Name=%s,PhotoSamplestatus=%s where StudentId=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1 
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #  ************************ load predefined data on face frontals from opencv***********
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                faces = face_classifier.detectMultiScale(
                                     gray, 1.3, 5)
                                # scaling factor=1.3
                                # neighbour minimum=5
                                for (x, y, w, h) in faces:
                                    face_cropped = img[y:y+h, x:x+w]
                                    return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                                    img_id += 1
                                    face = cv2.resize(
                                    face_cropped(my_frame), (500, 500))
                                    face = cv2.cvtColor(
                                        face, cv2.COLOR_BGR2GRAY)
                                    file_name_path = "data/user." +str(id)+"."+str(img_id)+".jpg"
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                    cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                    break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!!")
            except Exception as es:
                        messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
