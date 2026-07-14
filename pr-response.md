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
**My position:** I decided to set the default visibility for a user's watchlist to be public, unless specified.
**Reasoning:** The platform is a community app for users to share films they have watched, their ratings, and what they want to watch. By setting default visibility to public, the user's watchlist is immediately discoverable by fellow CineLoggers. If the user prefers to keep the list private, they can manually set their list to private.
**Tradeoff acknowledged:** With this decision, the user would need to take an extra step to manually set watchlist's private visibility. This reduces privacy, but I believe that this would provide them a better discovery and sense of control rather than having dead-on-arrival discoverability if users never set their visibility to public if default is private.

## Comment 5 — Sort order
**My position:** I agree that most recently added film is more relevant than the title order.
**Reasoning:** The most recently added film indicates that it has recently caught the attention of the user, which also indicates the most up-to-date genre interests. The older added film could also be an outdated interest that the user once wanted to watch, but not anymore. If ordered by alphabetical order, it would be helpful with finding title based on the name, but it does not provide as much context catered to user's current interests. 
**Engagement with reviewer's point:** I can agree with the reviewer on this point that the most recently added film corresponds more to user's recent interests in film. This would help the user navigate through their list and find what to watch next faster and it is contextually more informative than providing a list ordered by name. The tradeoff is that date-added order makes it harder to scan a large list by name, but for a watchlist whose primary purpose is deciding what to watch next, recency is more useful than alphabetical position.

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->