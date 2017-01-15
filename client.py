import memory, addresses, control, healer

class Client:
    def __init__(self):
        self.mem = memory.Memory()
        self.addr = addresses.Addresses()
        self.ctrl = control.Control(self.mem)

    def getEXP(self):
        return self.mem.ReadPtrInt(self.addr.exp)

    def getHP(self):
        return self.mem.ReadPtrShort(self.addr.hp)

    def getMaxHP(self):
        return self.mem.ReadPtrShort(self.addr.maxhp)

    def getMP(self):
        return self.mem.ReadPtrShort(self.addr.mp)

    def getMaxMP(self):
        return self.mem.ReadPtrShort(self.addr.maxmp)

    def getPosX(self):
        return self.mem.ReadPtrShort(self.addr.posx)

    def getPosY(self):
        return self.mem.ReadPtrShort(self.addr.posy)

    def getPosZ(self):
        return self.mem.ReadPtrShort(self.addr.posz)

    def sendText(self, text):
        self.ctrl.SendText(text)

    def sendKey(self, key):
        self.ctrl.SendKey(key)