from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(30))
    qtd_games = db.Column(db.Integer)
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))

    def __init__(self,name,year,price,status,qtd_games):
        self.name = name
        self.status = status
        self.qtd_games = qtd_games
        self.year = year
        self.price = price

    def __repr__(self):
        return 'Console {0}'.format(self.id)