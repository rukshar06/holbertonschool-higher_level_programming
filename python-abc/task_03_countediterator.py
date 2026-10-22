#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterator):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterator)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item, increment the counter, and handle StopIteration."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Return the total number of items fetched so far."""
        return self.counter
