from EquationSolver import EquationSolver


class Interpolator:

    @staticmethod
    def lagrange(xp, yp, x):
        y = 0
        for i in range(0, len(xp)):
            f = 1
            for j in range(0, len(xp)):
                if i != j:
                    f *= (x - xp[i])
                    f /= (xp[i] - xp[j])
            y += f * yp[i]
        return y

    @staticmethod
    def splines(xp, yp, x):
        n = len(xp) - 1
        N = n * 4
        h = abs(xp[1] - xp[0])
        M, b = Interpolator.getSplinesMatrixAndVector(xp, yp, n, N, h)
        equationSolver = EquationSolver(M, b, N)
        x = equationSolver.Solve()
        xi = 0
        for i in range(0, n):
            if x >= xp[i] & x <= xp[i + 1]:
                xi = i
                break
        y = 0
        y += x[xi * 4]
        y += x[xi * 4 + 1] * h
        y += x[xi * 4 + 2] * h ** 2
        y += x[xi * 4 + 3] * h ** 3
        return y

    @staticmethod
    def getSplinesMatrixAndVector(xp, yp, n, N, h):
        M = [[0 for x in range(0, N)] for y in range(0, N)]
        b = [0 for x in range(0, N)]
        for i in range(0, n):
            M[i][i * 4] = 1
            b[i] = yp[i]
        for i in range(0, n):
            M[i + n][i * 4] = 1
            M[i + n][i * 4 + 1] = h
            M[i + n][i * 4 + 2] = h ** 2
            M[i + n][i * 4 + 3] = h ** 3
            b[i + n] = yp[i + 1]
        for i in range(0, n - 1):
            M[i + n * 2][i * 4 + 1] = 1
            M[i + n * 2][i * 4 + 2] = 2 * h
            M[i + n * 2][i * 4 + 3] = 3 * h ** 2
            M[i + n * 2][i * 4 + 5] = -1
        for i in range(0, n - 1):
            M[i + n * 3 - 1][i * 4 + 2] = 2
            M[i + n * 3 - 1][i * 4 + 3] = 6 * h
            M[i + n * 3 - 1][i * 4 + 6] = -2
        M[n * 4 - 2][2] = 1
        M[n * 4 - 1][n * 4 - 2] = 2
        M[n * 4 - 1][n * 4 - 1] = 6 * h
        return M, b





