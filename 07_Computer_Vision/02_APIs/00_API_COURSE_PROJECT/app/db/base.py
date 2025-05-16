# app/db/base.py

# app/db/base.py
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# app/db/models/user.py, qc_data.py …
# each model subclasses Base
