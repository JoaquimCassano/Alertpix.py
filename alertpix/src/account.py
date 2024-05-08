import requests, statics

class Account():

    def __init__(self, BearerToken:str):
        self.BearerToken = BearerToken  

    @property
    def wallet(self) -> tuple[int, int]:
        """
            Retorna uma tupla com o valor líquido e o bruto da carteira, respectivamente
        """
        response = requests.get(
            f'{statics.BASEURL}/account/wallet',
            headers={'Authorization': self.BearerToken}
        )
        if response.status_code == 200:
            data = response.json()
            return (data["amount"], data["grossAmount"])
        else:
            raise Exception(f'Request returned status {response.status_code} | Response: {response.text}')
    
    @property
    def notifications(self) -> list[statics.Notification]:
        response = requests.get(
            f'{statics.BASEURL}/account/notifications',
            headers={'Authorization': self.BearerToken}
        )
        if response.status_code == 200:
            return [statics.Notification(notification) for notification in response.json()['data']]
        else:
            raise Exception(f'Request returned status {response.status_code} | Response: {response.text}')