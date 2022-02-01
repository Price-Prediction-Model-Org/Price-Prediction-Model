def create_classes(db):
    class crypto_info(db.Model):
        __tablename__ = 'crypto_price'

        time = db.Column(db.Integer, primary_key=True)
        high = db.Column(db.Float)
        Currency = db.Column(db.String(64))
        Coin = db.Column(db.Float)
        low = db.Column(db.Float)
        open = db.Column(db.Float)
        volumefrom = db.Column(db.Float)
        volumeto = db.Column(db.Float)
        close = db.Column(db.Float)
        timestamp_date = db.Column(db.DateTime)
        timestamp_Year = db.Column(db.Integer)


        def __repr__(self):
            return '<crypto_info %r>' % (self.name)
    return crypto_info