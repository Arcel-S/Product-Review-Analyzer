from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from .meta import Base
import datetime

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))
    confidence = Column(Float)
    key_points = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'review_text': self.review_text,
            'sentiment': self.sentiment,
            'confidence': self.confidence,
            'key_points': self.key_points,
            'created_at': self.created_at.strftime('%Y-%m-%d') if self.created_at else None
        }