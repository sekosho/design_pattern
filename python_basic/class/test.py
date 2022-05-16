kward = {"a": 1, "b": 3, "c": 4, "e": 5, "g": 6, "b": 2}
ward = {"a": 1, "b": 3, "c": 4, "g": 5, "a": 0}
unexpected_kwargs = set(kward) - set(ward)
print(unexpected_kwargs)
print(type(unexpected_kwargs))
