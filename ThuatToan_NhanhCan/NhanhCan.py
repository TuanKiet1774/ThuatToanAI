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

from tracemalloc import start


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

def BranchAndBound(sodinh, adj, h, start, stop):
    OPEN = [start]
    CLOSE = []
    min = float('inf')
    flag = False #chua tim thay duong di (n = dich gan flag = true)
    g = [float('inf')] * sodinh
    f = [float('inf')] * sodinh
    g[start] = 0
    f[start] = h[start]
    print(f"g = {g}")
    print(f"f = {f}")
    CHA = [-1] * sodinh

    while len(OPEN) > 0:
        n = OPEN.pop(0)
        print(f"n= {n}")
        CLOSE.append(n)
        print(f"CLOSE = {CLOSE}")
        if n == stop:
            flag = True
            if (f[n] < min): 
                print(f"Cap nhat fmin = {f[n]}")
                min = f[n]
            else:
                print(f"f[{n}] = {f[n]} > fmin = {min}")
        else:
            if f[n] >= min: # Neu f[n] >= fmin
                print(f"f[{n}] > fmin = {min} : Xen tia nhanh con")
            else: # Neu f[n] < fmin
                # Tim cac dinh ke
                Tn = [] #reset Tn
                for i in range(sodinh):
                    if adj[n][i] > 0: # Co duong di tu n den i
                        #TH1: i khong thuoc open, khong thuoc close
                        if i not in OPEN and i not in CLOSE:
                            print(f"{i} NOT IN OPEN and NOT IN CLOSE")
                            g[i] = g[n] + adj[n][i]
                            f[i] = g[i] + h[i]
                            Tn.append(i)
                            CHA[i] = n
                        #TH2: i khong thuoc open, thuoc close
                        elif i not in OPEN and i in CLOSE:   
                            print(f"{i} NOT IN OPEN , IN CLOSE")
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Neu fnew < f[i] thi cap nhat g[i], f[i],
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}]: Cap nhat g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                Tn.append(i)
                        #TH3: i thuoc open, khong thuoc close
                        elif i in OPEN and i not in CLOSE: 
                            print(f"{i} IN OPEN ,NOT IN CLOSE")
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Neu fnew < f[i] thi cap nhat g[i], f[i],
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}]: Cap nhat g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                # Tn.append(i) ko chen vao Tn == ko chen vao open
                        #TH4: i thuoc open, thuoc close
                        elif i in OPEN and i in CLOSE:   
                            print(f"{i} IN OPEN and IN CLOSE") 
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Neu fnew < f[i] thi cap nhat g[i], f[i],
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}]: Cap nhat g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                
                print(f"Tn = {Tn}")
                Tn = sorted(Tn, key=lambda x: f[x])                        
                OPEN = Tn + OPEN 
                print(f"OPEN = {OPEN}")
                print(f"g = {g}")
                print(f"f = {f}")
                print(f"CHA = {CHA}")
                
    if flag == True:
        print(f"Tim thay duong di tu {start} den {stop}")    
    else:
        print(f"Khong tim thay duong di tu {start} den {stop}")
    
    i = stop
    while i != -1:
        print(chr(i+65), end="<-")
        # print(i, end="<-")
        i = CHA[i]
    
if __name__ == "__main__":
    sodinh, adj = mtk("ThuatToan_NhanhCan/VD_NhanhCan.txt")
    h = readh("ThuatToan_NhanhCan/He_NhanhCan.txt")
    BranchAndBound(sodinh, adj, h, 0, 7)