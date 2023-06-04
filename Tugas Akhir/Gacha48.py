import random
from tkinter import *
import tkinter.messagebox as msg
import tkinter as tk
from tkvideo import tkvideo
from PIL import ImageTk, Image
import sys
import time
import threading


class gacha48:
    def __init__(self, gui, header):
        self.gui = gui
        self.gui.geometry("961x541")
        self.gui.title(header)
        self.gui.resizable(0, 0)
        self.gacha_count = 0
        self.inventory = []
        self.main_screen()

    def main_screen(self):
        self.bg = ImageTk.PhotoImage(Image.open("background-02.png"))
        self.b_main = Label(
            window,
            image=self.bg,
        )
        self.b_main.place(anchor="center", relx=0.5, rely=0.5)

        self.lgn = Button(
            text="Login",
            bg="#2CC797",
            fg="black",
            height="1",
            width="20",
            font=("Raleway", 12, "bold"),
            relief="flat",
            command=self.login,
        )
        self.lgn.place(x=250, y=418)

        self.rgs = Button(
            text="Register",
            bg="#3D6DBA",
            fg="black",
            height="1",
            width="20",
            font=("Raleway", 12, "bold"),
            relief="flat",
            command=self.register,
        )
        self.rgs.place(x=480, y=418)

        self.exit_program = Button(
            text="Exit",
            bg="#C7C7D2",
            fg="black",
            height="1",
            width="20",
            relief="solid",
            font=("Raleway", 10, "bold"),
            command=exit_program,
        )
        self.exit_program.place(x=388, y=470)

    def login(self):
        self.lgn.destroy()
        self.rgs.destroy()
        self.exit_program.destroy()

        self.entryEmail = Entry(
            window,
            bg="#8C8C94",
            highlightcolor="#FFFFFF",
            width=33,
            relief="flat",
            font=("Raleway", 10, "normal"),
        )
        self.entryEmail.place(x=324, y=397)
        self.entryEmail.insert(0, "Masukan Email Anda...")
        self.entryEmail.bind("<FocusIn>", self.on_entry_click)
        self.entryEmail.bind("<FocusOut>", self.on_focusout)
        self.entryEmail.config(fg="black")

        self.entryPass = Entry(
            window,
            bg="#8C8C94",
            highlightcolor="#FFFFFF",
            width=33,
            relief="flat",
            font=("Raleway", 10, "normal"),
        )
        self.entryPass.place(x=324, y=427)
        self.entryPass.insert(0, "Masukkan Password Anda...")
        self.entryPass.bind("<FocusIn>", self.on_entry_click2)
        self.entryPass.bind("<FocusOut>", self.on_focusout2)
        self.entryPass.config(fg="black")
        self.check = IntVar()
        self.showPass = Checkbutton(
            window,
            text="Tampilkan Password",
            fg="black",
            variable=self.check,
            command=self.open_password,
            height="1",
            width="18",
            font=("Raleway", 7, "normal"),
        ).place(x=335, y=457)
        self.showPass
        self.btnlogin = Button(
            window,
            text="Login",
            bg="#2CC797",
            fg="black",
            width="10",
            font=("Raleway", 12, "bold"),
            relief="flat",
            command=self.do_login,
        ).place(x=342, y=487)

        self.btnCancel = Button(
            window,
            text="Cancel",
            bg="#C7C7D2",
            fg="black",
            width="10",
            font=("Raleway", 12, "bold"),
            relief="solid",
            command=self.main_screen,
        ).place(x=468, y=487)

    def register(self):
        self.lgn.destroy()
        self.rgs.destroy()
        self.exit_program.destroy()

        self.entryUserName = Entry(
            window,
            bg="#8C8C94",
            highlightcolor="#FFFFFF",
            width=33,
            relief="flat",
            font=("Raleway", 10, "normal"),
        )
        self.entryUserName.place(x=324, y=386)
        self.entryUserName.insert(0, "Masukkan Username Anda...")
        self.entryUserName.bind("<FocusIn>", self.on_entry_click3)
        self.entryUserName.bind("<FocusOut>", self.on_focusout3)
        self.entryUserName.config(fg="black")
        self.entryEmail = Entry(
            window,
            bg="#8C8C94",
            highlightcolor="#FFFFFF",
            width=33,
            relief="flat",
            font=("Raleway", 10, "normal"),
        )
        self.entryEmail.place(x=324, y=411)
        self.entryEmail.insert(0, "Masukan Email Anda...")
        self.entryEmail.bind("<FocusIn>", self.on_entry_click)
        self.entryEmail.bind("<FocusOut>", self.on_focusout)
        self.entryEmail.config(fg="black")
        self.entryPass = Entry(
            window,
            bg="#8C8C94",
            highlightcolor="#FFFFFF",
            width=33,
            relief="flat",
            font=("Raleway", 10, "normal"),
        )
        self.entryPass.place(x=324, y=436)
        self.entryPass.insert(0, "Masukkan Password Anda...")
        self.entryPass.bind("<FocusIn>", self.on_entry_click2)
        self.entryPass.bind("<FocusOut>", self.on_focusout2)
        self.entryPass.config(fg="black")
        self.check = IntVar()
        self.showPass = Checkbutton(
            window,
            text="Tampilkan Password",
            fg="black",
            variable=self.check,
            command=self.open_password,
            height="1",
            width="18",
            font=("Raleway", 7, "normal"),
        ).place(x=335, y=464)

        self.btnlogin = Button(
            window,
            text="Register",
            bg="#2CC797",
            fg="black",
            width="10",
            font=("Raleway", 12, "bold"),
            relief="flat",
            command=self.register_user,
        ).place(x=342, y=490)

        self.btnCancel = Button(
            window,
            text="Cancel",
            bg="#C7C7D2",
            fg="black",
            width="10",
            font=("Raleway", 12, "bold"),
            relief="solid",
            command=self.main_screen,
        ).place(x=468, y=490)

    def on_entry_click(self, entry):
        if self.entryEmail.get() == "Masukan Email Anda...":
            self.entryEmail.delete(0, "end")
            self.entryEmail.insert(0, "")
            self.entryEmail.config(fg="black")

    def on_focusout(self, entry):
        if self.entryEmail.get() == "":
            self.entryEmail.insert(0, "Masukan Email Anda...")
            self.entryEmail.config(fg="black")

    def on_entry_click2(self, entry):
        if self.entryPass.get() == "Masukkan Password Anda...":
            self.entryPass.delete(0, "end")
            self.entryPass.insert(0, "")
            self.entryPass.config(fg="black")

    def on_focusout2(self, entry):
        if self.entryPass.get() == "":
            self.entryPass.insert(0, "Masukkan Password Anda...")
            self.entryPass.config(fg="black")

    def on_entry_click3(self, entry):
        if self.entryUserName.get() == "Masukkan Username Anda...":
            self.entryUserName.delete(0, "end")
            self.entryUserName.insert(0, "")
            self.entryUserName.config(fg="black")

    def on_focusout3(self, entry):
        if self.entryUserName.get() == "":
            self.entryUserName.insert(0, "Masukkan Username Anda...")
            self.entryUserName.config(fg="black")

    def register_user(self):
        get_name = self.entryUserName.get()
        get_email = self.entryEmail.get()
        get_password = self.entryPass.get()
        if get_name == "Masukan Username Anda...":
            msg.showerror(
                "Registrasi Gagal", "Username tidak boleh kosong", parent=self.gui
            )
            self.delete_uname()
        elif get_name == "":
            msg.showerror(
                "Registrasi Gagal", "Username tidak boleh kosong", parent=self.gui
            )
            self.delete_uname()
        elif get_email == "Masukkan Email Anda...":
            msg.showerror(
                "Registrasi Gagal", "Email tidak boleh kosong", parent=self.gui
            )
            self.delete_email()
        elif len(get_email) > 0 and len(get_email) <= 10:
            msg.showerror("Registrasi Gagal", "Email terlalu pendek", parent=self.gui)
            self.delete_email()
        elif get_email == "":
            msg.showerror(
                "Registrasi Gagal", "Email tidak boleh kosong", parent=self.gui
            )
            self.delete_email()
        elif "@gmail.com" not in get_email:
            msg.showerror(
                "Registrasi Gagal", "Harap sertakan domain @gmail.com", parent=self.gui
            )
            self.delete_email()
        elif " " in get_email:
            msg.showerror(
                "Registrasi Gagal",
                "Tidak boleh terdapat spasi dalam Email",
                parent=self.gui,
            )
            self.delete_email()
        elif get_password == "":
            msg.showerror(
                "Registrasi Gagal", "Password tidak boleh kosong!", parent=self.gui
            )
            self.delete_password()
        elif get_password == "Masukkan Password Anda...":
            msg.showerror(
                "Registrasi Gagal", "Password tidak boleh kosong!", parent=self.gui
            )
            self.delete_password()
        elif len(get_password) > 0 and len(get_password) <= 8:
            msg.showerror(
                "Registrasi Gagal", "Password terlalu pendek!", parent=self.gui
            )
            self.delete_password()
        else:
            file = open("userInfo.txt", "a")
            file.write("\n" + get_name + "," + get_email + "," + get_password)
            file.close()
            self.entryUserName.delete(0, END)
            self.entryEmail.delete(0, END)
            self.entryPass.delete(0, END)
            msg.showinfo(
                "Registrasi Berhasil",
                "Registrasi berhasil, silahkan login kembali pada halaman awal!",
                parent=self.gui,
            )
            self.main_screen()

    def do_login(self):
        get_useremail = self.entryEmail.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open("userInfo.txt", "r")

        for line in file:
            line = line.strip()
            if line:
                name, email, password = line.split(",")
                password = password.strip()
                if get_useremail == email and get_password == password:
                    sukses = True
                    break

        file.close()

        if sukses:
            msg.showinfo(
                "Login Berhasil",
                "Selamat Datang di Gacha48 %s" % (name),
                parent=self.gui,
            )
            self.gachascr()
            return
        elif get_useremail == "" or get_password == "":
            msg.showwarning(
                "Login Gagal", "Email atau Password tidak boleh kosong", parent=self.gui
            )
            self.entryEmail.focus_set()
        else:
            msg.showerror("Login Gagal", "Email atau Password salah!", parent=self.gui)
            self.delete_data()

    def temp_text(self):
        self.entryEmail.delete(0, END)

    def delete_data(self):
        self.entryEmail.delete(0, END)
        self.entryPass.delete(0, END)
        self.entryEmail.focus_set()

    def delete_uname(self):
        self.entryPass.focus_set()
        self.entryEmail.focus_set()
        self.entryUserName.delete(0, END)
        self.entryUserName.focus_set()

    def delete_email(self):
        self.entryEmail.delete(0, END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryEmail.focus_set()

    def delete_password(self):
        self.entryPass.delete(0, END)
        self.entryUserName.focus_set()
        self.entryEmail.focus_set()
        self.entryPass.focus_set()

    def open_password(self):
        Show = self.check.get()

        if Show == 1:
            self.entryPass["show"] = ""
        else:
            self.entryPass["show"] = "*"

    def gachascr(self):
        self.bg = ImageTk.PhotoImage(Image.open("background-01.png"))
        self.a_main = Label(window, image=self.bg)
        self.a_main.place(anchor="center", relx=0.5, rely=0.5)
        self.show_inventory_button()
        self.gachabtn = Button(
            text="Try Your Luck!",
            bg="white",
            fg="black",
            height="1",
            width="20",
            relief="flat",
            font=("Raleway", 20, "bold"),
            command=self.pull,
        )
        self.gachabtn.place(x=300, y=430)
        self.lgoutbtn = Button(
            text="Logout",
            bg="white",
            fg="black",
            height="1",
            width="16",
            relief="flat",
            font=("Raleway", 10, "bold"),
            command=self.logout,
        )
        self.lgoutbtn.place(x=800, y=10)
        self.video_label.destroy()

        gacha_count = self.get_gacha_count()
        total_gacha_label = Label(
            window,
            text=f"Total Gacha Saat Ini : {gacha_count}",
            font=("Raleway", 8, "bold"),
            bg="#C7C7D2",
            fg="black",
            relief="flat",
        )
        total_gacha_label.place(x=410, y=500)

        self.inventory_btn = Button(
            text="Inventory",
            bg="white",
            fg="black",
            height="1",
            width="16",
            relief="flat",
            font=("Raleway", 10, "bold"),
            command=self.open_inventory,
        )
        self.inventory_btn.place(x=800, y=50)

    def show_inventory_button(self):
        if not hasattr(self, "inventory_btn"):
            self.inventory_btn = Button(
                text="Inventory",
                bg="white",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.open_inventory,
            )
            self.inventory_btn.place(x=800, y=50)

    def open_inventory(self):
        inventory_window = Toplevel(self.gui)
        inventory_window.geometry("680x550")
        inventory_window.title("Inventory")
        inventory_window.resizable(False, False)
        inventory_label = Label(
            inventory_window,
            text="Your Photocard Inventory",
            font=("Raleway", 16, "bold"),
            bg="#F0F0F0",
            fg="black",
            relief="flat",
        )
        inventory_label.pack(pady=10)

        if len(self.inventory) == 0:
            no_card_label = Label(
                inventory_window,
                text="Belum ada photocard yang diperoleh",
                font=("Raleway", 12),
            )
            no_card_label.pack(pady=50)
        else:
            frame = Frame(inventory_window, bg="#F0F0F0")
            frame.pack(pady=5)

            num_columns = 4
            row_count = 0
            col_count = 0

            for card in self.inventory:
                card_image = ImageTk.PhotoImage(Image.open(card))
                card_label = Label(frame, image=card_image)
                card_label.image = card_image
                card_label.grid(row=row_count, column=col_count, padx=5, pady=5)

                col_count += 1
                if col_count == num_columns:
                    col_count = 0
                    row_count += 1

    def logout(self):
        self.gacha_count = 0
        self.main_screen()
        self.inventory.clear()
        self.open_inventory(clear=True)

    def get_gacha_count(self):
        return self.gacha_count

    def show_gacha_result(self):
        gacha_count = self.get_gacha_count()
        if self.gacha == [1]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Ci Shani!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [2]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Ci Gre!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [3]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Zee!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [4]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Christy!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [5]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Nona Freya!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [6]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Cepio!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [7]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Matcha!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [8]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Ngab Adel!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [9]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Teh Mpen!\nTotal Gacha: {gacha_count}",
            )
        elif self.gacha == [10]:
            msg.showinfo(
                "Selamatt!!",
                f"Anda mendapatkan Photocard Ashel!\nTotal Gacha: {gacha_count}",
            )

    def show_gacha_result_with_delay(self):
        timer = threading.Timer(6.0, self.show_gacha_result)
        timer.start()

    def pull(self):
        self.charlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.freq = 1, 1, 2, 4, 5, 5, 7, 7, 8, 9
        self.gacha = random.choices(self.charlist, self.freq)

        if self.gacha == [1]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_shani.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Shani.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [2]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_gracia.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Gracia.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [3]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_zee.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Zee.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [4]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_christy.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Christy.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [5]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_freya.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Freya.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [6]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_fiony.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Fiony.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [7]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_marsha.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Marsha.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [8]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_adel.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Adel.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [9]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_feni.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Feni.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()

        elif self.gacha == [10]:
            self.a_main.destroy()
            self.gachabtn.destroy()
            self.lgoutbtn.destroy()
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo(
                "resized_ashel.mp4", self.video_label, loop=0, size=(960, 540)
            )
            self.player.play()
            self.inventory.append("photocard-Ashel.png")

            self.backbtn = Button(
                text="Back",
                bg="pink",
                fg="black",
                height="1",
                width="16",
                relief="flat",
                font=("Raleway", 10, "bold"),
                command=self.gachascr,
            ).place(x=800, y=490)

            self.gacha_count += 1
            threading.Thread(target=self.show_gacha_result_with_delay).start()
            gacha_count = self.get_gacha_count()


def exit_program():
    window.destroy()
    sys.exit()


if __name__ == "__main__":
    global window
    window = tk.Tk()
    logo = PhotoImage(file="logo.png")
    window.iconphoto(True, logo)
    start = gacha48(window, "Gacha48 : JKT48 Custom Photocard")
    app = gacha48(window, "Gacha48 : JKT48 Custom Photocard")
    window.mainloop()
