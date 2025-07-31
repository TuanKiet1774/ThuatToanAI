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
    g = [float('inf')] * sodinh
    f = [float('inf')] * sodinh
    g[start] = 0
    f[start] = h[start]
    print(f"g = {g}")
    print(f"f = {f}")
    CHA = [-1] * sodinh
    flag = False #Chưa tìm thấy đường đi (n = goal ==> flag = true)

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
            if f[n] >= min: # Nếu f[n] >= fmin
                print(f"f[{n}] > fmin = {min} : Xén tỉa nhánh con")
            else: # Nếu f[n] < fmin
                Tn = [] #Khởi tạo danh sách kề = rỗng
                for i in range(sodinh):
                    if adj[n][i] > 0: # Có đỉnh kề
                        #TH1: i không thuộc OPEN và CLOSE
                        # tính g, f, chèn vào Tn và ghi nhận CHA
                        if i not in OPEN and i not in CLOSE: 
                            print(f"{i} NOT IN OPEN and NOT IN CLOSE")
                            g[i] = g[n] + adj[n][i]
                            f[i] = g[i] + h[i]
                            Tn.append(i)
                            CHA[i] = n 
                        #TH2: i thuộc OPEN 
                        elif i in OPEN and i not in CLOSE: 
                            print(f"{i} IN OPEN and NOT IN CLOSE")
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Nếu fnew < f[i] thì cập nhật g[i], f[i], CHA, không chèn vào Tn
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}] ==> Cập nhật: g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                # Tn.append(i) # có trong OPEN rồi nên không chèn vào Tn 
                        #TH3: i thuộc CLOSE
                        elif i not in OPEN and i in CLOSE:   
                            print(f"{i} NOT IN OPEN and IN CLOSE")
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Nếu fnew < f[i] thì cập nhật g[i], f[i], CHA, chèn vào Tn
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}] ==> Cập nhật: g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                Tn.append(i)
                        #TH4: i thuộc OPEN và CLOSE
                        elif i in OPEN and i in CLOSE:   
                            print(f"{i} IN OPEN and IN CLOSE") 
                            gnew = g[n] + adj[n][i]
                            fnew = gnew + h[i]
                            print(f"gnew[i] = {gnew}")
                            print(f"fnew[i] = {fnew}")
                            # Nếu fnew < f[i] thì cập nhật g[i], f[i], CHA, không chèn vào Tn
                            if fnew < f[i]:
                                print(f"fnew = {fnew} <f[i] = f[{i}]: Cap nhat g[{i}] = {gnew}, f[{i}] = {fnew}, CHA")
                                g[i] = gnew
                                f[i] = fnew
                                CHA[i] = n 
                                
                Tn = sorted(Tn, key=lambda x: f[x]) #Sắp xếp Tn theo f 
                print(f"Tn đẵ sắp xếp: {Tn}")             
                OPEN = Tn + OPEN # Chèn Tn vào đầu OPEN
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
        # print(chr(i+65), end="<-")
        print(i, end="<-")
        i = CHA[i]
    
if __name__ == "__main__":
    # sodinh, adj = mtk("ThuatToan_NhanhCan/BT_NhanhCan.txt")
    # h = readh("ThuatToan_NhanhCan/HeBT_NhanhCan.txt")
    # BranchAndBound(sodinh, adj, h, 0, 7)
    sodinh, adj = mtk("ThuatToan_NhanhCan/VD_NhanhCan.txt")
    h = readh("ThuatToan_NhanhCan/HeVD_NhanhCan.txt")
    BranchAndBound(sodinh, adj, h, 0, 1)