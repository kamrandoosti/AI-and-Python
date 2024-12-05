#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:38:45 2024

@author: kamran
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y1=['a','b','c','d','e','f']
y2=['G','H','I','I','J','K']
y3=['l','m','n','o','p','q']
fig,ax=plt.subplots()
ax.plot(x, y1,marker='o',color='black',linestyle='-.',label='y1')
ax.plot(x,y2, marker='*', linestyle='None', markersize=30, color='red')
ax.plot(x,y3,label='y3',linestyle='-.',color='darkmagenta',linewidth=2)
# plt.plot(3,3, marker='o')
ax.set_ylabel('alpha')
ax.set_xlabel('number')
ax.set_title('alphanumeric')
ax.grid(True,linestyle='--',linewidth=1.3,color='yellow')
image=plt.imread('/home/kamran/9b60bb3a458207ca407a3764a4771e03.jpg')
ax.imshow(image,aspect='auto',extent=[min(x),max(x), ax.get_ylim()[0],ax.get_ylim()[1]],alpha=0.5)
# plt.annotate("middle value", xy=(3,30), xytext=(5,30),arrowprops=dict(facecolor='red'))
# plt.annotate("middle value", xy=(3,30), xytext=(5,30),arrowprops=dict())
ax.set_facecolor('lightblue')
ax.text(2.5,-4,'this is a test name',color='red',fontsize=10)
ax.legend()
plt.savefig('/home/kamran/plt.pdf',dpi=300)
plt.show()
