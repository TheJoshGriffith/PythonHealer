class ClientProcess:
    def __init__(self, client, hwnd, title, pid):
        self.client = client
        self.hwnd = hwnd
        self.title = title
        self.pid = pid
