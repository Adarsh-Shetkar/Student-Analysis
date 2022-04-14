import pickle
from tkinter import *
from tkinter import font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# from tkinter import font
from tkinter.font import Font
# from tkinter import ttk
import matplotlib.pyplot as plt


def plot(n, s1, s2, m1, m2, sem):
    fig = Figure(figsize=(4, 2), dpi=100)
    plot1 = fig.add_subplot(1, 1, 1)
    slip1 = s1
    slip2 = s2
    mid1 = m1
    mid2 = m2
    x = ['DSA', 'OOP', 'MATH', 'CHEM']
    mid1_per = [m1[0] / 20 * 100, m1[1] / 20 * 100, m1[2] / 20 * 100,
                m1[3] / 20 * 100]  # mid1 marks in percentage
    mid2_per = [m2[0] / 20 * 100, m2[1] / 20 * 100, m2[2] / 20 * 100,
                m2[3] / 20 * 100]  # mid2 marks in percentage
    sem_per = [sem[0] / 60 * 100, sem[1] / 60 * 100, sem[2] / 60 * 100, sem[3] / 60 * 100]

    plot1.plot(x, mid1_per, marker='*')
    plot1.plot(x, mid2_per, marker='*')
    plot1.plot(x, sem_per, marker='*')
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=5)
    # l=Label(root,text="",bg="#95A5A6").grid(row=3,column=5)
    l = Label(root, text='Orange-Mid1\nBlue-Mid2\nGreen-Sem', fg="#CE0202", bg="#95A5A6", font=bigFont).grid(row=5,
                                                                                                             column=5)

    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()


# canvas.get_tk_widget().grid(row=12,column=0)


