import win32con, VKCodes

class HealRule:
    def __init__(self, minhp, maxhp, minmp, maxmp, hotkey):
        self.minhp = minhp
        self.maxhp = maxhp
        self.minmp = minmp
        self.maxmp = maxmp
        self.hotkey = VKCodes.VK_CODE[hotkey]

    def ToCsv(self):
        return str(self.minhp) + "," +\
               str(self.maxhp) + "," +\
               str(self.minmp) + "," +\
               str(self.maxmp) + "," +\
               str("self.hotkey")