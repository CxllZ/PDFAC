import threading, pyautogui, tkinter, time, sys
from tkinter import messagebox

threads = []
thread_count = 10
stop_threads = False

pyautogui.FAILSAFE = True

def killThreads():
    global stop_threads
    stop_threads = True

def clicker():
    while True:
        pyautogui.click()
        if stop_threads:
            break
    
def createThreads(thread_count, threads):
    for i in range(thread_count):
        threads.append(threading.Thread(target=clicker))
        
def resetThreads(thread_count, threads):
    for i in range(thread_count):
            threads[i] = (threading.Thread(target=clicker))
           
def startThreads(thread_count, threads):
    global stop_threads
    stop_threads = False
    for i in range(thread_count):
        threads[i].start()

def mainProgram():
    try:
        global threads
        global thread_count
        thread_count = int(threads_entry.get())
        if (len(threads)) == 0:
            createThreads(thread_count, threads)    
        else:
            resetThreads(thread_count, threads)
    except ValueError:
        messagebox.showerror("CPS Error", "Enter Only Integer Not string!")
    try:
        time.sleep(int(time_entry.get()))
    except ValueError:
        messagebox.showerror("Time Error", "Enter Only Integer Not string!")
    startThreads(thread_count, threads)

root = tkinter.Tk()
root.geometry("300x200")
root.resizable(False, False)

w = tkinter.Label(root, text="Enter time in seconds to wait before clicking")
w.pack()

time_entry = tkinter.Entry(root)
time_entry.pack()

t = tkinter.Label(root, text="Enter CPS (30 may get serious)")
t.pack()

threads_entry = tkinter.Entry(root)
threads_entry.pack()

start_button = tkinter.Button(root, text="START?", command=mainProgram)
start_button.pack()

def close(event):
    sys.exit()

stop_button = tkinter.Button(root, text="STOP? (use esc key optional)", command=close, padx=1)
stop_button.pack()

root.bind('<Escape>', close)

root.mainloop()
