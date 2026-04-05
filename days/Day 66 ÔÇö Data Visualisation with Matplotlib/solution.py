# Day 66 — Matplotlib — SOLUTIONS
import matplotlib.pyplot as plt
import numpy as np

def plot_trend(dates,values,title):
    fig,ax=plt.subplots(figsize=(10,4))
    ax.plot(dates,values,marker='o',linewidth=2)
    ax.set_title(title); ax.set_xlabel('Date'); ax.set_ylabel('Value')
    ax.grid(True,alpha=0.3); plt.tight_layout(); return fig

def plot_bar(categories,values,title):
    sorted_pairs=sorted(zip(values,categories)); vals,cats=zip(*sorted_pairs)
    fig,ax=plt.subplots(figsize=(8,5))
    ax.barh(cats,vals); ax.set_title(title); plt.tight_layout(); return fig

def plot_scatter(x,y,labels=None):
    fig,ax=plt.subplots(figsize=(8,6))
    ax.scatter(x,y,alpha=0.7)
    if labels:
        for xi,yi,l in zip(x,y,labels): ax.annotate(l,(xi,yi))
    m,b=np.polyfit(x,y,1); ax.plot(x,[m*xi+b for xi in x],'r--',alpha=0.5)
    return fig

def four_charts(data):
    fig,axes=plt.subplots(2,2,figsize=(12,10))
    x=range(len(data))
    axes[0,0].plot(x,data); axes[0,0].set_title('Line')
    axes[0,1].bar(x,data); axes[0,1].set_title('Bar')
    axes[1,0].scatter(x,data); axes[1,0].set_title('Scatter')
    axes[1,1].hist(data,bins=10); axes[1,1].set_title('Histogram')
    plt.tight_layout(); return fig

def save_chart(fig,filepath):
    fig.savefig(filepath,dpi=150,bbox_inches='tight')
