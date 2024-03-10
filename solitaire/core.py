class Martix:
    def __init__(self, size, init_v) -> None:
        self._size = size
        self._martix = [[init_v for __ in range(size[0])] for __ in range(size[1])]
    
    def set(self, idx, v):
        self._martix[idx[1]][idx[0]] = v
    
    def set_all(self, idx_1, idx_2, v):
        for x in range(idx_1[0], idx_2[0]+1):
            for y in range(idx_1[1], idx_2[1]+1):
                self.set((x, y), v)
                
    def get(self, idx):
        return self._martix[idx[1]][idx[0]]
    
    @property
    def size(self): return self._size


class Rander:
    def __init__(self, martix: Martix) -> None:
        self.__martix = martix
    
    def show(self):
        print("   0 1 2 3 4 5 6  ")
        print(" ┌─┴─┴─┴─┴─┴─┴─┴─┐")
        for i in range(self.__martix.size[1]):
            print(f'{i}┤', end=' ')
            for j in range(self.__martix.size[0]):
                elemt = self.__martix.get((j, i))
                if elemt ==  2:
                    print(' ', end=' ')
                elif elemt == 1: 
                    print("●", end=' ')
                else:
                    print("๐", end=' ')
            print('│')
        print(" └───────────────┘")


class ChessBoard(Martix):
    def __init__(self, size) -> None:
        super().__init__(size, 1)
        self.set_all((0, 0), (1, 1), 2)
        self.set_all((0, 5), (1, 6), 2)
        self.set_all((5, 0), (6, 1), 2)
        self.set_all((5, 5), (6, 6), 2)
        self.set((3, 3), 0)

    def is_empty(self, idx):
        try:
            return True if self.get(idx) == 0 else False
        except IndexError:
            return False

    def is_piece(self, idx):
        try:
            return True if self.get(idx) == 1 else False
        except IndexError:
            return False

    def is_out_of_range(self, idx):
        try:
            return True if self.get(idx) == 2 else False
        except IndexError:
            return True
    
    def get_all_points(self):
        for i in range(self._size[1]):
            for j in range(self._size[0]):
                if self.get((j, i)) == 1:
                    yield (j, i)
    
    def __str__(self) -> str:
        return str(self._martix)


class Engine:
    def __init__(self) -> None:
        self.ch_bd = ChessBoard((7, 7))
        self.render = Rander(self.ch_bd)
    
    def start(self):
        try:
            print("\nWARNING:")
            print("\tMono font is recommended to have a better rendering effects.\n".upper())
            print("Press enter to continue.")
            input('\>')
            self.render.show()
            while True:
                print()
                operation = input("\> ")
                try:
                    p1, p2 = self.identify_input(operation)
                except:
                    print("illegal input(1)")
                    continue

                mid_p = cal_mid_point(p1, p2)
                if mid_p:
                    if self.ch_bd.is_piece(mid_p):
                        self.ch_bd.set(p1, 0)
                        self.ch_bd.set(mid_p, 0)
                        self.ch_bd.set(p2, 1)
                        self.render.show()

                        status = self.check_chessboard()
                        if status == 0:
                            print("Congratulations, you've done it well!")
                            print(f"Remaining points: {len(list(self.ch_bd.get_all_points()))}.")
                            print()
                            break

                        continue
                print("illegal input(2)")
        except KeyboardInterrupt:
            print("\nExit.\n".upper())
    
    def check_chessboard(self):
        p = list(self.ch_bd.get_all_points())
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                res = is_nearby_point(p[i], p[j])
                if res is not None:
                    return 1
        return 0

    def identify_input(self, ipt):
            selct = (int(ipt[0]), int(ipt[1]))
            place = (int(ipt[2]), int(ipt[3]))
            if self.ch_bd.is_piece(selct) and not self.ch_bd.is_piece(place):
                return selct, place

def cal_mid_point(p1, p2):
    res = is_nearby_point(p1, p2)
    if res is not None:
        if res == 0:
            return (int((p1[0] + p2[0]) / 2), p1[1])
        else:
            return (p1[0], int((p1[1] + p2[1]) / 2))

def is_nearby_point(p1, p2):
    for i, j in ((0, 1), (1, 0)):
        if (p1[i] + 2 == p2[i]) or (p1[i] - 2 == p2[i]):
            if p1[j] == p2[j]:
                return i
