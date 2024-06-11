import qrcode

class BrCODE():

    def __init__(self, code:str):
        self.code = code
        
    def image(self):
        return qrcode.make(self.code)

    