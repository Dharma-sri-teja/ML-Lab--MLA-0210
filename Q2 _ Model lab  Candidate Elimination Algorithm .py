# Candidate Elimination

import copy

data = [
    ['Premium', 'Low', 'Good', 'Yes'],
    ['Premium', 'High', 'Good', 'Yes'],
    ['Basic', 'High', 'Poor', 'No'],
    ['Basic', 'Low', 'Poor', 'No']
]

attributes = 3

# Initialize S and G
S = ['0'] * attributes
G = [['?'] * attributes]

def more_general(h1, h2):
    return all(h1[i] == '?' or (h1[i] != '0' and (h1[i] == h2[i] or h2[i] == '0'))
               for i in range(len(h1)))

for example in data:
    x = example[:-1]
    y = example[-1]
    
    if y == 'Yes':
        G = [g for g in G if more_general(g, x)]
        for i in range(attributes):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'
                
    else:  # Negative example
        new_G = []
        for g in G:
            for i in range(attributes):
                if g[i] == '?':
                    if S[i] != x[i]:
                        new_h = copy.deepcopy(g)
                        new_h[i] = S[i]
                        new_G.append(new_h)
        G = new_G

print("Final S:", S)
print("Final G:", G)
