from App import Base, get_password_hash
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Team(Base):
    __tablename__ = 'teams'
    id = Column (Integer, primary_key= True)
    name = Column (String(20), nullable=False)
    creation_date = Column(DateTime, default= datetime.utcnow)
    users = relationship('User', back_populates='team')

class User(Base):
    __tablename__ = 'users'
    id = Column (Integer, primary_key= True)
    fname = Column (String(20), nullable=False)
    lname = Column(String(20), nullable = False)
    email = Column (String (50), nullable=False, unique= True)
    password = Column(String (50), nullable= False)
    join_date = Column(DateTime, default= datetime.utcnow)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='users')
    is_active = Column(Boolean, default = True)
    role = Column(String, default= 'Member')
    assigned_tasks = relationship('Task', back_populates='assignee')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column (Integer, primary_key= True)
    title = Column (String(20), nullable=False)
    description = Column (String, nullable = False)
    assignment_date = Column(DateTime, default= datetime.utcnow)
    assignee_id = Column(Integer, ForeignKey('users.id'))
    assignee = relationship('User', back_populates='assigned_tasks')