def plotting(num, st1, st2, mid1, mid2, sem, roll, name):
    temp = name + " " + str(roll)

    if num == 1:
        x = ['DSA', 'OOP', 'MATH', 'CHEM']
        st1_per = [st1[0] / 20 * 100, st1[1] / 20 * 100, st1[2] / 20 * 100,
                   st1[3] / 20 * 100]  # st1 marks in percentage
        plt.plot(x, st1_per, marker='*')
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.title(temp)
        plt.legend(['SLIP TEST 1'])
        plt.show()
    if num == 2:
        x = ["DSA", "OOP", "MATH", "CHEM"]
        st2_per = [st2[0] / 20 * 100, st2[1] / 20 * 100, st2[2] / 20 * 100, st2[3] / 20 * 100]
        st1_per = [st1[0] / 20 * 100, st1[1] / 20 * 100, st1[2] / 20 * 100, st1[3] / 20 * 100]
        plt.plot(x, st1_per, marker='*')
        plt.plot(x, st2_per, marker='*')
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.title(temp)
        plt.legend(['SLIPTEST 1', "SLIPTEST 2"])
        plt.show()
    if num == 3:
        x = ['DSA', 'OOP', 'MATH', 'CHEM']
        st2_per = [st2[0] / 20 * 100, st2[1] / 20 * 100, st2[2] / 20 * 100, st2[3] / 20 * 100]
        st1_per = [st1[0] / 20 * 100, st1[1] / 20 * 100, st1[2] / 20 * 100, st1[3] / 20 * 100]
        mid1_per = [mid1[0] / 20 * 100, mid1[1] / 20 * 100, mid1[2] / 20 * 100,
                    mid1[3] / 20 * 100]  # mid1 marks in percentage
        # mid2_per = [mid2[0]/20*100, mid2[1]/20*100, mid2[2]/20*100, mid2[3]/20*100] # mid2 marks in percentage
        plt.plot(x, mid1_per, marker='*')
        # plt.plot(x, mid2_per, marker='*')
        plt.plot(x, st1_per, marker='*')
        plt.plot(x, st2_per, marker='*')
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.title(temp)
        plt.legend(['SLIPTEST 1', "SLIPTEST 2", "MID-1"])
        plt.show()
    if num == 4:
        x = ["DSA", "OOP", "MATH", "CHEM"]
        mid1_per = [mid1[0] / 20 * 100, mid1[1] / 20 * 100, mid1[2] / 20 * 100,
                    mid1[3] / 20 * 100]  # mid1 marks in percentage
        mid2_per = [mid2[0] / 20 * 100, mid2[1] / 20 * 100, mid2[2] / 20 * 100,
                    mid2[3] / 20 * 100]  # mid2 marks in percentage
        # sem_per = [sem[0]/60*100, sem[1]/60*100, sem[2]/60*100, sem[3]/60*100] # sem marks in percentage
        st2_per = [st2[0] / 20 * 100, st2[1] / 20 * 100, st2[2] / 20 * 100, st2[3] / 20 * 100]
        st1_per = [st1[0] / 20 * 100, st1[1] / 20 * 100, st1[2] / 20 * 100, st1[3] / 20 * 100]
        plt.plot(x, st1_per, marker='*')
        plt.plot(x, st2_per, marker='*')
        plt.plot(x, mid1_per, marker='*')
        plt.plot(x, mid2_per, marker='*')
        # plt.plot(x, sem_per, marker='*')
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.title(temp)
        plt.legend(["SLIPTEST 1", "SLIPTEST 2", "MID-1", "MID-2"])
        plt.show()

    if num == 5:
        x = ["DSA", "OOP", "MATH", "CHEM"]
        mid1_per = [mid1[0] / 20 * 100, mid1[1] / 20 * 100, mid1[2] / 20 * 100,
                    mid1[3] / 20 * 100]  # mid1 marks in percentage
        mid2_per = [mid2[0] / 20 * 100, mid2[1] / 20 * 100, mid2[2] / 20 * 100,
                    mid2[3] / 20 * 100]  # mid2 marks in percentage
        sem_per = [sem[0] / 60 * 100, sem[1] / 60 * 100, sem[2] / 60 * 100,
                   sem[3] / 60 * 100]  # sem marks in percentage
        st2_per = [st2[0] / 20 * 100, st2[1] / 20 * 100, st2[2] / 20 * 100, st2[3] / 20 * 100]
        st1_per = [st1[0] / 20 * 100, st1[1] / 20 * 100, st1[2] / 20 * 100, st1[3] / 20 * 100]
        plt.plot(x, st1_per, marker='*')
        plt.plot(x, st2_per, marker='*')
        plt.plot(x, mid1_per, marker='*')
        plt.plot(x, mid2_per, marker='*')
        plt.plot(x, sem_per, marker='*')
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.title(temp)
        plt.legend(["SLIPTEST 1", "SLIPTEST 2", "MID-1", "MID-2", "SEM-END"])
        plt.show()


# plotting(3, [17, 18, 20, 19], [20, 19, 20, 17], [45, 55, 60, 50])   # this is a sample example how to add data
def make_marks(l1, l2, l3, l4):
    # ls=[len(l1),len(l2),len(l3),len(l4)]

    x = len(l1)

    st1 = []
    st2 = []
    mid1 = []
    mid2 = []
    sem = []

    for i in range(x):

        if i == 0:
            st1.append(l1[0])
            st1.append(l2[0])
            st1.append(l3[0])
            st1.append(l4[0])

        if i == 1:
            st2.append(l1[1])
            st2.append(l2[1])
            st2.append(l3[1])
            st2.append(l4[1])

        if i == 2:
            mid1.append(l1[2])
            mid1.append(l2[2])
            mid1.append(l3[2])
            mid1.append(l4[2])

        elif i == 3:
            mid2.append(l1[3])
            mid2.append(l2[3])
            mid2.append(l3[3])
            mid2.append(l4[3])

        elif i == 4:
            sem.append(l1[4])
            sem.append(l2[4])
            sem.append(l3[4])
            sem.append(l4[4])

    plot(x, st1, st2, mid1, mid2, sem)


