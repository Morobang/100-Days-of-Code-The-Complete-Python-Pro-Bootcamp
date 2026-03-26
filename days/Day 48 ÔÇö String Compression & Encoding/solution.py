# Day 48 — Encoding — SOLUTIONS
import re

def rle_encode(s):
    if not s: return ''
    result=[]; i=0
    while i<len(s):
        char=s[i]; count=1
        while i+count<len(s) and s[i+count]==char: count+=1
        result.append((str(count) if count>1 else '')+char); i+=count
    return ''.join(result)

def rle_decode(s):
    result=[]
    for count,char in re.findall(r'(\d*)(\D)',s):
        result.append(char*(int(count) if count else 1))
    return ''.join(result)

def compress(s):
    if not s: return s
    result=[]; i=0
    while i<len(s):
        char=s[i]; count=1
        while i+count<len(s) and s[i+count]==char: count+=1
        result.append(char+str(count)); i+=count
    compressed=''.join(result)
    return compressed if len(compressed)<len(s) else s

def encode(strs): return ''.join(f'{len(s)}#{s}' for s in strs)
def decode(s):
    result=[]; i=0
    while i<len(s):
        j=s.index('#',i); n=int(s[i:j]); i=j+1
        result.append(s[i:i+n]); i+=n
    return result

def to_base(n,base):
    digits='0123456789abcdef'; result=''
    while n: result=digits[n%base]+result; n//=base
    return result or '0'

def from_base(s,base): return int(s,base)

class TreeNode:
    def __init__(self,val): self.val=val; self.left=self.right=None

def serialize(root):
    if not root: return '#'
    return f'{root.val},{serialize(root.left)},{serialize(root.right)}'

def deserialize(data):
    vals=iter(data.split(','))
    def build():
        v=next(vals)
        if v=='#': return None
        node=TreeNode(int(v)); node.left=build(); node.right=build()
        return node
    return build()

def count_and_say(n):
    s='1'
    for _ in range(n-1):
        new=''; i=0
        while i<len(s):
            char=s[i]; count=1
            while i+count<len(s) and s[i+count]==char: count+=1
            new+=str(count)+char; i+=count
        s=new
    return s

def decode_ways(s):
    if not s or s[0]=='0': return 0
    dp=[0]*(len(s)+1); dp[0]=dp[1]=1
    for i in range(2,len(s)+1):
        if s[i-1]!='0': dp[i]+=dp[i-1]
        two=int(s[i-2:i])
        if 10<=two<=26: dp[i]+=dp[i-2]
    return dp[len(s)]
