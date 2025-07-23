def readmtk(filename):
    with open(filename,'r') as f:
        n = int(f.readline().strip())
        print(n)
        adj=[]
        for i in range(n):
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

def HillClimbingSearch(n,adj,h,start,stop):
    OPEN = [start]  
    CLOSE = []
    PARENT = [-1] * n

    while len(OPEN) > 0:
        cur = OPEN.pop(0) #Đỉnh hiện tại là đỉnh đầu tiên của OPEN
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
        Tn = [] # Luu tru cac dinh ke cua cur
        for i in range(n):
            if adj[cur][i] == 1 and i not in OPEN and i not in CLOSE:
                Tn.append(i)
                PARENT[i] = cur

        print(f"Tn = {Tn}")        
        Tn_sort = sorted(Tn, key=lambda x: h[x]) # Sắp xếp Tn theo thứ tự tăng dần của Heuristic
        print(f"Sắp xếp Tn: {Tn_sort}")
        OPEN =  Tn_sort + OPEN # Tn và đầu OPEN
        print(f"OPEN = {OPEN}")
        print(f"PARENT = {PARENT}")
    print(f"Khong tim thay duong di tu {start} - {stop}")    

if __name__=="__main__":
    n, adj = readmtk("ThuatToan_LeoDoi/VD_LeoDoi.txt")
    h = readheuristic("ThuatToan_LeoDoi/He_LeoDoi.txt")   
    HillClimbingSearch(n,adj,h,0,8)