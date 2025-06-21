import tkinter as tk
import threading
import time

class AlertPy:
    @staticmethod
    def chce(message, button="OK"):
        """Показать окно с сообщением и одной кнопкой."""
        root = tk.Tk()
        root.title("AlertPy")
        root.geometry("300x120")
        root.resizable(False, False)

        label = tk.Label(root, text=message, padx=20, pady=20)
        label.pack()

        def close():
            root.destroy()

        btn = tk.Button(root, text=button, width=10, command=close)
        btn.pack(pady=10)

        root.mainloop()

    @staticmethod
    def print(msg):
        """Выводит сообщение в консоль."""
        print(msg)

    @staticmethod
    def loadg(intrvl=0.5, smbol='.', limit=10):
        """Показывает индикатор загрузки с указанным символом и интервалом."""

        def loader():
            count = 0
            while count < limit:
                print(smbol, end='', flush=True)
                time.sleep(intrvl)
                count += 1
            print()  # перевод строки после окончания

        t = threading.Thread(target=loader)
        t.start()
        t.join()