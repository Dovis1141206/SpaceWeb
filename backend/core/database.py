# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chat.db")

# SQLite일 경우 필요 (Thread 오류 방지)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM Base 클래스
Base = declarative_base()

# DB 세션 dependency (FastAPI 사용 시)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ⚡ 자동 테이블 생성 함수
def init_db():
    import app.models  # Base에 등록된 모델 불러오기
    Base.metadata.create_all(bind=engine)




# class MySQLCharsetMixin:
#     """ MySQL의 기본 charset을 설정하는 Mixin 클래스 """

#     @declared_attr.directive
#     def __table_args__(cls):
#         return {'mysql_charset': DBConnect().charset}