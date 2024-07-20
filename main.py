import tkinter as tk
from tkinter import ttk
import calendar
import datetime
import Mathematics 
import tkinter.messagebox as mb
main_win=tk.Tk()
main_win.geometry("200x150")
main_win.maxsize(200,150)
main_win.maxsize(200,150)
main_win.title("3-C")
photo_main=tk.PhotoImage(file="main_icon.png")
main_win.iconphoto(False,photo_main)

"""************************************* UNIT CONVERTOR **********************************************"""

def unit_convertor():

    def convert():
        nonlocal first
        nonlocal second
        nonlocal ent_second
        

        """ this function do the main conversion"""
        first_option=combo_first.get()
        second_option=combo_second.get()

        first_value=int(first.get())
        mathh=Mathematics.Math()

        """ main operation """
        if first_option==second_option:
            mb.showerror("Invalid operation!",f"Can't convert {first_option} to {second_option} ")
   
        elif first_option=='m' and second_option=='cm':
            result=mathh.m_cm(m=first_value)
        elif first_option=='cm' and second_option=='m':
            result=mathh.cm_m(cm=first_value)
        elif first_option=='km' and second_option=='m':
            result=mathh.km_m(km=first_value)
        elif first_option=='m' and second_option=='km':
            result=mathh.m_km(m=first_value)
        elif first_option=='foot' and second_option=='inch':
            result=mathh.foot_inch(f=first_value)
        elif first_option=='inch' and second_option=='foot':
            result=mathh.inch_foot(i=first_value)
        elif first_option=='cm' and second_option=='mm':
            result=mathh.cm_mm(cm=first_value)
        elif first_option=='mm' and second_option=='cm':
            result=mathh.mm_cm(mm=first_value)
        elif first_option=='mile' and second_option=='yard':
            result=mathh.mile_yard(m=first_value)
        elif first_option=='yard' and second_option=='mile':
            result=mathh.yard_mile(y=first_value)
        elif first_option=='l' and second_option=='ml':
            result=mathh.l_ml(l=first_value)
        elif first_option=='ml' and second_option=='l':
            result=mathh.ml_l(ml=first_value)
        elif first_option=='kg' and second_option=='g':
            result=mathh.kg_g(kg=first_value)
        elif first_option=='g' and second_option=='kg':
            result=mathh.g_kg(g=first_value)
        elif first_option=='kg' and second_option=='tonne':
            result=mathh.kg_tonne(kg=first_value)
        elif first_option=='tonne' and second_option=="kg":
            result=mathh.tonne_kg(t=first_value)

        elif first_option=='fah' and second_option=='celsius':
            result=mathh.fah_celsius(f=first_value)
        elif first_option=='celsius' and second_option=='fah':
            result=mathh.celsius_fah(c=first_value)
        elif first_option=='kelvin' and second_option=='celsius':
            result=mathh.kel_celsius(k=first_value)
        elif first_option=='celsius' and second_option=='kelvin':
            result=mathh.celsius_kel(c=first_value)
        elif first_option=='fah' and second_option=='kelvin':
            result=mathh.fah_kelvin(f=first_value)
        elif first_option=='kelvin' and second_option=='fah':
            result=mathh.kelvin_fah(k=first_value)
        else:
            mb.showerror("Invalid operation!",f"Can't convert {first_option} to {second_option}")

        second.set(result)
        ent_second.update()
            
        
    
    """ some variables """
    first=tk.StringVar()
    second=tk.StringVar()
    width = 370
    height = 380

    """ geometry of window"""
    root_convertor=tk.Toplevel()
    root_convertor.geometry(f"{width}x{height}")
    root_convertor.title("Unit Convertor ")
    root_convertor.minsize(width, height)
    root_convertor.maxsize(width, height)
    photo_conv=tk.PhotoImage(file="convertor.png")
    root_convertor.iconphoto(False,photo_conv)

    
    """ label and frame for unitconvertor heading """
    frm1_conv=tk.Frame(root_convertor,width=350,height=25,relief=tk.SUNKEN,borderwidth=15,bg="red")
    frm1_conv.pack(anchor="nw")
    tk.Label(frm1_conv,text="  Unit\nConvertor",width=50,height=2,font="Arial 15 bold",padx=13).pack()
    

    """ frame for options """
    frm2_conv=tk.Frame(root_convertor,width=350,height=250,relief=tk.SUNKEN,borderwidth=2)
    frm2_conv.pack()
    combo_first=ttk.Combobox(frm2_conv,width=5,state="readonly")
    combo_first['value']=('m','cm','l','ml','yard','mm','kg','g','mile','yard','celsius','fah','kelvin','km','inch','foot')
    ent_first=tk.Entry(frm2_conv,textvariable=first)
    ent_first.pack(side=tk.RIGHT,padx=5,pady=5)
    combo_first.pack(pady=5)

    frm3_conv=tk.Frame(root_convertor,width=350,height=250,relief=tk.SUNKEN,borderwidth=2)
    frm3_conv.pack()
    combo_second=ttk.Combobox(frm3_conv,width=5,state="readonly")
    combo_second['values']=('m','cm','l','ml','yard','mm','kg','g','mile','yard','celsius','fah','kelvin','km','inch','foot')
    combo_first.set('m')
    combo_second.set('cm')
    ent_second=tk.Entry(frm3_conv,textvariable=second)
    ent_second.pack(side=tk.RIGHT,padx=5,pady=20)
    combo_second.pack(pady=20)
    frm4_conv=tk.Frame(root_convertor)
    frm4_conv.pack()
    ttk.Button(frm4_conv,text="Submit",command=convert).pack()
    root_convertor.mainloop()



    
    
    

