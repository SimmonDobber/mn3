
class SetOfEquations:
    def __init__(self, matrix, vector, N):
        self.matrixSize = N
        self.matrix = matrix
        self.vector = vector

    def LUSolve(self):
        _L, _U = self.LUDecomposition()
        y = self.forwardSubstitution(_L, self.vector)
        x = self.backwardSubstitution(_U, y)
        return x

    def LUDecomposition(self):
        _L = [[0 for x in range(self.matrixSize)] for y in range(self.matrixSize)]
        _U = [[0 for x in range(self.matrixSize)] for y in range(self.matrixSize)]
        for i in range(0, self.matrixSize):
            for j in range(0, self.matrixSize):
                if j >= i:
                    _L[j][i] = self.matrix[j][i]
                    for k in range(0, i):
                        _L[j][i] = _L[j][i] - _L[j][k] * _U[k][i]
            for j in range(0, self.matrixSize):
                if j == i:
                    _U[i][j] = 1
                elif j >= i:
                    _U[i][j] = self.matrix[i][j] / _L[i][i]
                    for k in range(0, i):
                        _U[i][j] = _U[i][j] - ((_L[i][k] * _U[k][j]) / _L[i][i])
        return _L, _U

    def forwardSubstitution(self, _L, b):
        y = [0 for i in range(self.matrixSize)]
        for i in range(0, self.matrixSize):
            s = 0
            for j in range(0, i):
                s = s + _L[i][j] * y[j]
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
