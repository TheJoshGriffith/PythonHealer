import client, healrule, threading, time, pprint, random
from healrule import *

class Healer:
    def __init__(self, cl, healrules, delaymin = 300, delaymax = 500):
        self.cl = cl
        self.healrules = healrules
        self.delaymin = delaymin
        self.delaymax = delaymax
        self.healerThread = threading.Thread(target=self.runHeal)
        self.healerThread.start()
        self.itemThread = threading.Thread(target=self.runItemHeal)
        self.itemThread.start()

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
                if hr.type == HEALRULE_SPELL:
                    if hr.percent:
                        if hr.minhp < self.cl.getHPPC() <= hr.maxhp and hr.minmp < self.cl.getMPPC() <= hr.maxmp:
                            self.cl.ctrl.SendKey(hr.hotkey)
                            time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)
                    else:
                        if hr.minhp < self.cl.getHP() <= hr.maxhp and hr.minmp < self.cl.getMP() <= hr.maxmp:
                            self.cl.ctrl.SendKey(hr.hotkey)
                            time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)

    def runItemHeal(self):
        while(True):
            for hr in self.healrules:
                if hr.type == HEALRULE_ITEM:
                    if hr.percent:
                        if hr.minhp < self.cl.getHPPC() <= hr.maxhp and hr.minmp < self.cl.getMPPC() <= hr.maxmp:
                            self.cl.ctrl.SendKey(hr.hotkey)
                            time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)
                    else:
                        if hr.minhp < self.cl.getHP() <= hr.maxhp and hr.minmp < self.cl.getMP() <= hr.maxmp:
                            self.cl.ctrl.SendKey(hr.hotkey)
                            time.sleep(random.randint(self.delaymin, self.delaymax) / 1000)
