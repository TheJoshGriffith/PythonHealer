import win32api, win32con, memory, time

class Control:
	def __init__(self, mem):
		self.mem = mem

	def SendText(self, key):
		for k in key:
			if k == "\n":
				win32api.PostMessage(self.mem.CLIENT.hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
				win32api.PostMessage(self.mem.CLIENT.hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
			else:
				win32api.PostMessage(self.mem.CLIENT.hwnd, win32con.WM_CHAR, ord(k), 0)

	def SendKey(self, key):
		win32api.PostMessage(self.mem.CLIENT.hwnd, win32con.WM_KEYDOWN, key, 0x03B0001)
		time.sleep(1)
		win32api.PostMessage(self.mem.CLIENT.hwnd, win32con.WM_KEYUP, key, 0xC03B0001)