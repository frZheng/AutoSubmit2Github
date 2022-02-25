import os
import win32con
import win32gui
import win32api
import time
import pyautogui
import ctypes
from apscheduler.schedulers.blocking import BlockingScheduler

def move_to_top(name='SSTap Beta 1.0.9.7 - 享受游戏'):
    def get_all_hwnd(hwnd, mouse):
        if (win32gui.IsWindow(hwnd) and
                win32gui.IsWindowEnabled(hwnd) and
                win32gui.IsWindowVisible(hwnd)):
            hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})

    hwnd_map = {}
    win32gui.EnumWindows(get_all_hwnd, 0)
    h_list = []
    for h, t in hwnd_map.items():
        # print(h, t)
        if t:
            if t == name:
                # h 为想要放到最前面的窗口句柄
                # print(h)

                win32gui.BringWindowToTop(h)
                # shell = win32com.client.Dispatch("WScript.Shell")
                # shell.SendKeys('%')

                # 被其他窗口遮挡，调用后放到最前面
                win32gui.SetForegroundWindow(h)

                # 解决被最小化的情况
                win32gui.ShowWindow(h, win32con.SW_RESTORE)
                h_list.append(h)
    return h_list

def movePos(x, y):
    win32api.SetCursorPos((x, y))


# 模拟单击
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 模拟enter
def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


#import win32api
#import win32gui
#import win32con
#import win32process
#import time



def chmod_input():
    # import pyautogui
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2 ** 16 - 1)
    lid_hex = hex(lid)

    print(lid_hex)
    if lid_hex == '0x409':
        pass
        # print('当前的输入法状态是英文输入模式\n\n')
    elif lid_hex == '0x804':
        pyautogui.hotkey('ctrl', 'shiftleft') #不是英文输入则切换为英文
        # print('当前的输入法是中文输入模式\n\n')
    else:
        #pyautogui.hotkey('ctrl', 'shiftleft') #不是英文输入则切换为英文
        print('当前的输入法既不是英文输入也不是中文输入\n\n')
def submit_func():
    while True:
        try:
            submit_func_old()
            break
        except:
            print("error")
            pass
def submit_func_old():

    print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    hwnd_list = move_to_top("C:\Windows\system32\cmd.exe - submit.bat")
    
    # 关闭多余的窗口
    if(len(hwnd_list)):
        for i in hwnd_list:
            # win32gui.CloseWindow(i)
            win32gui.PostMessage(i, win32con.WM_CLOSE, 0, 0)
            print("close: ", i)
    else:
        print("None to close")
        
    os.system("start submit.bat")

    sleep_time = 5 # 休眠时间是为了防止github被墙了
    for i in range(sleep_time):
        print(sleep_time - i)
        time.sleep(1)
    hwnd_list = move_to_top("C:\Windows\system32\cmd.exe - submit.bat")
    if(len(hwnd_list)==1):
        hwnd =hwnd_list[0]
    else:
        print("窗口数量大于1")
        raise ValueError
        
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.MoveWindow(hwnd, 0, 0, 1000, 700, True)
    time.sleep(0.01)
    movePos(28, 147)
    time.sleep(0.1)
    click()
    time.sleep(0.1)
    password = "your pass word"
    print(password)
    pyautogui.typewrite(password)
    time.sleep(0.1)
    pyautogui.press("enter")
    print("finish once\n\n")
    
    # 使用完了之后关闭窗口
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    
    # time.sleep(1)
    # hwnd = move_to_top("C:\Windows\system32\cmd.exe - submit.bat")
    # win32gui.EnumWindows(close_process_by_hwnd, None)

if __name__ == "__main__":
    # chmod_input()
    # exit()
    code_version = 202111221400
    print(os.getcwd())
    print("file name: %s" % (__file__), ", code Version: ", code_version)

    # submit_func_old()
    scheduler = BlockingScheduler()

    # 多次防止链接不上github
    scheduler.add_job(func=submit_func, args=(), trigger='cron', hour=6, minute=0, misfire_grace_time=60 * 5)  #
    scheduler.add_job(func=submit_func, args=(), trigger='cron', hour=13, minute=0, misfire_grace_time=60 * 5)  #
    scheduler.add_job(func=submit_func, args=(), trigger='cron', hour=18, minute=0, misfire_grace_time=60 * 5)  #
    scheduler.add_job(func=submit_func, args=(),trigger='cron', hour=23, minute=45, misfire_grace_time=60 * 5)  #
    scheduler.add_job(func=submit_func, args=(),trigger='cron', hour=23, minute=50, misfire_grace_time=60 * 5)  #
    scheduler.start()
    # book_cmd()
