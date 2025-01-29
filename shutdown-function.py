import os
ans = input('Are You Sure You Want to Shut Down? (Yes/No) ')
if ans == 'Yes':
    print('Shutting Down...')
    os.system('shutdown /s /t 3')
elif ans == 'No':
    print ('Shutdown Sequence Aborted.')
else:
    print ('Invalid Input.')