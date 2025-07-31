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

def tinhbac(sodinh, adj):
    bac = [0] * sodinh
    for i in range(sodinh):
        for j in range(sodinh):
            if adj[i][j] == 1:
                bac[i] += 1
    print(f"Bậc của các đồ thị: {bac}")
    return bac

def tomau(sodinh, adj, bac):
    mau = 0
    dinh = [] # Danh sach dinh can to mau
    color = [-1] * sodinh 
    for i in range(sodinh):
        dinh.append(i)
    print(f"Danh sách các đỉnh: {dinh}")
    #Sap xep giam danh sach giam dan theo bac
    dinh = sorted(dinh, key=lambda x: bac[x], reverse=True)
    print(f"Danh sách đỉnh giảm dần theo bậc: {dinh}")
    while len(dinh) > 0:
        n = dinh.pop(0)
        print(f"n = {n}")
        color[n] = mau
        # tim cac dinh khong ke voi n
        Tn = [] # Tap cac dinh can to
        for i in range(sodinh):
            if adj[n][i] == 0 and color[i] == -1:
                Tn.append(i)
        # To mau cho cac dinh tiem nang
        print(f"Tn = {Tn}")
        # Loai bo cac dinh ke nhau trong Tn
        for i in Tn:
            for j in Tn:
               if i != j and adj[i][j] == 1 :
                Tn.remove(j)
        print(f"Tn sau khi loại bỏ các đỉnh kề: {Tn}")
                   
        for i in Tn:
            if i in dinh:
                dinh.remove(i)
                color[i] = mau
        print(f"Màu = {color}")
        if(len(dinh) > 0):
            print(f"Đỉnh còn lại chưa tô = {dinh}")
        else:
            print("Đã tô màu xong")    
        mau += 1   

if __name__ == "__main__":
    sodinh, adj = mtk("ToMau_ThamLam/ToMau.txt")
    bac = tinhbac(sodinh, adj)
    tomau(sodinh, adj,bac)
   
