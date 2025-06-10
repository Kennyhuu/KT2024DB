
from sqlalchemy import select
from sqlalchemy.orm import query_expression

from interface import FractionCreate
from models import Operative, StrategicPloy, Equipment, FireFightPloy
from models.operatives_model import Fraction
from repository.config import connect_db

class PostgresFunction:

    @staticmethod
    def postgres_insert_operatives(data:FractionCreate):
        session = connect_db()
        try:
            fraction = Fraction(name=data.name)
            session.add(fraction)
            session.flush()

            new_id = fraction.id
            PostgresFunction.insert_operatives(data, new_id, session)
            session.commit()
            return new_id
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            raise
        finally:
            session.close()

    @staticmethod
    def insert_operatives(data, new_id, session):
        for oper in data.operatives:
            weapons_json = [w.to_dict() for w in oper.weapons]
            abiliy_json = [a.to_dict() for a in oper.abilities]
            operative = Operative(
                fraction_id=new_id,
                name=oper.name,
                type=oper.type,
                apl=oper.stats.APL,
                move=oper.stats.MOVE,
                save=oper.stats.SAVE,
                wounds=oper.stats.WOUNDS,
                weapons=weapons_json,
                abilities=abiliy_json
            )
            session.add(operative)
            session.flush()

    @staticmethod
    def postgres_insert_strategic(fk_id:int,  data: dict):
        first_key = next(iter(data))
        ploy_list = data[first_key]

        session = connect_db()
        for ploy in ploy_list:
            new_ploy = StrategicPloy(
                fractions_id=fk_id,
                name=ploy["name"],
                description=ploy["description"]
            )
            session.add(new_ploy)
        session.commit()
        session.close()

    @staticmethod
    def postgres_insert_firefight(fk_id: int, data: dict):
        first_key = next(iter(data))
        ploy_list = data[first_key]

        session = connect_db()
        for ploy in ploy_list:
            new_ploy = FireFightPloy(
                fractions_id=fk_id,
                name=ploy["name"],
                description=ploy["description"]
            )
            session.add(new_ploy)
        session.commit()
        session.close()

    @staticmethod
    def postgres_insert_equipment(fk_id: int, data: dict):
        first_key = next(iter(data))
        ploy_list = data[first_key]

        session = connect_db()
        for ploy in ploy_list:
            new_ploy = Equipment(
                fractions_id=fk_id,
                name=ploy["name"],
                description=ploy["description"]
            )
            session.add(new_ploy)
        session.commit()
        session.close()


    @staticmethod
    def postgres_fetch_fraction():
        try:
            session = connect_db()
            stmt = select(Fraction)
            query = session.execute(stmt) # .first() first with select
            return query
        except Exception as e:
            print(e)

    @staticmethod
    def post_get_operative(fraction_name):
        try:
            session = connect_db()
            stmt = select(Fraction).where(Fraction.name == fraction_name)
            query = session.execute(stmt).first()  # .first() first with select

            stmt2 = select(Operative).where(Operative.fraction_id == query[0].id)
            return session.execute(stmt2)

        except Exception as e:
            print(e)