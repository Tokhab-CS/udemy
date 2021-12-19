class Code:
    def __init__(self, var, value):
        self.value = value
        self.var = var

    def __str__(self):
        return f'self.{self.var} = {self.value}'


class Class:
    def __init__(self, name):
        self.name = name
        self.code = []

    def __str__(self):
        lines = [f'class {self.name}:']
        if not self.code:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for i in self.code:
                lines.append(f'    {i}')
        return '\n'.join(lines)

    @staticmethod
    def creat(name):
        return CodeBuilder(name)


class CodeBuilder:
    def __init__(self, root_name):
        self.__root = Class(root_name)

    def add_field(self, var, value):
        self.__root.code.append(
            Code(var, value)
        )
        return self

    def clear(self):
        self.__root.code = []

    def __str__(self):
        return str(self.__root)

if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', 39)
    print(cb)
    cb1 = Class.creat('Company')
    print(cb1)
    cb.add_field('company', 'Samsung')
    print(cb)
    cb.clear()
    print(cb)
