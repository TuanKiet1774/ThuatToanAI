def mtk(filename):
    with open(filename, 'r') as f:
        sodinh = int(f.readline().strip())
        print(sodinh)
        adj = []
        for i in range(sodinh):
            line = list(map(int, f.readline().split()))
            adj.append(line)
            print(line)
    return sodinh, adj

def readh(filename):
    with open(filename, 'r') as f:
        h = list(map(int,f.readline().split()))
        print(h)
    return h

def Astar(sodinh, adj, h, start, stop):
   OPEN = [start]
   CLOSE = []
   g = [float('inf')] * sodinh
   f = [float('inf')] * sodinh
   f[start] = h[start]
   g[start] = 0  
   print(f'g = {g}')
   print(f'f = {f}')
   CHA = [-1] * sodinh
   while len(OPEN) > 0:
        n = OPEN.pop(0)
        print(f"n = {n}")
        if n == stop:
            print(f"Tim thay duong di tu {start} den {stop}")
            i = stop
            while i != -1:
                # print(chr(i+65), end="<-") #in ra đường đi bằng chữ cái
                print(i, end="<-")
                i = CHA[i]
            return True
        
        # Nguoc lai
        CLOSE.append(n)
        print(f"CLOSE = {CLOSE}")
        # Tim cac dinh ke
        Tn = []
        for i in range(sodinh):
            if adj[n][i] != 0: # Co duong di tu n den i
                if i not in OPEN and i not in CLOSE:
                    g[i] = g[n] + adj[n][i]
                    f[i] = g[i] + h[i]
                    Tn.append(i)
                    CHA[i] = n
                elif i in OPEN or i in CLOSE:    
                    gnew = g[n] + adj[n][i]
                    fnew = gnew + h[i]
                    print(f"gnew[i] = {gnew} <- OPEN: {gnew}")
                    print(f"fnew[i] = {fnew} <- OPEN: {fnew}")
                    if fnew < f[i]:
                        g[i] = gnew
                        f[i] = fnew
                        CHA[i] = n
        print(f"Tn = {Tn}")                    
        OPEN = OPEN + Tn
        print(f"OPEN = {OPEN}")
        # Sap xep OPEN theo f
        OPEN = sorted(OPEN, key=lambda x: f[x])
        print(f"OPEN sorted = {OPEN}")
        print(f"g = {g}")
        print(f"f = {f}")
        print(f"CHA = {CHA}")
   # Het while
   print(f"Khong tim thay duong di tu {start} den {stop}")    

    
if __name__ == "__main__":
    sodinh, adj = mtk("ThuatToan_Astar/VD_Astar.txt")
    h = readh("ThuatToan_Astar/He_Astar.txt")
    Astar(sodinh, adj, h, 0, 10)