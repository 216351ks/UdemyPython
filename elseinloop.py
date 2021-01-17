instruction = ['say hello','say how are you','abort','ask for money', 'say than you','say bye']
instructionApproved=[]

for instr in instruction:
    print('Adding instruction: ',instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!!')
        break

else: 
    print('Following actions will be taken: ', instructionApproved)

print('-'*30)

i = 0

while i< len(instruction):
    print('Adding instruction: ',instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!')
        instructionApproved.clera()
        break
    
    i+=1
    
else: 
    print('Following actions will be taken: ', instructionApproved)