from model_state import Base, State
from sqlalchemy.orm import sessionmaker

query = session.query(State.id, State.name)

result = query().all()