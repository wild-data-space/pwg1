from App import app, CreateSession, get_password_hash, verify_password, oauth2_scheme, ALGORITHM, SECRET_KEY
from App import models as M
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from pydantic import BaseModel
from typing import Optional
@app.post('/add_user')
def add_user(fname:str, lname:str, email:str, password:str, team:int, session : Session = Depends(CreateSession)):
    db_user = session.query(M.User).filter_by(email = email).first()
    if db_user:
        raise HTTPException(400, 'Email already used')
    new_user = M.User(
        fname = fname,
        lname = lname,
        email = email,
        password = get_password_hash(password),
        team_id = team
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.post('/add_team')
def add_team(name:str, session :Session=Depends(CreateSession)):
    team = M.Team(name = name)
    session.add(team)
    session.commit()
    session.refresh(team)
    return team

class TokenData(BaseModel):
    email :Optional[str] = None

def get_current_user(token: str = Depends(oauth2_scheme), session:Session = Depends(CreateSession)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = session.query(M.User).filter_by(email = email).first()
    if user is None:
        raise credentials_exception
    return user


@app.post('/tasks')
def add_task(title:str, description:str, assignee:int, session:Session = Depends(CreateSession), current_user :M.User = Depends(get_current_user)):
    task = M.Task(title = title, description = description, assignee_id = assignee)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task