class Group:
    def __init__(self, name=None, non_grouping=False):
        self.name = None
        self.data = ''
        if non_grouping:
            self.name = ''
            self.data = r'?:'
        elif name:
            self.name = name
            self.data = f'?P<{name}>'

    def add_pattern(self, pattern):
        self.data += pattern
        return self

    @property
    def pattern(self):
        return f'({self.data})'