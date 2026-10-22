#!/usr/bin/env python3

class VerboseList(list):
    """A custom list class that prints notifications when modified."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        # Print the message before removing the item
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        # Retrieve the item before popping it so
        # we can display it in the message
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
