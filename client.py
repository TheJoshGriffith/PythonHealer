import memory, addresses, control, healer

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
        return self.mem.readPtrInt(self.addr.statusc)

    def getStatuses(self):
        statusCount = self.getStatusCount()
        if statusCount == 0:
            return None
        statuses = []
        currentStatus = self.addr.statuss
        currentStatus.append(self.mem.readPtrInt(currentStatus))
        for i in range(0, statusCount):
            statuses[i] = self.mem.readPtrInt(self.addr.statuss)

    def sendText(self, text):
        self.ctrl.SendText(text)

    def sendKey(self, key):
        self.ctrl.SendKey(key)