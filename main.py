import tkinter as tk
from tkinter import messagebox
import datetime

class TimeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Waktu dan Tugas")
        self.tasks = []

        # Buat frame untuk header
        self.header_frame = tk.Frame(self.root, bg="#3498db")
        self.header_frame.pack(fill="x")

        # Buat label untuk header
        self.header_label = tk.Label(self.header_frame, text="Aplikasi Manajemen Waktu dan Tugas", font=("Arial", 18), bg="#3498db", fg="#ffffff")
        self.header_label.pack(pady=20)

        # Buat frame untuk input tugas
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=20)

        # Buat label dan entry untuk input tugas
        self.task_label = tk.Label(self.input_frame, text="Tugas:", font=("Arial", 14))
        self.task_label.pack(side=tk.LEFT)
        self.task_entry = tk.Entry(self.input_frame, width=50, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT)

        # Buat label dan entry untuk input waktu
        self.time_label = tk.Label(self.input_frame, text="Waktu (HH:MM):", font=("Arial", 14))
        self.time_label.pack(side=tk.LEFT)
        self.time_entry = tk.Entry(self.input_frame, width=10, font=("Arial", 14))
        self.time_entry.pack(side=tk.LEFT)

        # Buat tombol untuk menambahkan tugas
        self.add_button = tk.Button(self.input_frame, text="Tambah", command=self.add_task, font=("Arial", 14), bg="#2ecc71", fg="#ffffff")
        self.add_button.pack(side=tk.LEFT, padx=10)

        # Buat frame untuk daftar tugas
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=20)

        # Buat tombol untuk menampilkan tugas yang harus dilakukan hari ini
        self.today_button = tk.Button(self.root, text="Tugas Hari Ini", command=self.show_today_tasks, font=("Arial", 14), bg="#f1c40f", fg="#ffffff")
        self.today_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        time = self.time_entry.get()
        if task and time:
            try:
                datetime.datetime.strptime(time, "%H:%M")
                self.tasks.append((task, time))
                self.display_tasks()
                self.task_entry.delete(0, tk.END)
                self.time_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Format waktu salah. Gunakan format HH:MM.")

    def display_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, (task, time) in enumerate(self.tasks):
            task_frame = tk.Frame(self.task_frame, bg="#ecf0f1")
            task_frame.pack(fill="x", pady=5)

            task_label = tk.Label(task_frame, text=f"{task} - {time}", font=("Arial", 14), bg="#ecf0f1")
            task_label.pack(side=tk.LEFT)

            delete_button = tk.Button(task_frame, text="Hapus", command=lambda i=i: self.delete_task(i), font=("Arial", 12), bg="#e74c3c", fg="#ffffff")
            delete_button.pack(side=tk.RIGHT, padx=10)

    def delete_task(self, index):
        del self.tasks[index]
        self.display_tasks()

    def show_today_tasks(self):
        today = datetime.datetime.now().strftime("%H:%M")
        today_tasks = [(task, time) for task, time in self.tasks if time <= today]
        messagebox.showinfo("Tugas Hari Ini", "\n".join([f"{task} - {time}" for task, time in today_tasks]))

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeManagementApp(root)
    root.mainloop()