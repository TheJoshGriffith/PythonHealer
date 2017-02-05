import ctypes, win32ui, win32gui, win32process, win32api, clientprocess, control


class Memory:
    def __init__(self):
        PROCESS_ALL_ACCESS = 0x1F0FFF
        self.rPM = ctypes.windll.kernel32.ReadProcessMemory
        self.wPM = ctypes.windll.kernel32.WriteProcessMemory
        self.CLIENT = self.getClientByConsole()
        self.HANDLE = win32api.OpenProcess(PROCESS_ALL_ACCESS, 0, self.CLIENT.pid[1])
        self.BASEADDRESSLIST = win32process.EnumProcessModulesEx(self.HANDLE.handle)
        for BA in self.BASEADDRESSLIST:
            if "Qt5Core.dll" in win32process.GetModuleFileNameEx(self.HANDLE.handle, BA):
                self.QT5CORE = BA
            elif "client.exe" in win32process.GetModuleFileNameEx(self.HANDLE.handle, BA):
                self.MAINMODULE = BA
        self.BASEADDRESS = self.BASEADDRESSLIST[0]

    def dump(self):
        print()
        print("HWND        : " + str(self.CLIENT.hwnd))
        print("PID         : " + str(self.CLIENT.pid))
        print("HANDLE      : " + str(self.HANDLE.handle))
        print("BASEADDRESS : " + str(self.BASEADDRESS))

    def getWindowTitle(self, hwid):
        return win32gui.GetWindowText(hwid)

    def getDefaultTibiaHandle(self):
        return self.gettibiahandle()[0].GetSafeHwnd()

    def getClientByConsole(self):
        clientList = self.gettibiaclients()
        iter = 0
        if len(clientList) == 1:
            return clientList[0]
        else:
            for Client in clientList:
                print(str(iter) + ": " + win32gui.GetWindowText(Client.hwnd))
                iter += 1
            res = input("Select a client: ")
            print("You selected client " + win32gui.GetWindowText(clientList[int(res)].hwnd))
            return clientList[int(res)]

    @staticmethod
    def gettibiaclients():
        clientList = []
        i = 0
        for Client in Memory.gettibiahandle():
            clientList.insert(i, clientprocess.ClientProcess(Client, win32gui.GetWindowText(Client), win32process.GetWindowThreadProcessId(Client)))
            i += 1
        return clientList


    @staticmethod
    def gettibiahandle():
        hwndList = []
        currentHwnd = win32ui.FindWindowEx(None, None, "Qt5QWindowOwnDCIcon", None).GetSafeHwnd()
        hwndList.insert(0, currentHwnd)
        i = 1
        while currentHwnd != None:
            try:
                currentHwnd = win32ui.FindWindowEx(None, currentHwnd, "Qt5QWindowOwnDCIcon", None).GetSafeHwnd()
                hwndList.insert(i, currentHwnd)
            except win32ui.error:
                currentHwnd = None
            i += 1
        return hwndList

    def readString(self, Address):
        data = b"wah"
        buff = ctypes.create_string_buffer(data, 32)
        self.rPM(self.HANDLE.handle, Address + self.BASEADDRESS, buff, 32, 0)
        val = ctypes.string_at(buff).decode("utf-8")
        return val

    def readIntDirect(self, Address):
        val = ctypes.c_long()
        buffersize = ctypes.sizeof(val)
        bytesread = ctypes.c_ulong(0)
        self.rPM(self.HANDLE.handle, Address, ctypes.byref(val), buffersize, ctypes.byref(bytesread))
        return val

    def readShortDirect(self, Address):
        val = ctypes.c_ushort()
        buffersize = ctypes.sizeof(val)
        bytesread = ctypes.c_ulong(0)
        self.rPM(self.HANDLE.handle, Address, ctypes.byref(val), buffersize, ctypes.byref(bytesread))
        #print(type(val.value))
        return val

    def readPtrInt(self, Address):
        data = ctypes.c_long(0)
        iter = 0
        for i in Address:
            if iter == 0:
                toread = ctypes.c_long(i + self.QT5CORE).value
                data = self.readIntDirect(toread)
                iter += 1
            elif iter == len(Address) - 1:
                toread = ctypes.c_long(data.value + i).value
                data = self.readIntDirect(toread)
                return data.value
            else:
                toread = ctypes.c_long(data.value + i).value
                data = self.readIntDirect(toread)
                iter += 1

    def readPtrShort(self, Address):
        data = ctypes.c_long(0)
        iter = 0
        for i in Address:
            if iter == 0:
                toread = ctypes.c_long(i + self.QT5CORE).value
                data = self.readIntDirect(toread)
                iter += 1
            elif iter == len(Address) - 1:
                res = ctypes.c_short(0)
                toread = ctypes.c_long(data.value + i).value
                res = self.readShortDirect(toread)
                return res.value
            else:
                toread = ctypes.c_long(data.value + i).value
                data = self.readIntDirect(toread)
                iter += 1