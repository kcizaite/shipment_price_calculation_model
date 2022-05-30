from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///shipment_price_data.db")
Base = declarative_base()


class Shipments(Base):
    __tablename__ = "Shipment_price_data"
    ID = Column(Integer, primary_key=True)
    supplier = Column("Supplier", String)
    size = Column("Size", String)
    price = Column("Price", Float)

    def __init__(self, supplier, size, price):
        self.supplier = supplier
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.ID} {self.supplier} {self.size} {self.price}"


Base.metadata.create_all(engine)
