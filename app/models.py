from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TradeData(db.Model):
    __tablename__ = 'trade_data'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    open_price = db.Column(db.Float, nullable=False)
    high_price = db.Column(db.Float, nullable=False)
    low_price = db.Column(db.Float, nullable=False)
    close_price = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<TradeData {self.symbol} {self.timestamp}>'

class TradingSignal(db.Model):
    __tablename__ = 'trading_signal'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    signal_type = db.Column(db.String(10), nullable=False)  # 'buy' or 'sell'
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<TradingSignal {self.symbol} {self.signal_type} {self.timestamp}>'
