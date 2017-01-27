import win32con, VKCodes

HEALRULE_SPELL = 0
HEALRULE_ITEM = 1

class HealRule:
    def __init__(self, minhp, maxhp, minmp, maxmp, hotkey, type = HEALRULE_SPELL, percent = False):
        self.minhp = minhp
        self.maxhp = maxhp
        self.minmp = minmp
        self.maxmp = maxmp
        self.hotkey = VKCodes.VK_CODE[hotkey]
        self.type = type
        self.percent = percent

    def ToCsv(self):
        return str(self.minhp) + "," +\
               str(self.maxhp) + "," +\
               str(self.minmp) + "," +\
               str(self.maxmp) + "," +\
               str("self.hotkey")