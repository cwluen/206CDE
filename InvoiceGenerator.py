import os
import tkinter as tk
from datetime import datetime
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import cx_Oracle
conn = cx_Oracle.connect('std004/cestd0516@144.214.177.102/xe')
cur = conn.cursor()

# ==== creating main class
class InvoiceGenerator:
   def __init__(self,root):
       self.root = root
       self.root.title("Invoice Generator By Towngas")
       self.root.geometry("750x800")

       # creating frame in window 
       self.frame=Frame(self.root,bg="white")
       self.frame.place(x=80,y=20, width=600, height=700)

       Label(self.frame, text="Towngas", font=("times new roman", 40, "bold"), bg="white", fg="Blue").place(x=150, y=55)
       Label(self.frame, text="Invoice generator", font=("times new roman", 20, "bold"), bg="white", fg="black").place(x=150, y=120)
       
       Label(self.frame, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=200)
       self.name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.name.place(x=150, y=200, width=400, height=35)
       
       Label(self.frame, text="Date", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
       self.date = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.date.place(x=150, y=260, width=400, height=35)

       Button(self.frame, text = "sql commit", command = self.database_collectall, font = ("times new roman", 14),fg = "white",cursor = "hand2", bg = "#B00857").place(x = 50,y = 640, width = 180, height = 40)	

       # ====submit details
       Button(self.frame, text = "Submit Details",command = self.generate_invoice, font = ("times new roman", 14),fg = "white",cursor = "hand2", bg = "#B00857").place(x = 300, y = 640, width = 180, height = 40)

# ==== SQL function
   def database_collectall(self):
         global A,B,C,D,E,F,G
         v0 = self.name.get()
         v1 = self.date.get()
         sql = "select a.*, b.*, c.* from member a, payment b, usage c where a.member_name = '{0}' and b.pay_before < to_date('{1}','dd-mm-yy') and a.member_name = '{0}' and b.member_id = a.member_id and c.member_id = a.member_id".format(v0,v1)
         cur.execute(sql)
         for row in cur.fetchall():
             A = row[0]
             B = row[1]
             C = row[2]
             D = str(row[4])
             E = str(row[5])
             F = row[6]
             G = str(row[10])

# ==== Invoice Generation Function
   def generate_invoice(self):
         c = canvas.Canvas("Invoice by Towngas.pdf", pagesize=(200, 250), bottomup=0)
         c.setFillColorRGB(0.8, 0.5, 0.7)

         c.line(5, 45, 195, 45)            #table
         c.line(15, 120, 185, 120)
         c.line(15, 108, 185, 108)
         c.line(15, 108, 15, 160)
         c.line(185, 108, 185, 160)
         c.line(57, 108, 57, 160)
         c.line(99, 108, 99, 160)
         c.line(141, 108, 141, 160)
         c.line(15, 160, 185, 160)

         c.setFont("Times-Bold", 10)
         c.drawCentredString(30, 20,"Towngas")

         c.setFont("Times-Bold", 8)
         c.drawCentredString(100, 55, "INVOICE")

         c.setFont("Times-Bold", 5)

         c.drawRightString(50, 70, "Invoice No. :")
         c.drawRightString(100, 70, "0290235")

         c.drawRightString(50, 75, "Date :")
         c.drawRightString(100, 75, datetime.today().strftime('%F'))

         c.drawRightString(50, 80, "Customer Name :")
         c.drawRightString(100, 80, self.name.get())

         c.drawRightString(50, 85, "Phone No. :")
         c.drawRightString(100, 85, B)
         
         c.drawRightString(50, 90, "Address:")
         c.drawRightString(150, 90, C)

         c.drawCentredString(36, 118, "Payment ID")
         c.drawCentredString(36, 130, F)
         c.drawCentredString(78, 118, "Pay Before")
         c.drawCentredString(78, 130, E[0:10])
         c.drawCentredString(120, 118, "Usage")
         c.drawCentredString(120, 130, G)
         c.drawCentredString(162, 118, "Price")
         c.drawCentredString(162, 130, D)

         c.line(15, 200, 185, 200)

         c.setFont("Times-Bold",3)
         c.drawRightString(185,205,"Self-reading by QR Code - Simple, Easy & Quick: A new Self-reading method has been lanuched.")
         c.drawRightString(185,208,"Simply scan your gas bill's QR Code,your account number will be displayed automatically. Entre the meter reading and submit.")

         c.showPage()
         c.save()

   # ==== creating main function
def main():
   # ==== create tkinter window
   root = Tk()
   # === creating object for class InvoiceGenerator
   obj = InvoiceGenerator(root)
   # ==== start the gui
   root.mainloop()

if __name__ == "__main__":
   # ==== calling main function
   main()
   # ==== creating object for class InvoiceGenerator
   obj = InvoiceGenerator(root)
   # ==== start the gui
   root.mainloop()

if __name__ == "__main__":
   # ==== calling main function
   main()