class student_node:
    def __init__(self, *data):  # data=[roll,branch,name]
        self.roll = data[0]
        self.branch = data[1]
        self.name = data[2]

        # self.atten=data[3]

    def disp(self):
        # print(self.name)
        m = str(self.roll)
        # l=Label(root,text="R.NO:"+m,font=bigFont,bg="#95A5A6").grid(row=2,column=5)
        n = str(self.branch)
        # l=Label(root,text=m,font=bigFont,bg="#95A5A6").grid(row=3,column=5)
        o = str(self.name)
        l = Label(root, text="R.No:" + m + "\n" + n + "\n" + "WELCOME " + o, font=bigFont, bg="#95A5A6").grid(row=1,
                                                                                                              column=5)

        # print(self.dsa_mid1)

    def dsa(self, r):
        ldsa = []
        # print("DSA")s
        f_2 = open("dsa.dat", "rb")
        f_3 = open("studEN.dat", "rb")
        ls1 = pickle.load(f_3)
        for i in ls1:
            if i.roll == self.roll:
                break

            # i.disp()
        f_3.close()
        # l=Label(root,text="DSA",font=bigFont,bg="#95A5A6").grid(row=5,column=0)
        x = ["SLIPTEST-1", "SLIPTEST-2", "*mid1*******", "*mid2*******", "endsem****"]
        i = -1
        st = ""
        try:

            while 1:
                # if i==3:
                #  break
                i += 1
                ls2 = pickle.load(f_2)
                m = "*********" + str(x[i]) + "***********"

                n = str((ls2[r - 160120737121]))
                st += "\n" + m + n

                # l=Label(root,text=m+n,font=bigFont,bg="#95A5A6").grid(row=i+6,column=0)
                # l=Label(root,text=m).grid(row=i+7,column=0)
                ldsa.append(ls2[r - 160120737121])


        except EOFError:

            pass
        l = Label(root, text="DSA" + st, font=bigFont, bg="#95A5A6").grid(row=5, column=0)
        f_2.close()

        return ldsa

    def oop(self, r):
        loop = []
        # l=Label(root,text="OOP",font=bigFont,bg="#95A5A6").grid(row=5,column=3)
        f_2 = open("oop.dat", "rb")
        f_3 = open("studEN.dat", "rb")
        ls1 = pickle.load(f_3)
        # for i in ls1:
        #   if i.roll==self.roll:

        # i.disp()
        #      pass
        f_3.close()
        x = ["SLIPTEST-1", "SLIPTEST-2", "*mid1*******", "*mid2*******", "endsem****"]
        i = -1
        st = ""
        try:

            while 1:
                # if i==3:
                # break
                i += 1
                ls2 = pickle.load(f_2)
                m = "   *********" + str(x[i]) + "***********"

                n = str((ls2[r - 160120737121]))
                st += "\n" + m + n
                # l=Label(root,text=m+n,font=bigFont,bg="#95A5A6").grid(row=i+6,column=3)
                # l=Label(root,text=m).pack()
                loop.append(ls2[r - 160120737121])

        except EOFError:
            pass
        l = Label(root, text="OOP" + st, font=bigFont, bg="#95A5A6").grid(row=5, column=3)
        f_2.close()

        return loop

    def math(self, r):
        lmath = []
        # l=Label(root,text="MATH",font=bigFont,bg="#95A5A6").grid(row=11,column=0)#c0,r11
        f_2 = open("math.dat", "rb")
        f_3 = open("studEN.dat", "rb")
        ls1 = pickle.load(f_3)
        # for i in ls1:
        #    if i.roll==self.roll:

        # i.disp()
        #       pass
        f_3.close()
        x = ["SLIPTEST-1", "SLIPTEST-2", "*mid1*******", "*mid2*******", "endsem****"]
        i = -1
        st = ""
        try:

            while 1:
                # if i==3:
                #  break
                i += 1
                ls2 = pickle.load(f_2)
                m = " *********" + str(x[i]) + "***********"

                n = str((ls2[r - 160120737121]))
                # l=Label(root,text=m+n,font=bigFont,bg="#95A5A6").grid(row=i+12,column=0)
                # l=Label(root,text=m).pack()
                st += "\n" + m + n
                lmath.append(ls2[r - 160120737121])

        except EOFError:
            pass
        l = Label(root, text="MATH" + st, font=bigFont, bg="#95A5A6").grid(row=11, column=0)
        f_2.close()

        return lmath

    def chem(self, r):
        lchem = []
        # l=Label(root,text="CHEM",font=bigFont,bg="#95A5A6").grid(row=11,column=3)
        f_2 = open("chem.dat", "rb")
        f_3 = open("studEN.dat", "rb")
        ls1 = pickle.load(f_3)
        # for i in ls1:
        #    if i.roll==self.roll:

        # i.disp()
        #       pass
        f_3.close()
        x = ["SLIPTEST-1", "SLIPTEST-2", "*mid1*******", "*mid2*******", "endsem****"]
        i = -1
        st = ""
        try:

            while 1:
                # if i==3:
                #  break
                i += 1
                ls2 = pickle.load(f_2)
                m = str(("   **********" + str(x[i]) + "********"))

                n = str((ls2[r - 160120737121]))
                st += "\n" + m + n
                # l=Label(root,text=m+n,font=bigFont,bg="#95A5A6").grid(row=i+12,column=3)
                # l=Label(root,text=m).pack()
                lchem.append(ls2[r - 160120737121])

        except EOFError:
            pass
        f_2.close()
        l = Label(root, text="CHEM" + st, font=bigFont, bg="#95A5A6").grid(row=11, column=3)

        return lchem


