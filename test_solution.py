import pytest
import solution

def test_one():
    inputs=iter(['1', '0467123456'])
    output=10
    class _s():
        o=''
    def p(o): print(o);_s.o=o
    solution.input = lambda:next(inputs)
    solution.print = p
    solution.run()
    assert _s.o is output

def test_two():
    inputs=iter(['2','0123456789','1123456789'])
    output=20
    class _s():
        o=''
    def p(o): print(o);_s.o=o
    solution.input = lambda:next(inputs)
    solution.print = p
    solution.run()
    assert _s.o is output

def test_three():
    inputs=iter(['2','0123456789','0123'])
    output=10
    class _s():
        o=''
    def p(o): print(o);_s.o=o
    solution.input = lambda:next(inputs)
    solution.print = p
    solution.run()
    assert _s.o is output

def test_four():
    inputs=iter(['5','0412578440','0412199803','0468892011','112','15'])
    output=28
    class _s():
        o=''
    def p(o): print(o);_s.o=o
    solution.input = lambda:next(inputs)
    solution.print = p
    solution.run()
    assert _s.o is output