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

hrs = [healrule.HealRule(200, 3000, 20, 10000, "F1"), healrule.HealRule(400, 500, 20, 1000, "F2")]
he = healer.Healer(cl, hrs)