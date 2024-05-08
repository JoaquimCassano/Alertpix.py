MINIMUM_VALUE = 100
BASEURL = "https://alertpix.fly.dev"


class Notification:
    def __init__(self, json:dict):
        self.json = json
        self.type = json["type"]
        self.message = json["message"]
        self.seen:bool = json["seen"]
        self.createdAt:int = json["createdAt"]
        if json.get('metadata'):
            class Metadata:
                def __init__(self, json:dict):
                    self.amount = json['metadata']['amount']
                    self.grossAmount = json['metadata']['grossAmount']
                    self.audio:bool = json['metadata']['audio']
                    self.comment = json['metadata']['comment']
                    self.username = json['metadata']['userName']

            self.metadata = Metadata(json)

        return