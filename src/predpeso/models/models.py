from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from predpeso.db.base import Base

class UserModel(Base):
    __tablename__ = 'user'
    id: Mapped[str] = mapped_column(primary_key=True, unique= True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    profile_picture: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=False)

    farms: Mapped[list["FarmModel"]] = relationship("FarmModel", back_populates="user")

class FarmModel(Base):
    __tablename__ = 'farm'

    id: Mapped[str] = mapped_column(primary_key=True, unique= True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    animal_quantity: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=False)

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="farms")

    animals: Mapped[list["AnimalModel"]] = relationship("AnimalModel", back_populates="farm")

class AnimalModel(Base):
    __tablename__ = 'animal'

    id: Mapped[str] = mapped_column(primary_key=True, unique= True)
    name: Mapped[str] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    gender: Mapped[str] = mapped_column(nullable=False)
    health_condition: Mapped[str] = mapped_column(nullable=True)
    current_weight: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=False)

    farm_id: Mapped[str] = mapped_column(ForeignKey("farm.id"), nullable=False)
    farm: Mapped["FarmModel"] = relationship("FarmModel", back_populates="animals")

