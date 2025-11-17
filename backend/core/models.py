# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

# from core.database import DBConnect, MySQLCharsetMixin
# Base = declarative_base(cls=MySQLCharsetMixin)

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(10), nullable=False)     # 'user' 또는 'assistant'
    message = Column(Text, nullable=False)        # 메시지 내용
    created_at = Column(DateTime(timezone=True), server_default=func.now())
