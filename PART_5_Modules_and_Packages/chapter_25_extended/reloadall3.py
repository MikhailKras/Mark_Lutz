"""
reloadall3.py: транзитивная перезагрузка вложенных модулей (явный стек)
"""
import types
from importlib import reload
from reloadall import status, tryreload, tester


def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()
        status(next)
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values() if isinstance(x, types.ModuleType) and x not in visited)


def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
