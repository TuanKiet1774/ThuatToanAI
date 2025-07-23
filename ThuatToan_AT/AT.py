def readmtk(filename):
    with open(filename,'r') as f:
        n = int(f.readline().strip())
        print(n)
        adj=[]
        for i in range(n): # i=0;i<n;i++
            line = list(map(int,f.readline().split()))
            print(line)
            adj.append(line)
    return n, adj

def readheuristic(filename):
    with open(filename,'r') as f:
        n = int(f.readline().strip())
        print(n)
        h = list(map(int,f.readline().split()))
        print(h)
    return h

def AT(n,adj,h,start,stop):
    OPEN = [start]  
    CLOSE = []
    PARENT = [-1] * n

    while len(OPEN) > 0:
        cur = OPEN.pop(0)
        print(f"cur = {cur}")
        CLOSE.append(cur)
        print(f"CLOSE = {CLOSE}")
        if cur == stop:
            print(f"Tim thay duong di tu {start} - {stop}")
            i = stop
            while i != -1:
                print(i, end=" <== ")
                i = PARENT[i]
            return 
        
        # Nguoc lai, tim cac dinh ke cua cur
        for i in range(n):
            if adj[cur][i] == 1 and i not in OPEN and i not in CLOSE:
                h[i] = h[cur] + h[i]
                OPEN.append(i)
                PARENT[i] = cur

        OPEN.sort(key=lambda x: h[x])   
        print(f"OPEN = {OPEN}")
        print(f"PARENT = {PARENT}")
    print(f"Khong tim thay duong di tu {start} - {stop}")    

if __name__=="__main__":
    n, adj = readmtk("leodoi.mtk")
    h = readheuristic("leodoi.heuristic")   
    AT(n,adj,h,0,8)