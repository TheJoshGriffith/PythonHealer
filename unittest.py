import client, win32con, healrule, healer, array

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

# Rules will be prioritised where first is most important
hrs = [healrule.HealRule(0, 40, 10, 100, "F3", True), healrule.HealRule(40, 70, 10, 100, "F2", True), healrule.HealRule(70, 90, 10, 100, "F1", True), healrule.HealRule(0, 100, 0, 80, "F4", True)]
he = healer.Healer(cl, hrs)