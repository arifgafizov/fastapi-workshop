from workshop.database import engine
from workshop.database import Base


Base.metadata.create_all(engine)
