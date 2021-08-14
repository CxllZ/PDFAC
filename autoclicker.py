import threading, pyautogui, tkinter, time
from tkinter import messagebox
from pynput.keyboard import Key, Listener

threads = []
thread_count = 10
stop_threads = False

pyautogui.FAILSAFE = True

def killThreads():
    global stop_threads
    stop_threads = True
    
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
        global timing_delay
        timing_delay = int(time_entry.get())
    except ValueError:
        messagebox.showerror("Time Error", "Enter Only Integer Not String!")
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
    startThreads(thread_count, threads)

def clicker():
    while True:
        selection = click_btn.get()
        if selection == 1:
            item = "Left Click On"
            pyautogui.leftClick()
        elif selection == 2:
            item = "Right Click On"
            pyautogui.rightClick()

        label.config(text=item)
        time.sleep(timing_delay)
        if stop_threads:
            break

def on_press(key):
    pass

def on_release(key):
    if key == Key.esc:
        killThreads()
        root.quit()
        print("Exiting")
        return False
    elif key == Key.f1:
        mainProgram()
        print("Started")
    elif key == Key.f2:
        resetThreads(thread_count, threads)
        killThreads()
        print("Paused")
    else:
        pass

def keylistener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def exit():
    killThreads()
    root.quit()
    print("Exiting")
    return False

root = tkinter.Tk()
root.title("PDFAC - Pretty Damn Fast Autoclicker")
root.geometry("400x250")
root.resizable(False, False)

click_btn = tkinter.IntVar()

LeftClickEntry = tkinter.Radiobutton(root, text="Left Click", padx = 20, variable=click_btn,  value=1)
LeftClickEntry.pack()

RightClickEntry = tkinter.Radiobutton(root, text="Right Click", padx = 30, variable=click_btn, value=2)
RightClickEntry.pack()

label = tkinter.Label(root)
label.pack()

w = tkinter.Label(root, text="Enter delay in seconds (0 for fast clicks, above 3 for afk clicks)")
w.pack()

time_entry = tkinter.Entry(root)
time_entry.pack()

t = tkinter.Label(root, text="Enter CPS (5 recommended for fast clicks)")
t.pack()

threads_entry = tkinter.Entry(root)
threads_entry.pack()

start_button = tkinter.Button(root, text="START     (F1)", command=mainProgram)
start_button.pack()

stop_button = tkinter.Button(root, text="PAUSE      (F2)", command=killThreads, padx=1)
stop_button.pack()

exit_button = tkinter.Button(root, text="EXIT       (ESC)", command=exit, padx=2)
exit_button.pack()

tg = threading.Thread(target=keylistener)
tg.start()
root.wm_attributes("-topmost", 1)
root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()
