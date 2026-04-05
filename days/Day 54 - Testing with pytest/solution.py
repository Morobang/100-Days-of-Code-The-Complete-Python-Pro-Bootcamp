# Day 54 — Testing with pytest — SOLUTIONS
import pytest
from unittest.mock import patch, MagicMock

class Stack:
    def __init__(self): self._data=[]
    def push(self,x): self._data.append(x)
    def pop(self):
        if not self._data: raise IndexError('empty')
        return self._data.pop()
    def peek(self): return self._data[-1] if self._data else None
    def is_empty(self): return not self._data
    def size(self): return len(self._data)

def test_push(): s=Stack(); s.push(1); assert s.size()==1
def test_pop(): s=Stack(); s.push(5); assert s.pop()==5
def test_pop_empty_raises():
    with pytest.raises(IndexError): Stack().pop()
def test_peek(): s=Stack(); s.push(3); s.push(7); assert s.peek()==7; assert s.size()==2
def test_is_empty_new(): assert Stack().is_empty()
def test_is_empty_after_push(): s=Stack(); s.push(1); assert not s.is_empty()
def test_size(): s=Stack(); s.push(1);s.push(2);s.push(3); assert s.size()==3
def test_lifo(): s=Stack(); s.push(1);s.push(2);s.push(3); assert [s.pop() for _ in range(3)]==[3,2,1]

def fizzbuzz(n):
    if n%15==0: return 'FizzBuzz'
    if n%3==0: return 'Fizz'
    if n%5==0: return 'Buzz'
    return str(n)

@pytest.mark.parametrize('n,expected',[
    (1,'1'),(2,'2'),(3,'Fizz'),(5,'Buzz'),(15,'FizzBuzz'),(30,'FizzBuzz')])
def test_fizzbuzz(n,expected): assert fizzbuzz(n)==expected
