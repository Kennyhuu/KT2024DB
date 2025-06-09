from pydantic import BaseModel


from typing import List, Optional, Dict, Any

class Stats(BaseModel):
    APL: int
    MOVE: str
    SAVE: str
    WOUNDS: int

class Weapon(BaseModel):
    name: str
    type: str
    attacks: int
    hit: str
    damage: str
    special_rules: Optional[List[str]] = None
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "attacks": self.attacks,
            "hit": self.hit,
            "damage": self.damage,
            "special_rules": self.special_rules,
        }

class Ability(BaseModel):
    name: str
    description: str
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

class Operative(BaseModel):
    name: str
    type: str
    stats: Stats
    weapons: List[Weapon]
    abilities: List[Ability]

class FractionCreate(BaseModel):
    name: str
    operatives: List[Operative]

class StrategicPloy(BaseModel):
    fractions_id: int
    name: str
    description: str

class FireFightPloy(BaseModel):
    fractions_id: int
    name: str
    description: str

class Equipment(BaseModel):
    fractions_id: int
    name: str
    description: str
