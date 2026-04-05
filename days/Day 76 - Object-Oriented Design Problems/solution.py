# Day 76 — OOP Design — SOLUTIONS
from enum import Enum
from dataclasses import dataclass, field
import random

class SpotSize(Enum): SMALL=1; MEDIUM=2; LARGE=3
class VehicleType(Enum): MOTORCYCLE=1; CAR=2; TRUCK=3

@dataclass
class Vehicle:
    plate: str; type: VehicleType

@dataclass
class ParkingSpot:
    floor:int; number:int; size:SpotSize; vehicle:Vehicle=None
    def is_available(self): return self.vehicle is None
    def fits(self,v): return v.type.value<=self.size.value

class ParkingLot:
    def __init__(self,floors,spots_per_floor):
        self.spots=[]
        sizes=[SpotSize.SMALL,SpotSize.MEDIUM,SpotSize.LARGE]
        for f in range(floors):
            for s in range(spots_per_floor):
                self.spots.append(ParkingSpot(f,s,sizes[s%3]))
    def park(self,vehicle):
        for spot in self.spots:
            if spot.is_available() and spot.fits(vehicle): spot.vehicle=vehicle; return spot
        return None
    def leave(self,spot): spot.vehicle=None
    def available_spots(self): return sum(1 for s in self.spots if s.is_available())

class Suit(Enum): HEARTS='♥'; DIAMONDS='♦'; CLUBS='♣'; SPADES='♠'
class Rank(Enum):
    TWO=2;THREE=3;FOUR=4;FIVE=5;SIX=6;SEVEN=7;EIGHT=8;NINE=9;TEN=10;JACK=11;QUEEN=12;KING=13;ACE=14

@dataclass
class Card:
    suit:Suit; rank:Rank
    def __str__(self): return f'{self.rank.name} of {self.suit.value}'

class Deck:
    def __init__(self): self.cards=[Card(s,r) for s in Suit for r in Rank]
    def shuffle(self): random.shuffle(self.cards)
    def deal(self): return self.cards.pop() if self.cards else None
    def deal_hand(self,n): return [self.deal() for _ in range(n)]
    def __len__(self): return len(self.cards)

class State(Enum): IDLE='idle'; HAS_MONEY='has_money'; DISPENSING='dispensing'

class VendingMachine:
    def __init__(self,inventory): self.inventory=inventory; self.state=State.IDLE; self.balance=0; self.selected=None
    def insert_coin(self,amount): self.balance+=amount; self.state=State.HAS_MONEY
    def select_item(self,code):
        if code in self.inventory and self.balance>=self.inventory[code]['price']:
            self.selected=code; self.state=State.DISPENSING
    def dispense(self):
        if self.state==State.DISPENSING and self.selected:
            item=self.inventory[self.selected]; item['qty']-=1
            self.balance-=item['price']; change=self.balance
            self.balance=0; self.state=State.IDLE; name=item['name']; self.selected=None
            return name
        return None
    def cancel(self): change=self.balance; self.balance=0; self.state=State.IDLE; self.selected=None; return change

class FSNode:
    def __init__(self,name): self.name=name
class File(FSNode): pass
class Directory(FSNode):
    def __init__(self,name): super().__init__(name); self.children={}

class FileSystem:
    def __init__(self): self.root=Directory('/')
    def _traverse(self,path):
        parts=[p for p in path.split('/') if p]
        node=self.root
        for p in parts[:-1]:
            if p not in node.children or not isinstance(node.children[p],Directory): raise FileNotFoundError(p)
            node=node.children[p]
        return node,parts[-1] if parts else None
    def mkdir(self,path):
        parts=[p for p in path.split('/') if p]; node=self.root
        for p in parts:
            if p not in node.children: node.children[p]=Directory(p)
            node=node.children[p]
    def touch(self,path):
        parent,name=self._traverse(path)
        if name and name not in parent.children: parent.children[name]=File(name)
    def ls(self,path):
        parts=[p for p in path.split('/') if p]; node=self.root
        for p in parts: node=node.children[p]
        return list(node.children.keys())
    def rm(self,path):
        parent,name=self._traverse(path)
        if name in parent.children: del parent.children[name]
    def find(self,name,node=None):
        if node is None: node=self.root
        results=[]
        if isinstance(node,Directory):
            for child in node.children.values():
                if child.name==name: results.append(child.name)
                results.extend(self.find(name,child))
        return results
