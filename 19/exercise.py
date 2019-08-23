from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name=str, expire=datetime):
        self.expire = expire
    
    @property
    def expired(self):
        if self.expire > NOW:
            return False
        else:
            return True