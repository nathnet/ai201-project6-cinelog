"""
seed.py — CineLog

Populates the database with realistic test data.
Run with: py seed.py

This script creates:
- 4 users
- 10 films across 5 genres
- Collection entries (films already watched, some with ratings)
- Watchlist entries (films saved to watch later, mix of public/private)
"""

from datetime import datetime, timedelta, timezone
from app import create_app, db
from models import User, Film, CollectionEntry, WatchlistEntry


def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        now = datetime.now(timezone.utc)

        # --- Users ---
        users = [
            User(username="alice",  email="alice@example.com"),
            User(username="bob",    email="bob@example.com"),
            User(username="cara",   email="cara@example.com"),
            User(username="daniel", email="daniel@example.com"),
        ]
        db.session.add_all(users)
        db.session.flush()

        # --- Films ---
        films = [
            Film(title="Alien",           year=1979, director="Ridley Scott",      genre="Horror"),
            Film(title="Arrival",         year=2016, director="Denis Villeneuve",  genre="Sci-Fi"),
            Film(title="Blade Runner",    year=1982, director="Ridley Scott",      genre="Sci-Fi"),
            Film(title="Clueless",        year=1995, director="Amy Heckerling",    genre="Comedy"),
            Film(title="Hereditary",      year=2018, director="Ari Aster",         genre="Horror"),
            Film(title="Memento",         year=2000, director="Christopher Nolan", genre="Thriller"),
            Film(title="Paddington 2",    year=2017, director="Paul King",         genre="Comedy"),
            Film(title="Parasite",        year=2019, director="Bong Joon-ho",      genre="Thriller"),
            Film(title="Spirited Away",   year=2001, director="Hayao Miyazaki",    genre="Animation"),
            Film(title="Zootopia",        year=2016, director="Byron Howard",      genre="Animation"),
        ]
        db.session.add_all(films)
        db.session.flush()

        # --- Collection entries (already watched) ---
        collection_data = [
            # alice: watched several films, rated most of them
            (users[0], films[0], 5, now - timedelta(days=30)),   # Alien
            (users[0], films[2], 4, now - timedelta(days=20)),   # Blade Runner
            (users[0], films[6], 5, now - timedelta(days=10)),   # Paddington 2
            (users[0], films[7], 4, now - timedelta(days=3)),    # Parasite
            # bob: light watcher, one unrated
            (users[1], films[1], 3, now - timedelta(days=14)),   # Arrival
            (users[1], films[5], None, now - timedelta(days=2)), # Memento (unrated)
            # cara: animation fan
            (users[2], films[8], 5, now - timedelta(days=60)),   # Spirited Away
            (users[2], films[9], 4, now - timedelta(days=45)),   # Zootopia
            (users[2], films[6], 5, now - timedelta(days=7)),    # Paddington 2
            # daniel: horror fan
            (users[3], films[0], 4, now - timedelta(days=90)),   # Alien
            (users[3], films[4], 5, now - timedelta(days=5)),    # Hereditary
        ]
        for user, film, rating, date_added in collection_data:
            db.session.add(CollectionEntry(
                user_id=user.id,
                film_id=film.id,
                rating=rating,
                date_added=date_added,
            ))

        # --- Watchlist entries (saved to watch later) ---
        watchlist_data = [
            # alice: wants to watch horror and thriller
            (users[0], films[4], True,  now - timedelta(days=5)),    # Hereditary
            (users[0], films[5], True,  now - timedelta(days=2)),    # Memento
            # bob: curious about animation
            (users[1], films[8], True,  now - timedelta(days=8)),    # Spirited Away
            (users[1], films[9], False, now - timedelta(days=1)),    # Zootopia (private)
            # cara: wants to explore sci-fi
            (users[2], films[1], True,  now - timedelta(days=3)),    # Arrival
            (users[2], films[2], False, now - timedelta(days=1)),    # Blade Runner (private)
            # daniel: saved a comedy
            (users[3], films[6], True,  now - timedelta(days=10)),   # Paddington 2
        ]
        for user, film, public, date_added in watchlist_data:
            db.session.add(WatchlistEntry(
                user_id=user.id,
                film_id=film.id,
                public=public,
                date_added=date_added,
            ))

        db.session.commit()

        print("Seeded users:")
        for u in users:
            print(f"  {u.id}  {u.username}")

        print("\nSeeded films:")
        for f in films:
            print(f"  {f.id:>3}  {f.title}  ({f.genre})")

        print(f"\nSeeded {len(collection_data)} collection entries")
        print(f"Seeded {len(watchlist_data)} watchlist entries")


if __name__ == "__main__":
    seed()
