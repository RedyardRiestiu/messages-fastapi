from src.messenger.database import engine
from src.messenger.tables import Base

print("imported!")

Base.metadata.create_all(engine)

print("done!")