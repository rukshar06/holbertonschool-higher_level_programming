#!/usr/bin/env python3

class SwimMixin:
    """Mixin to add swimming capability to a creature."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying capability to a creature."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting behaviors from SwimMixin and FlyMixin.
    """

    def roar(self):
        print("The dragon roars!")
