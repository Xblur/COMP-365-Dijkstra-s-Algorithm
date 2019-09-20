# =============================================================================
# Made by: Hoz Rashid
# =============================================================================
import math
f = open ("Dijkstra_Data_1600.txt")
s = f.read()
s = s.strip()
s = s.splitlines()
numofvertex = int(s[0])
s.pop(0)
i = 0
while i<len(s):
    a = s[i]
##    a = a.strip()
    a = a.split()
    s.pop(i)
    s.insert(i, a)
    i += 1
##print(s)
a = 0

def W(v , w):
    return int(s[v][w])
pinf=math.inf
cost = []
reached = []
candidate = []
estimate = []
predecessor = []
i = 0
while i<numofvertex:
    cost.append(pinf)
    reached.append(False)
    candidate.append([])
    j= 0
    while j<numofvertex:
        candidate[i].append(False)
        j +=1
    estimate.append(pinf)
    predecessor.append(None)
    i += 1
##print(estimate)
reached[0]=True
cost[0]=0
estimate[0]=0
i=0
for i, value in enumerate (s[0]):
    if int(value) != 0:
        estimate [i] = float(value)
        candidate[0][i]=True
        cost[i]= int(value)
    elif int(value) == 0 and i !=0:
        estimate[i]= pinf
        candidate[0][i] = False
finished = False
x=0
i=0
v = 0
while not all(reached):
    best_candidate_estimate = pinf
    i%=numofvertex
    j = 0
    while i < numofvertex*3:
        b = i
        i%=numofvertex
        while any(candidate[i]):
            j %= numofvertex
    #        print(candidate[j])
    #        print(estimate[j])
            if candidate[i][j] == True or float(estimate[j]) < best_candidate_estimate:
                v = j
                best_candidate_estimate = float(estimate[j])
                cost[v] = estimate[v]
                reached[v]=True    
                candidate[i][v]=False
                for y, value in enumerate (s[v]):
                    if W(v,y) > 0 and y != 0:
                        if cost[v]+W(v,y) < estimate[y]:
                            estimate[y]=cost[v]+W(v,y)
                            candidate[v][y]=True
                            predecessor[y]=v  
            j+=1
        if any(candidate [i]):
            i=0
        else:
            i=b
        i+=1
    i+=1
print(max(cost))
print(cost.index(max(cost)))
print(max(estimate))
print(estimate.index(max(estimate)))