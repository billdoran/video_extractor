from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class Video(Base):
    """
    This object represents a media source entity
    """
    __tablename__ = "syarc_source"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    retrieval_date = Column(DateTime)
    upload_date = Column(DateTime)
    location = Column(String)
    size = Column(String)
    source_id = Column(Integer)


    def __init__(self, **fields):
        self.__dict__.update(fields)
