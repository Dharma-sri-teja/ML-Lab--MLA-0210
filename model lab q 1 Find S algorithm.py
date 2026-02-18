# FIND-S Algorithm

# Training data
data = [
    ['Premium', 'Low', 'Good', 'Yes'],
    ['Premium', 'High', 'Good', 'Yes'],
    ['Basic', 'High', 'Poor', 'No'],
    ['Basic', 'Low', 'Poor', 'No']
]

# Initialize hypothesis with most specific values
hypothesis = ['0', '0', '0']

for example in data:
    if example[-1] == 'Yes':  # Only positive examples
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = example[i]
            elif hypothesis[i] != example[i]:
                hypothesis[i] = '?'

print("Final Hypothesis (FIND-S):", hypothesis)
