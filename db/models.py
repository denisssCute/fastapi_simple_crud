from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db.database import Base


class Colleagues(Base):

    __tablename__ = 'colleagues'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)

class Sales(Base):

    __tablename__ = 'sales'

    id_colleague = Column(Integer, ForeignKey("colleagues.id"), primary_key=True)
    department = Column(String, index=True)
    position = Column(String, index=True)
    is_admin = Column(Boolean, default=False)

