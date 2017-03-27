from IPython.display import display, Markdown

class Table(object):
    def __init__(self, columns):
        self.columns = columns
        self.max_lengths = [0] * len(columns)
        self.rows = []

    def __iadd__(self, v):
        if len(v) != len(self.columns):
            raise ValueError('Length of row must be %d' % len(self.columns))
        self.rows.append(v)

        for i, r in enumerate(v):
            l = len(str(r))
            if l > self.max_lengths[i]:
                self.max_lengths[i] = l
        return self

    def __str__(self):
        res = ""
        for i, col in enumerate(self.columns):
            res += '| ' + col.ljust(self.max_lengths[i]) + ' '
            if i == len(self.columns) - 1:
                res += '|'

        res += "\n"
        
        for i, col in enumerate(self.columns):
            res += '|' + self.max_lengths[i] * '-' + '--'
            if i == len(self.columns) - 1:
                res += '|'

        for row in self.rows:
            res += '\n'
            for i, col in enumerate(row):
                res += '| ' + str(col).rjust(self.max_lengths[i]) + ' '
                if i == len(self.columns) - 1:
                    res += '|'

        return res
    
    def jupyter(self):
        return display(Markdown(str(self)))

if __name__ == '__main__':
    table = Table(['a', 'b', 'c', 'd'])
    table += [1, 2, 30, 4]
    table += [1, "hello", 2, 40]
    print(table)