#############################################################################
# maincode
stu = []
print("\n                                                                            WELCOME TO IT-3\n")
beg = 160120737121
names = ['ANAVI', 'BHAVITHA', 'GAYATRI', 'HARSHITHA', 'JHANSI', 'KAVYA', 'MANSI', 'MEGHANA', 'BHARGAVI', 'PALLAVI',
         'SAHITHI', 'NIKHITHA', 'SANTOSHI', 'SHIVATHMIKA', 'SINDHU', 'SRAVANTHI', 'TRISHIKA', 'TULASI', 'VAISHNAVI',
         'VAISHNAVI', 'VAISHNODEVI', 'VARSHA', 'ADARSH', 'AFFAN', 'AKHIL', 'AMEYA', 'ANURAAG', 'DHEERAJ', 'ESHWAR',
         'K.VARDHAN', 'C.VARDAN', 'KARTHIK', 'KARTIKEYA', 'KASHYAP', 'KRISHNA', 'KUSHAL', 'MANOJ', 'MAHBOOB', 'NAGI',
         'NIKHIL', 'PAWAN', 'PRANAV', 'PRASHANTH', 'REVANTH', 'RISHIL', 'MEHAR', 'SARATH', 'SATHVIK', 'K.TEJA',
         'T.TEJA', 'SAKETH', 'SHIVA', 'SIDHARTHA', 'SIFATHJEET', 'CHAITANYA', 'SRIKANTH', 'SRINATH', 'KRISHNA',
         'SUKUMAR', 'LUKMAN']
for i in names:
    nn = student_node(beg, "SEM-2 IT-3", i)
    stu.append(nn)
    beg += 1
