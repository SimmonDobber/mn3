
class EquationSolver:
    def __init__(self, matrix, vector, N):
        self.matrixSize = N
        self.matrix = matrix
        self.vector = vector

    def Solve(self):
        _L, _U, b = self.LUDecomposition()
        y = self.forwardSubstitution(_L, b)
        x = self.backwardSubstitution(_U, y)
        return x

    def LUDecomposition(self):
        _P = [[0 for x in range(self.matrixSize)] for y in range(self.matrixSize)]
        _L = [[0 for x in range(self.matrixSize)] for y in range(self.matrixSize)]
        _U = [[self.matrix[y][x] for x in range(self.matrixSize)] for y in range(self.matrixSize)]
        b = [0 for x in range(self.matrixSize)]

        for i in range(0, self.matrixSize):
            _P[i][i] = _L[i][i] = 1

        for i in range(0, self.matrixSize):
            self.pivoting(_U, _L, _P, i)
            for j in range(i + 1, self.matrixSize):
                _L[j][i] = _U[j][i] / _U[i][i]
                for k in range(i, self.matrixSize):
                    _U[j][k] = _U[j][k] - _L[j][i] * _U[i][k]

        for i in range(0, self.matrixSize):
            for j in range(0, self.matrixSize):
                b[i] += _P[i][j] * self.vector[j]

        return _L, _U, b

    def forwardSubstitution(self, _L, b):
        y = [0 for i in range(self.matrixSize)]
        for i in range(0, self.matrixSize):
            s = 0
            for j in range(0, i):
                s += _L[i][j] * y[j]
            y[i] = (b[i] - s) / _L[i][i]
        return y

    def backwardSubstitution(self, _U, b):
        x = [0 for i in range(self.matrixSize)]
        for i in reversed(range(0, self.matrixSize)):
            s = 0
            for j in range(i + 1, self.matrixSize):
                s = s + _U[i][j] * x[j]
            x[i] = (b[i] - s) / _U[i][i]
        return x

    def pivoting(self, _U, _L, _P, i):
        p = abs(_U[i][i])
        pi = i
        for j in range(i + 1, self.matrixSize):
            if abs(_U[j][i]) > p:
                p = abs(_U[j][i])
                pi = j
        if pi != i:
            for j in range(0, self.matrixSize):
                if j >= i:
                    _U[i][j], _U[pi][j] = _U[pi][j], _U[i][j]
                else:
                    _L[i][j], _L[pi][j] = _L[pi][j], _L[i][j]
                _P[i][j], _P[pi][j] = _P[pi][j], _P[i][j]
