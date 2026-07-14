# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename
**What I did:** I looked up `save_to_watchlist`'s callsites using VS Code's `Find All References` and doubled check with search functionality. Then I renamed to function to `add_to_watchlist` and also traced the other references and renamed them as well.
**How I verified:** I checked with search functionality on `save_to_watchlist` again and found no match. Then, I started `FLASK_APP=app:create_app flask run` up with no compile error. I also added test cases for watchlist and ran `pytest tests/ -v` with all green. I called POST `/watchlist/1/add` to check the call still works.

## Comment 2 — Deduplication
**What I did:** I looked at `add_to_collection` and created a a new error `AlreadyInWatchlistError` to be raised when the film is found to exist in the user's watchlist already. This error is separated from the collection error to provide clear separation and clarity on collection vs watchlist being different.
**How I verified:** I started up the app with `FLASK_APP=app:create_app flask run` with no compile error, made the same POST call `/watchlist/1/add` with `{"film_id": "2"}` as the previous call and confirmed `services.watchlist_service.AlreadyInWatchlistError: Film '1' is already in this user's watchlist` is present in server log.

## Comment 3 — Missing test
**What I did:** I accidentally added the tests that cover the watchlist prior to the rename fix commit. I referenced tests in the existing `./tests/test_collection.py` for the code pattern and applied to all test cases in `watchlist_service.py`
**How I verified:** I ran `pytest tests/ -v` and confirmed tests passed with 100% with all new tests visibly added.

## Comment 4 — Default visibility
**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 5 — Sort order
**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->