f = open("studEn.dat", "wb")
pickle.dump(stu, f)
f.close()
c = ["SLIP TEST-1", "SLIP TEST-2", "MID-1", "MID-2", "SEM-END"]
while (1):

    ans = input("enter stu for student, admin for management :  ")

    if ans == "admin":
        subj = input("dsa or oop  or chem or math :  ")
        if subj == "dsa":
            f3 = open("county.txt", "a+")

            # password entry should happen

            f3.write("1")
            # f2=open("exam.dat","rb")
            # c=pickle.load(f2)
            # f2.close()
            f3.close()
            f4 = open("county.txt", "r")
            ch = f4.read()
            f4.close()
            l = len(ch)
            # print("*******",l,"******")
            if l == 1:

                it3_dsa_st1 = []
                print("*****", c[0], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_st1 = [20, 19, 18, 16, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("dsa.dat", "ab")
                pickle.dump(it3_dsa_st1, f_1)
                f_1.close()






            elif l == 2:

                it3_dsa_st2 = []
                print("*****", c[1], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_st2 = [20, 19, 18, 18, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("dsa.dat", "ab")
                pickle.dump(it3_dsa_st2, f_1)
                f_1.close()

            elif l == 3:

                it3_dsa_mid1 = []
                print("*****", c[2], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_mid1 = [20, 19, 18, 19, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("dsa.dat", "ab")
                pickle.dump(it3_dsa_mid1, f_1)
                f_1.close()




            elif l == 4:
                it3_dsa_mid2 = []
                print("*****", c[3], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_mid2 = [20, 20, 18, 19, 19, 17, 14, 15, 20, 20] * 6

                # for i in range(10):
                # stu[i].dsa(c[l-1],it3_dsa_mid2[i])

                f_1 = open("dsa.dat", "ab")
                pickle.dump(it3_dsa_mid2, f_1)
                f_1.close()



            elif l == 5:
                it3_dsa_endsem = []
                print("*****", c[4], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_endsem = [57, 55, 60, 54, 57, 58, 60, 60, 55, 52] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_endsem[i])
                f_1 = open("dsa.dat", "ab")
                pickle.dump(it3_dsa_endsem, f_1)
                f_1.close()





            else:
                print("ALL EXAMS DONE ")

        elif subj == "oop":
            fo = open("county1.txt", "a+")
            fo.write("1")
            # password entry should happen

            # f2=open("exam.dat","rb")
            # c=pickle.load(f2)
            # f2.close()
            fo.close()
            f5 = open("county1.txt", "r")
            ch = f5.read()
            f5.close()
            l1 = len(ch)
            # print("*******",l,"******")

            if l1 == 1:

                it3_dsa_st1 = []
                print("*****", c[0], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_st1 = [20, 19, 18, 15, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("oop.dat", "ab")
                pickle.dump(it3_dsa_st1, f_1)
                f_1.close()






            elif l1 == 2:

                it3_dsa_st2 = []
                print("*****", c[1], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_dsa_st2 = [20, 19, 18, 14, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("oop.dat", "ab")
                pickle.dump(it3_dsa_st2, f_1)
                f_1.close()





            elif l1 == 3:

                it3_oop_mid1 = []
                print("*****", c[2], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_oop_mid1 = [17, 16] * 30

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_o = open("oop.dat", "ab")
                pickle.dump(it3_oop_mid1, f_o)
                f_o.close()

            elif l1 == 4:
                it3_oop_mid2 = []
                print("*****", c[3], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_oop_mid2 = [19, 18] * 30

                # for i in range(10):
                # stu[i].dsa(c[l-1],it3_dsa_mid2[i])

                f_1 = open("oop.dat", "ab")
                pickle.dump(it3_oop_mid2, f_1)
                f_1.close()



            elif l1 == 5:
                it3_oop_endsem = []
                print("*****", c[4], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_oop_endsem = [58, 59] * 30

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_endsem[i])
                f_1 = open("oop.dat", "ab")
                pickle.dump(it3_oop_endsem, f_1)
                f_1.close()





            else:
                print("ALL EXAMS DONE ")

        elif subj == "math":
            f3 = open("county3.txt", "a+")

            f3.write("1")
            # f2=open("exam.dat","rb")
            # c=pickle.load(f2)
            # f2.close()
            f3.close()
            f4 = open("county3.txt", "r")
            ch = f4.read()
            f4.close()
            l = len(ch)
            # print("*******",l,"******")

            if l == 1:

                it3_math_st1 = []
                print("*****", c[0], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_math_st1 = [20, 19, 18, 19, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("math.dat", "ab")
                pickle.dump(it3_math_st1, f_1)
                f_1.close()






            elif l == 2:

                it3_math_st2 = []
                print("*****", c[1], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_math_st2 = [20, 19, 18, 15, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("math.dat", "ab")
                pickle.dump(it3_math_st2, f_1)
                f_1.close()






            elif l == 3:

                it3_math_mid1 = []
                print("*****", c[2], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_math_mid1 = [16, 17, 18, 19, 20] * 12

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("math.dat", "ab")
                pickle.dump(it3_math_mid1, f_1)
                f_1.close()

            elif l == 4:
                it3_math_mid2 = []
                print("*****", c[3], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_math_mid2 = [18, 16] * 30

                # for i in range(10):
                # stu[i].dsa(c[l-1],it3_dsa_mid2[i])

                f_1 = open("math.dat", "ab")
                pickle.dump(it3_math_mid2, f_1)
                f_1.close()



            elif l == 5:
                it3_math_endsem = []
                print("*****", c[4], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_math_endsem = [54, 55, 56, 57, 58] * 12
                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_endsem[i])
                f_1 = open("math.dat", "ab")
                pickle.dump(it3_math_endsem, f_1)
                f_1.close()





            else:
                print("ALL EXAMS DONE ")


        elif subj == "chem":
            f3 = open("county4.txt", "a+")

            # password entry should happen

            f3.write("1")
            # f2=open("exam.dat","rb")
            # c=pickle.load(f2)
            # f2.close()
            f3.close()
            f4 = open("county4.txt", "r")
            ch = f4.read()
            f4.close()
            l = len(ch)
            # print("*******",l,"******")

            if l == 1:

                it3_chem_st1 = []
                print("*****", c[0], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_chem_st1 = [20, 19, 18, 20, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("chem.dat", "ab")
                pickle.dump(it3_chem_st1, f_1)
                f_1.close()






            elif l == 2:

                it3_chem_st2 = []
                print("*****", c[1], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_chem_st2 = [20, 19, 18, 17, 17, 19, 20, 19, 18, 17] * 6

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("chem.dat", "ab")
                pickle.dump(it3_chem_st2, f_1)
                f_1.close()





            elif l == 3:

                it3_chem_mid1 = []
                print("*****", c[2], "*****")

                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_chem_mid1 = [20] * 60

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_mid1[i])
                f_1 = open("chem.dat", "ab")
                pickle.dump(it3_chem_mid1, f_1)
                f_1.close()

            elif l == 4:
                it3_chem_mid2 = []
                print("*****", c[3], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_chem_mid2 = [19, 18] * 30

                # for i in range(10):
                # stu[i].dsa(c[l-1],it3_dsa_mid2[i])

                f_1 = open("chem.dat", "ab")
                pickle.dump(it3_chem_mid2, f_1)
                f_1.close()



            elif l == 5:
                it3_chem_endsem = []
                print("*****", c[4], "*****")
                print("Entry Done")
                # it3_dsa=list(map(int,input('enter marks of 10 students by giving one space and enter after 10th student marks : ').split()))
                it3_chem_endsem = [55, 56] * 30

                # for i in range(10):
                #  stu[i].dsa(c[l-1],it3_dsa_endsem[i])
                f_1 = open("chem.dat", "ab")
                pickle.dump(it3_chem_endsem, f_1)
                f_1.close()





            else:
                print("ALL EXAMS DONE ")


    elif ans == "stu":
        a = g = q = f = t1 = c = 0

        root = Tk()
        l = Label(root, text="C.B.I.T", font=("Vineta BT", 40), bg="#95A5A6").grid(row=0, column=0)
        l = Label(root, text="Student Analysis", font=("Segoe Print", 27), bg="#95A5A6").grid(row=0, column=6)
        # l=Label(root,text="Analysis",font=("Segoe Print", 35),bg="#95A5A6").grid(row=1,column=6)
        root.geometry("1400x1400")
        bigFont = Font(family="Helvetica", size=13, slant="italic", underline=0, overstrike=0)
        root.configure(background="#95A5A6")
        # x2=Scrollbar(root,relief="flat").pack()
        e = Entry(root, font=bigFont)
        e.grid(row=0, column=5)
        root.title(" STUDENT ANALYSIS")


        def fun():
            root.attributes('-fullscreen', True)
            global e
            global c
            rollno = e.get()
            c = int(rollno)

            e.destroy()
            l = Label(root, text="  Section-H3  ", font=("Viner Hand ITC", 25), bg="#95A5A6")
            l.grid(row=0, column=5)
            l = Label(root, text="  Batch '24  ", font=("Viner Hand ITC", 25), bg="#95A5A6").grid(row=0, column=3)

            for k in stu:
                if k.roll == c:
                    k.disp()

                    def f1():
                        global a
                        global c
                        # print(c)
                        a = k.dsa(c)
                        # s1.destroy()

                    s1 = Button(root, text="DSA", command=f1, font=bigFont, fg="dark slate gray", bg="peach puff",
                                borderwidth=16.5, background="lightcyan1")
                    s1.grid(row=1, column=0)

                    def f2():
                        global g
                        global c
                        g = k.oop(c)

                    #  s2.destroy()

                    s2 = Button(root, text="OOP", command=f2, font=bigFont, fg="dark slate gray", bg="peach puff",
                                borderwidth=16.5, background="lightcyan1")
                    s2.grid(row=1, column=3)

                    def f3():
                        global q
                        global c
                        q = k.math(c)

                    #  s3.destroy()

                    s3 = Button(root, text="MATH", command=f3, font=bigFont, fg="dark slate gray", bg="peach puff",
                                borderwidth=16.5, background="lightcyan1")
                    s3.grid(row=2, column=0)

                    def f4():
                        global f
                        global c
                        f = k.chem(c)

                    # s4.destroy()

                    s4 = Button(root, text="CHEM", command=f4, font=bigFont, fg="dark slate gray", bg="peach puff",
                                borderwidth=16.5, background="lightcyan1")
                    s4.grid(row=2, column=3)

                    def f5():
                        global a
                        global g
                        global q
                        global f
                        make_marks(a, g, q, f)
                        # s5.grid(row=5,column=5)
                        # plot()
                        # s5.destroy()'''
                        l = Label(root, text="\nVaishno|Varsha|Adarsh|Affan|Akhil", bg="#95A5A6", font=("Vivaldi", 20))
                        l.grid(row=12, column=5)
                        global t1
                        t1 = Text(root, height=2, width=6)
                        t1.grid(row=5, column=6)

                        def f6():
                            global t1
                            t1.destroy()

                            l = Label(root, text="Thank You", font=("Brush Script MT", 25), bg="#95A5A6")
                            l.grid(row=5, column=6)

                            pass

                        s6 = Button(root, text="Feedback Submit", font=bigFont, command=f6, fg="dark slate gray",
                                    bg="peach puff", borderwidth=16.5, background="lightcyan1")
                        s6.grid(row=11, column=6)

                    s5 = Button(root, text="GET GRAPH", command=f5, font=bigFont, fg="dark slate gray", bg="peach puff",
                                borderwidth=16.5, background="lightcyan1")
                    s5.grid(row=2, column=6)

                    b.destroy()

                    def log():
                        root.destroy()

                    z = Button(root, text=" LOG  OUT ", command=log, font=bigFont, fg="dark slate gray",
                               bg="peach puff", borderwidth=16.5, background="lightcyan1").grid(row=1, column=6,
                                                                                                padx=25, pady=25)

                # k=Label(root,text=str(a))
                # k.pack()
                # b= i.oop()
                # c= i.math()
                # d= i.chem()
                # make_marks(a,b,c,d,i.roll,i.name)


        b = Button(root, text="ENTER YOUR ROLL NO AND CLICK HERE TO GET DETAILS", command=fun, font=bigFont,
                   fg="dark slate gray", bg="peach puff", borderwidth=16.5, background="lightcyan1")
        b.grid(row=1, column=5, padx=25, pady=25)
        root.mainloop()




    elif ans == "stop":
        print("done")
        break
