import os
def shutdown():
    print('Shutting Down...')
    os.system('shutdown /s /t 3')
ans = input('Are You Sure You Want to Shut Down? (Yes/No) ')
if ans == 'Yes':
    shutdown()
elif ans == 'No':
    print ('Shutdown Aborted.')
else:
    print ('Invalid Input.')