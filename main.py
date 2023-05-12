from sqlalchemy import create_engine, MetaData, inspect

engine = create_engine("postgresql://admin:password@localhost:5432/admin", echo=True)
# print(engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

inspector = inspect(engine)
schemas = inspector.get_schema_names()
print(inspector.get_table_names())
# for schema in schemas:
#     print("schema: %s" % schema)
#     for table_name in inspector.get_table_names(schema=schema):
#         for column in inspector.get_columns(table_name, schema=schema):
#             print("Column: %s" % column)
# class Lake(Base):
#     __tablename__ = "lake
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     geom = Column(Geometry("POLYGON"))


# Lake.__table__.create(engine)
