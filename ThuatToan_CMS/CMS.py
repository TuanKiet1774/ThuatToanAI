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

def CMS(sodinh, adj, h, start, stop):
   OPEN = [start]
   CLOSE = []
   g = [0] * sodinh
   print(f'g = {g}')
   CHA = [-1] * sodinh

   while len(OPEN) > 0:
        n = OPEN.pop(0)
        print(f"n = {n}")
        if n == stop:
            print(f"Tim thay duong di tu {start} den {stop}")
            i = stop
            while i != -1:
                print(i, end="<-")
                i = CHA[i]
            return True
        
        # Nguoc lai
        CLOSE.append(n)
        print(f"CLOSE = {CLOSE}")
        # Tim cac dinh ke
        Tn = []
        for i in range(sodinh):
            if adj[n][i] == 1:
                if i not in OPEN and i not in CLOSE:
                    # g[i] = g[n] + h[i]
                    g[i] = g[n] + adj[n][i]
                    Tn.append(i)
                    CHA[i] = n
                elif i in OPEN:    
                    # gnew = g[n] + h[i]
                    gnew = g[n] + adj[n][i]
                    print(f"gnew[i] = {gnew}")
                    if gnew < g[i]:
                        g[i] = gnew
                        CHA[i] = n
        print(f"Tn = {Tn}")                    
        OPEN = OPEN + Tn
        print(f"OPEN = {OPEN}")
        # Sap xep OPEN theo g
        OPEN = sorted(OPEN, key=lambda x: g[x])
        print(f"OPEN sorted = {OPEN}")
        print(f"g = {g}")
        print(f"CHA = {CHA}")
   print(f"Khong tim thay duong di tu {start} den {stop}")    
    
if __name__ == "__main__":
    sodinh, adj = mtk("ThuatToan_CMS/cms.mtk")
    h = readh("ThuatToan_CMS/cms.heuristic")
    CMS(sodinh, adj, h, 0, 7)