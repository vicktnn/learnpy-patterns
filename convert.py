class Mapping:
    def __init__(self, mapping):
        self.mapping = mapping

    def __call__(self, value):
        for expected_list, result in self.mapping:
            if value in expected_list:
                return result
        raise ValueError('Value does not match the mapping.')