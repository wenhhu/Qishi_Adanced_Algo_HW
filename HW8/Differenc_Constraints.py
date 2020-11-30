import numpy as np

class problem1:
    def __init__(self, timeslot, cashier):
        self.timeslot = []
        self.cap = []
        for i in range(len(timeslot)):
            if timeslot[i] != 0:
                self.timeslot.append(i)
                self.cap.append(timeslot[i])
        self.graph = [[self.cap[i] + self.cap[j] if i != j else self.cap[i] for j in range(len(self.timeslot))] for i in range(len(self.timeslot))]
        self.cashier = cashier

    def build_graph(self):
        for i in self.cashier:
            for j, c in zip(range(len(self.timeslot)), self.cap):
                if (self.timeslot[j] >= i or (i >= 16 and (i+8) % 24 >= self.timeslot[j])) and ((self.timeslot[j] <= i+8) or (self.timeslot[j] <= (i+8) % 24)):
                    for k, cc in zip(range(len(self.timeslot)), self.cap):
                        if self.timeslot[k] != j and (self.timeslot[k] >= i or (i >= 16 and (i+8) % 24 >= self.timeslot[k])) and ((self.timeslot[k] <= i+8) or (self.timeslot[k] <= (i+8) % 24)):
                            if (j == 3 or k == 3):
                                print(self.timeslot[k], self.timeslot[j], i)
                            self.graph[j][k] = max(self.graph[j][k] - 1, c, cc)
                            self.graph[k][j] = max(self.graph[k][j] - 1, c, cc)

    def bellman(self):
        D = [self.graph[i].copy() for i in range(len(self.timeslot))]
        for i in range(len(self.timeslot)):
            for j in range(len(self.timeslot)):
                D[i][j] = np.inf if D[i][j] != max(self.cap[i], self.cap[j]) else D[i][j]

        for k in range(len(self.timeslot)):
            for i in range(len(self.timeslot)):
                for j in range(len(self.timeslot)):
                    D[i][j] = D[i][j] if D[i][j] < D[i][k]+D[k][j] else D[i][k]+D[k][j]
        return D

if __name__ == '__main__':
    timeslot = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    cashier = [0, 23, 22, 1, 10, 6]
    prob = problem1(timeslot, cashier)
    prob.build_graph()
    D = prob.bellman()
    res = np.inf
    for i in range(len(D)):
        if res > D[i][(i+len(D)-1) % len(D)]:
            res = D[i][(i+len(D)-1) % len(D)]

    print(res)

