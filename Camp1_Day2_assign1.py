Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

check = Sessions_Attended["sessions"][-1]

if check == ',':
    newSession = Sessions_Attended["sessions"][0:-1]

newSession = Sessions_Attended["sessions"]
arr = newSession.split(',')

print ('I have attended ' + str(len(arr)) + ' sessions!!')
