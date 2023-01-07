import typing as t


class Mapping(dict):
    def invert(self: dict[t.Hashable, t.Union[t.Hashable, t.Sequence[t.Hashable]]]) -> dict[t.Hashable, t.Hashable]:
        inverted_dict = {}
        for key, vals in self.items():
            if isinstance(vals, t.Sequence) and not isinstance(vals, str):
                for val in vals:
                    inverted_dict[val] = key
            else:
                inverted_dict[vals] = key

        return inverted_dict
