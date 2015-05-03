from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class Source(Base):
    """
    This object represents a media source entity
    """
    __tablename__ = "syarc_source"
    id = Column(Integer, primary_key=True)
    org_name = Column(String)
    org_desc = Column(String, default="")

    def __init__(self, **fields):
        self.__dict__.update(fields)
