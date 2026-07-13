# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename
**What I did:** I looked up `save_to_watchlist`'s callsites using VS Code's `Find All References` and doubled check with search functionality. Then I renamed to function to `add_to_watchlist` and also traced the other references and renamed them as well.
**How I verified:** I checked with search functionality on `save_to_watchlist` again and found no match. Then, I started `FLASK_APP=app:create_app flask run` up with no compile error. I also added test cases for watchlist and ran `pytest tests/ -v` with all green. I called POST `/watchlist/1/add` to check the call still works.

## Comment 2 — Deduplication
**What I did:**
**How I verified:**

## Comment 3 — Missing test
**What I did:**
**How I verified:**

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