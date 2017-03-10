import memory, addresses, control, healer, pprint

class Client:
    def __init__(self):
        self.mem = memory.Memory()
        self.addr = addresses.Addresses()
        self.ctrl = control.Control(self.mem)

    def getWindowTitle(self):
        return self.mem.getWindowTitle(self.mem.CLIENT.hwnd)

    def percentage(self, part, whole):
        return 100 * float(part) / float(whole)

    def getEXP(self):
        return self.mem.readPtrInt(self.addr.exp)

    def getHP(self):
        return self.mem.readPtrShort(self.addr.hp)

    def getHPPC(self):
        return self.percentage(self.getHP(), self.getMaxHP())

    def getMaxHP(self):
        return self.mem.readPtrShort(self.addr.maxhp)

    def getMP(self):
        return self.mem.readPtrShort(self.addr.mp)

    def getMPPC(self):
        return self.percentage(self.getMP(), self.getMaxMP())

    def getMaxMP(self):
        return self.mem.readPtrShort(self.addr.maxmp)

    def getPosX(self):
        return self.mem.readPtrShort(self.addr.posx)

    def getPosY(self):
        return self.mem.readPtrShort(self.addr.posy)

    def getPosZ(self):
        return self.mem.readPtrShort(self.addr.posz)

    def getStatusCount(self):
        return self.mem.readIntDirect(self.mem.readPtrInt(self.addr.statusc) + 0xC)

    def getStatuses(self):
        statuses = [] # missing final value from statusc is 0xC
        adrNow = self.mem.readPtrInt(self.addr.statusc)
        if adrNow == -1:
            return None
        adrNow = adrNow + 0xC
        statusCount = self.mem.readIntDirect(adrNow)
        for i in range(1, statusCount.value + 1):
            adrItem = self.mem.readIntDirect(adrNow + (i * 4))
            adrItem = adrItem.value + 0xC
            adrItem = self.mem.readIntDirect(adrItem)
            item = self.mem.readString(adrItem.value + 0x10, 64)
            statuses.append(item)
        return statuses


    def sendText(self, text):
        self.ctrl.SendText(text)

    def sendKey(self, key):
        self.ctrl.SendKey(key)