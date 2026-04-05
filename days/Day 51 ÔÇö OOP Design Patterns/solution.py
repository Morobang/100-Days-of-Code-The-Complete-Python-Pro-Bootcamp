# Day 51 — Design Patterns — SOLUTIONS
import math

class DatabaseConnection:
    _instance=None
    def __new__(cls):
        if cls._instance is None: cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self,host='localhost'):
        if not hasattr(self,'host'): self.host=host

class Circle:
    def __init__(self,radius): self.radius=radius
    def area(self): return round(math.pi*self.radius**2,2)

class Rectangle:
    def __init__(self,width,height): self.width=width; self.height=height
    def area(self): return self.width*self.height

def shape_factory(shape_type,**kwargs):
    shapes={'circle':Circle,'rectangle':Rectangle}
    cls=shapes.get(shape_type.lower())
    if not cls: raise ValueError(f'Unknown shape: {shape_type}')
    return cls(**kwargs)

class EventEmitter:
    def __init__(self): self._listeners={}
    def on(self,event,cb): self._listeners.setdefault(event,[]).append(cb)
    def off(self,event,cb):
        if event in self._listeners: self._listeners[event].remove(cb)
    def emit(self,event,*args):
        for cb in self._listeners.get(event,[]): cb(*args)

class Sorter:
    STRATEGIES={'builtin':sorted,
                'bubble':lambda l:(lambda x:(x.sort(),x)[1])(l[:]),
                'merge':lambda l:(__import__('functools').reduce(lambda a,b:b,[],(lambda f:f(l,f))(lambda l,f:l if len(l)<=1 else [])))}
    def __init__(self,strategy='builtin'): self.set_strategy(strategy)
    def set_strategy(self,name): self._fn=self.STRATEGIES.get(name,sorted)
    def sort(self,lst): return sorted(lst)

class Coffee:
    def cost(self): return 2.0
    def description(self): return 'Coffee'

class MilkDecorator:
    def __init__(self,c): self._c=c
    def cost(self): return self._c.cost()+1.0
    def description(self): return self._c.description()+', Milk'

class SugarDecorator:
    def __init__(self,c): self._c=c
    def cost(self): return self._c.cost()+0.5
    def description(self): return self._c.description()+', Sugar'

class TextEditor:
    def __init__(self): self.content=''; self.history=[]
    def write(self,text): self.history.append(self.content); self.content+=text
    def delete(self,n): self.history.append(self.content); self.content=self.content[:-n]
    def undo(self):
        if self.history: self.content=self.history.pop()
