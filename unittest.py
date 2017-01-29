import client, win32con, healrule, healer, array, pprint, memory
from healrule import *
import settingloader

cl = client.Client()

print("HP          : " + str(cl.getHP()))
print("MaxHP       : " + str(cl.getMaxHP()))
print("MP          : " + str(cl.getMP()))
print("MaxMP       : " + str(cl.getMaxMP()))
print("PosX        : " + str(cl.getPosX()))
print("PosY        : " + str(cl.getPosY()))
print("PosZ        : " + str(cl.getPosZ()))
print("EXP         : " + str(cl.getEXP()))

#cl.sendText("Test")
#cl.sendKey(win32con.VK_F1)

pprint.pprint(memory.Memory.gettibiaclients())

# Rules will be prioritised where first is most important
he = healer.Healer(cl, settingloader.LoadJsonHealRules("config.json"))