import client, healrule, threading, time, pprint, random

class Healer:
    def __init__(self, cl, healrules, delaymin = 500, delaymax = 600):
        self.cl = cl
        self.healrules = healrules
        self.healerThread = threading.Thread(target=self.runHeal)
        self.healerThread.start()
        self.delaymin = delaymin
        self.delaymax = delaymax

    def stop(self):
        self.healerThread.stop()

    def addHealRule(self, healrule):
        self.healrules.insert(healrule)

    def removeHealRule(self, healrule):
        for hr in self.healrules:
            if hr == healrule:
                self.healrules.remove(healrule)

    def replaceHealRule(self, oldhealrule, newhealrule):
        for hr in self.healrules:
            if hr == oldhealrule:
                hr = newhealrule

    def runHeal(self):
        while(True):
            for hr in self.healrules:
                if hr.percent:
                    if hr.minhp < self.cl.getHPPC() <= hr.maxhp and hr.minmp < self.cl.getMPPC() <= hr.maxmp:
                        self.cl.ctrl.SendKey(hr.hotkey)
                        time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)
                else:
                    if hr.minhp < self.cl.getHP() <= hr.maxhp and hr.minmp < self.cl.getMP() <= hr.maxmp:
                        self.cl.ctrl.SendKey(hr.hotkey)
                        time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)
