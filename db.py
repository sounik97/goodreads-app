from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


DATABASE_URL = 'postgres://vtxfxgdjyhapnc:6c42ff36dc32ef50a4e33bde584964bd9735a0284addefaec38b2f724b844485@ec2-34-225-82-212.compute-1.amazonaws.com:5432/dadhl1lseoo0fe'

engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))