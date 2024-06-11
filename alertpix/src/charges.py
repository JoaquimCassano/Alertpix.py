import requests
from .brcode import BrCODE
from .statics import BASEURL
class Charge():
    def __init__(self, link:str,  amount:int, comment:str=".", username:str=None,) -> None:
        """
        Args:x'
            link (str): Username da conta da twitch que IRÁ RECEBER
            comment (str): Mensagem que o usuário irá receber (OPCIONAL)
            username (str): Nome que o pagante será identificado (OPCIONAL)
            amount (int): Quantia que o usuário irá receber
        """
        if amount <= 100:
            raise ValueError("Amount must be greater than 100")
        self.link = link
        self.comment = comment
        self.username = username
        self.amount = amount

    def create(self):
        request  =  requests.post(
            url=f'{BASEURL}/create-charge',
            json={
                "link": self.link,
                "amount": self.amount,
                "comment": self.comment,
                "userName": self.username,
                "anonymous": True if self.username == None else False

            },
            headers={"content-type": "application/json"}
            
        )
        if request.status_code == 200:
            self.charge_id = request.json()['data']["id"]
            self.brcode = BrCODE(request.json()['data']["brCode"])   
            return self
        else:
            raise Exception(f'Request returned status {request.status_code} | Response: {request.text}')

    def check(self) -> bool:
        """
        Verifica se o pagamento foi concluído

        Retorna:
            bool: True se o pagamento foi concluído, False se não
        """
        request  =  requests.get(
            url=f'{BASEURL}/check-charge?id={self.charge_id}'
        )
        if request.status_code == 200:
            return False if request.json()["data"]["status"] == "pending" else True
        else:
            raise Exception(f'Request returned status {request.status_code} | Response: {request.text}')