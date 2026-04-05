# Day 30 — CLI Task Manager — SOLUTIONS
import json, os
from datetime import date

PRIORITIES = {'low':1,'medium':2,'high':3}

class Task:
    def __init__(self,title,priority='medium',due_date=None):
        self.title=title; self.priority=priority
        self.due_date=due_date; self.done=False

    def complete(self): self.done=True

    def to_dict(self):
        return {'title':self.title,'priority':self.priority,
                'due_date':self.due_date,'done':self.done}

    @classmethod
    def from_dict(cls,d):
        t=cls(d['title'],d['priority'],d.get('due_date'))
        t.done=d.get('done',False); return t

    def __str__(self):
        status='x' if self.done else ' '
        due=f' due:{self.due_date}' if self.due_date else ''
        return f'[{status}] {self.title} ({self.priority}){due}'

class TaskManager:
    def __init__(self,filepath='/tmp/tasks.json'):
        self.filepath=filepath; self.tasks=[]; self.load()

    def add(self,task): self.tasks.append(task); self.save()

    def complete(self,title):
        for t in self.tasks:
            if t.title==title: t.complete(); self.save(); return

    def delete(self,title):
        self.tasks=[t for t in self.tasks if t.title!=title]; self.save()

    def list_tasks(self,show_done=True):
        tasks=self.tasks if show_done else [t for t in self.tasks if not t.done]
        return sorted(tasks,key=lambda t:PRIORITIES.get(t.priority,0),reverse=True)

    def save(self):
        with open(self.filepath,'w') as f:
            json.dump([t.to_dict() for t in self.tasks],f,indent=2)

    def load(self):
        try:
            with open(self.filepath) as f:
                self.tasks=[Task.from_dict(d) for d in json.load(f)]
        except FileNotFoundError: self.tasks=[]

    def summary(self):
        done=[t for t in self.tasks if t.done]
        return {'total':len(self.tasks),'done':len(done),
                'pending':len(self.tasks)-len(done),
                'by_priority':{p:sum(1 for t in self.tasks if t.priority==p) for p in PRIORITIES}}

def main():
    tm=TaskManager()
    while True:
        print('\n=== Task Manager ===')
        print('1.Add 2.List 3.Complete 4.Delete 5.Exit')
        ch=input('> ').strip()
        if ch=='1':
            title=input('Title: ')
            priority=input('Priority (low/medium/high) [medium]: ') or 'medium'
            due=input('Due date (YYYY-MM-DD) [none]: ') or None
            tm.add(Task(title,priority,due)); print('✅ Added!')
        elif ch=='2':
            for t in tm.list_tasks(): print(t)
        elif ch=='3':
            title=input('Title to complete: '); tm.complete(title); print('✅ Done!')
        elif ch=='4':
            title=input('Title to delete: '); tm.delete(title); print('✅ Deleted!')
        elif ch=='5': print('Bye!'); break

if __name__=='__main__': main()
