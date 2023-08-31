#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Game  # Import the Base and Game classes

if __name__ == '__main__':
    fake = Faker()

    # Connect to the database
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear old data from the games table
    session.query(Game).delete()
    session.commit()

    # Add new data using Faker
    print("Seeding games...")
    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for _ in range(50)
    ]

    session.add_all(games)
    session.commit()

    # Count the number of records
    game_count = session.query(Game).count()
    print(f"Total games seeded: {game_count}")

    # Print the first and last records
    first_game = session.query(Game).first()
    last_game = session.query(Game).order_by(Game.id.desc()).first()
    print(f"First game: {first_game}")
    print(f"Last game: {last_game}")