""" ************************************ CALCULATOR ***************************************************"""

def calculator():
    val=tk.StringVar()
    root = tk.Toplevel()
    photo_calc=tk.PhotoImage(file="calculator.png")
    root.iconphoto(False,photo_calc)

    """ some variables"""
    width = 370
    height = 380

    """ geometry of window"""
    root.geometry(f"{width}x{height}")
    root.title("Calculator")
    root.minsize(width, height)
    root.maxsize(width, height)


    """functions """

    def calculation(event):
        nonlocal val
        value = event.widget.cget("text")
        if value == "C":
            value = ""
        elif value == "=":
            try:
                value = eval(ent.get())
            except Exception as e:
                value = "Invalid operation!"

        else:
            value = val.get() + value

        val.set(value)
        ent.update()

    """ frame and label for main claculating area"""
    frm = tk.Frame(root, width=40, height=10, borderwidth=6, relief=tk.SUNKEN, bg="red", padx=34)
    frm.pack(side=tk.TOP, anchor="nw")
    ent = ttk.Entry(frm, textvariable=val, width=40, font="Arial 19 bold")
    ent.pack(side=tk.TOP, anchor="nw")

    frm2 = tk.Frame(root, width=500, height=280, borderwidth=5, relief=tk.SUNKEN)
    frm2.pack(anchor="ne")

    """ lists for roe,column and text"""
    lst_btn_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0", "=", "+", "-", "*", "/", "C", "(", ")", "%"]
    lst_btn_row = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0, 1, 2, 3, 4, 4, 4, 4]
    lst_btn_column = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 3, 3, 3, 0, 1, 2, 3]

    """ buttons and packing it on frm2"""
    for index, btns_text in enumerate(lst_btn_text):
        btn1 = tk.Button(frm2, text=lst_btn_text[index], width=7, height=2, bg="black", fg="white",
                         font="Arial 15 bold")
        btn1.grid(row=lst_btn_row[index], column=lst_btn_column[index], sticky="ne")
        btn1.bind("<Button-1>", calculation)
    root.mainloop()

"""************************************* CALENDAR *********************************************************************"""

def calenderr():

    def main_calender():
        nonlocal year
        nonlocal month
        """ label for calendar"""
        main_calendar=calendar.month(int(year.get()),int(month.get()))
        ttk.Label(frm_3,text=main_calendar,font=" bold").place(x=80,y=50)


    """ variables to store year and month"""
    year=tk.StringVar()
    month=tk.StringVar()

    """ fetching current year and current month"""
    current_datetime = str(datetime.datetime.now())
    lst_date_month = current_datetime.split("-")
    current_year=lst_date_month[0]
    current_month=lst_date_month[1]
    year.set(current_year)

    """ window and managing its geometry,title and icon"""
    root_calendar=tk.Toplevel()
    root_calendar.geometry("350x350")
    root_calendar.minsize(350,350)
    root_calendar.maxsize(350,350)
    root_calendar.title("Calendar")
    photo_cal=tk.PhotoImage(file="calendar.png")
    root_calendar.iconphoto(False,photo_cal)

    """ Frame 1 and Label for Calendar heading"""
    frm_1=tk.Frame(root_calendar,width=350,height=25,relief=tk.SUNKEN,borderwidth=15,bg="red")
    frm_1.pack(anchor="nw")
    tk.Label(frm_1,text="Calendar",width=50,height=2,font="Arial 15 bold",padx=13).pack()

    """ frame 2 and label year,month,entry and combobox"""
    frm_2=tk.Frame(root_calendar,width=350,height=250,relief=tk.SUNKEN,borderwidth=2)
    frm_2.pack(side=tk.LEFT,anchor="nw")

    ttk.Label(frm_2,text="Year",width=12).grid(row=0,column=0)
    ttk.Entry(frm_2,textvariable=year,width=12).grid(row=0,column=1)
    ttk.Label(frm_2,text="Month",width=12).grid(row=0,column=2)
    combo_box=ttk.Combobox(frm_2, textvariable=month, width=12,state="readonly")
    combo_box.grid(row=0,column=3)
    combo_box['values']=(1,2,3,4,5,6,7,8,9,10,11,12)
    combo_box.set(int(current_month))


    """ button to see the calendar"""
    frm_3=tk.Frame(root_calendar,relief=tk.SUNKEN,borderwidth=2,height=228,width=348)
    frm_3.place(x=0,y=120)
    ttk.Button(frm_3,text="Submit",command=main_calender).place(x=130,y=5)


    root_calendar.mainloop()


"""****************************************** MAIN WINDOW *************************************************************"""

ttk.Button(text="Calculator",command=calculator).pack(pady=6)
ttk.Button(text="Calendar",command=calenderr).pack(pady=6)
ttk.Button(text="   Unit\nconvertor",command=unit_convertor).pack(pady=6)
main_win.config(bg="#399E9E")
tk.Label(text="Vishwa -Make It Easy!",fg="black",bg="#399E9E").pack(pady=5,anchor="ne")

main_win.mainloop()






