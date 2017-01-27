import ctypes, win32ui, win32gui, win32process, win32api, clientprocess


class Memory:
    def __init__(self):
        PROCESS_ALL_ACCESS = 0x1F0FFF
        self.rPM = ctypes.windll.kernel32.ReadProcessMemory
        self.wPM = ctypes.windll.kernel32.WriteProcessMemory
        self.HWND = self.GetClientByConsole()
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

    def GetDefaultTibiaHandle(self):
        return self.gettibiahandle()[0].GetSafeHwnd()

    def GetClientByConsole(self):
        clientList = self.gettibiaclients()
        iter = 0
        for Client in clientList:
            print(str(iter) + ": " + win32gui.GetWindowText(Client.hwnd))
            iter += 1
        res = input("Select a client: ")
        print("You selected client " + win32gui.GetWindowText(clientList[int(res)].hwnd))
        return clientList[int(res)].client

    @staticmethod
    def gettibiaclients():
        clientList = []
        i = 0
        for Client in Memory.gettibiahandle():
            clientList.insert(i, clientprocess.ClientProcess(Client, Client, win32gui.GetWindowText(Client), win32process.GetWindowThreadProcessId(Client)))
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
        val = ctypes.c_ushort()
        buffersize = ctypes.sizeof(val)
        bytesread = ctypes.c_ulong(0)
        self.rPM(self.HANDLE.handle, Address, ctypes.byref(val), buffersize, ctypes.byref(bytesread))
        #print(type(val.value))
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
                res = ctypes.c_short(0)
                toread = ctypes.c_long(data.value + i).value
                res = self.ReadShortDirect(toread)
                return res.value
            else:
                toread = ctypes.c_long(data.value + i).value
                data = self.ReadIntDirect(toread)
                iter += 1