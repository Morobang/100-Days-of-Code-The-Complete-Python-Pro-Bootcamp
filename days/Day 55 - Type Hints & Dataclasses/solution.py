# Day 55 — Type Hints & Dataclasses — SOLUTIONS
from dataclasses import dataclass, field
from typing import TypeVar, Generic, List, Optional, TypedDict
import math

T = TypeVar('T')

def clamp(n:int, lo:int, hi:int) -> int: return max(lo, min(hi, n))
def flatten(lst): return [x for sub in lst for x in sub]
def group_by(lst, key_fn):
    result = {}
    for item in lst: result.setdefault(key_fn(item),[]).append(item)
    return result

@dataclass
class Product:
    name: str; price: float; quantity: int; category: str='general'
    def __post_init__(self):
        if self.price<=0: raise ValueError('Price must be positive')
    def total_value(self): return round(self.price*self.quantity,2)
    def apply_discount(self,pct): self.price=round(self.price*(1-pct/100),2)

@dataclass(frozen=True)
class Point3D:
    x:float; y:float; z:float
    def distance_to(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    def translate(self,dx,dy,dz): return Point3D(self.x+dx,self.y+dy,self.z+dz)

class UserRecord(TypedDict):
    name:str; email:str; age:int; is_active:bool

def create_user(name,email,age) -> UserRecord:
    return {'name':name,'email':email,'age':age,'is_active':True}

class Stack(Generic[T]):
    def __init__(self): self._data:List[T]=[]
    def push(self,item:T): self._data.append(item)
    def pop(self) -> T:
        if self.is_empty(): raise IndexError('empty')
        return self._data.pop()
    def peek(self) -> Optional[T]: return self._data[-1] if self._data else None
    def is_empty(self) -> bool: return not self._data
