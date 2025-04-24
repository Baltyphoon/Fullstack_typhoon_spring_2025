# File Meta Data 
import os 

if os.path.exists('advenced.txt'):
    size = os.path.getsize('advenced.txt')
    print(size)

    # get modification time
    mod_time = os.path.getmtime('advenced.txt')
    print(mod_time)
    os.rename('advenced.txt', 'new_advenced.txt')
    print('renamed')
    os.remove('new_advenced.txt')
    print('removed')

