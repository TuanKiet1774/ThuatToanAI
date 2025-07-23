def readMTK(filename):
  with open(filename, 'r') as f:
    soDinh  = int(f.readline())
    print(soDinh)
    adj = []
    for i in range(soDinh):
      line = list(map(int,f.readline().split()))
      adj.append(line)
      print(line)
    # print(adj)
  return soDinh, adj

def dfs(soDinh, adj, start, stop):
  open = [start]
  close = []
  cha = [-1] * soDinh
  print(cha)
  
  while len(open) > 0:
    n = open.pop(0) #Lấy phần tử đầu tiên của ds
    print(f"n = {n}")    
    close.append(n)
    print(f"Close = {close}")
    if n == stop:
      print(f"tìm thấy đường đi từ {start} đến {stop}")
      #in đường đi
      i = stop
      while i != -1:
        print(i, end = "<=" )
        i = cha[i]
      return True
    #Ngược lại tìm các đỉnh kề của đỉnh n
    Tn = [] #Reset Tn rổng
    for i in range(soDinh):
      if(adj[n][i] == 1 and i not in open and i not in close):
        Tn.append(i)
        cha[i] = n
    print(Tn)
    print(f"Tn = {Tn}")
    open = Tn + open #Thêm TN vào trước Open
    print(f"Open = {open}")
    print(f"Cha = {cha}")
  print(f"Không tìm thấy đường đi từ {start} đến {stop}")


if __name__=="__main__":
    soDinh, adj = readMTK("ThuatToan_DFS/VD1C2_DFS.txt")
    dfs(soDinh, adj, 0, 6) 