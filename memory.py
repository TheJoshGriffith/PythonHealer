import ctypes, win32ui, win32gui, win32process, win32api


class Memory:
    def __init__(self):
        PROCESS_ALL_ACCESS = 0x1F0FFF
        self.rPM = ctypes.windll.kernel32.ReadProcessMemory
        self.wPM = ctypes.windll.kernel32.WriteProcessMemory
        self.HWND = self.GetTibiaHandle()
        self.PID = win32process.GetWindowThreadProcessId(self.HWND)[1]
        self.HANDLE = win32api.OpenProcess(PROCESS_ALL_ACCESS, 0, self.PID)
        self.BASEADDRESSLIST = win32process.EnumProcessModulesEx(self.HANDLE.handle)
        for BA in self.BASEADDRESSLIST:
            if "Qt5Core.dll" in win32process.GetModuleFileNameEx(self.HANDLE.handle, BA):
                self.QT5CORE = BA
            elif "client.exe" in win32process.GetModuleFileNameEx(self.HANDLE.handle, BA):
                self.MAINMODULE = BA
        self.BASEADDRESS = self.BASEADDRESSLIST[0]

    def Dump(self):
        print()
        print("HWND        : " + str(self.HWND))
        print("PID         : " + str(self.PID))
        print("HANDLE      : " + str(self.HANDLE.handle))
        print("BASEADDRESS : " + str(self.BASEADDRESS))

    def GetTibiaHandle(self):
        hwnd = win32ui.FindWindowEx(None, None, "Qt5QWindowOwnDCIcon", None).GetSafeHwnd()
        while True:
            if "Tibia" in win32gui.GetWindowText(hwnd):
                return hwnd
            hwnd = win32ui.FindWindowEx(None, hwnd, "Qt5QWindowOwnDCIcon", None).GetSafeHwnd()

    def ReadString(self, Address):
        data = b"wah"
        buff = ctypes.create_string_buffer(data, 32)
        self.rPM(self.HANDLE.handle, Address + self.BASEADDRESS, buff, 32, 0)
        val = ctypes.string_at(buff).decode("utf-8")
        return val

    def ReadIntDirect(self, Address):
        val = ctypes.c_long()
        buffersize = ctypes.sizeof(val)
        bytesread = ctypes.c_ulong(0)
        self.rPM(self.HANDLE.handle, Address, ctypes.byref(val), buffersize, ctypes.byref(bytesread))
        return val

    def ReadShortDirect(self, Address):
        val = ctypes.c_short()
        buffersize = ctypes.sizeof(val)
        bytesread = ctypes.c_ulong(0)
        self.rPM(self.HANDLE.handle, Address, ctypes.byref(val), buffersize, ctypes.byref(bytesread))
        return val

    def ReadPtrInt(self, Address):
        data = ctypes.c_long(0)
        iter = 0
        for i in Address:
            if iter == 0:
                toread = ctypes.c_long(i + self.QT5CORE).value
                data = self.ReadIntDirect(toread)
                iter += 1
            elif iter == len(Address) - 1:
                toread = ctypes.c_long(data.value + i).value
                data = self.ReadIntDirect(toread)
                return data.value
            else:
                toread = ctypes.c_long(data.value + i).value
                data = self.ReadIntDirect(toread)
                iter += 1

    def ReadPtrShort(self, Address):
        data = ctypes.c_long(0)
        iter = 0
        for i in Address:
            if iter == 0:
                toread = ctypes.c_long(i + self.QT5CORE).value
                data = self.ReadIntDirect(toread)
                iter += 1
            elif iter == len(Address) - 1:
                toread = ctypes.c_long(data.value + i).value
                data = self.ReadShortDirect(toread)
                return data.value
            else:
                toread = ctypes.c_long(data.value + i).value
                data = self.ReadIntDirect(toread)
                iter += 1