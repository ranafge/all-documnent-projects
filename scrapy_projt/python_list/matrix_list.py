metrix = [[1, 2, 2], [2, 2, 2], [2, 2, 1]]
n,m = 3,3
def package(n,m,arr):
    xyz = arr.copy()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                xyz[i][j]=0
    print("arr",arr)
    print("xyz",xyz)

package(n,m,metrix)

import subprocess
subprocess.run('dir', shell=True)

