
# Faulty decorator mimicking that of Django.
def cached_property(method):
    prop_name = f"{method.__name__}"

    def wrapped_func(self, *args, **kwargs):
        if not hasattr(self, prop_name):
            setattr(self, prop_name, method(self, *args, **kwargs))

        return getattr(self, prop_name)
    return property(wrapped_func)


class House:

    @property
    def color(self):
        print("Accessing color")
        return "blue"

    @cached_property
    def square_footage(self):
        print("Accessing square footage")
        return 1500


h = House()

print(h.color)

print(h.square_footage)
print(h.square_footage)
