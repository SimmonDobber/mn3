from EquationSolver import EquationSolver


class Interpolator:

    @staticmethod
    def lagrange(xp, yp, x):
        y = 0
        for i in range(0, len(xp)):
            f = 1
            for j in range(0, len(xp)):
                if i != j:
                    f *= (x - xp[j])
                    f /= (xp[i] - xp[j])
            y += f * yp[i]
        return y

    @staticmethod
    def splines(xp, yp, xs, x):
        n = len(xp) - 1
        h = abs(xp[1] - xp[0])
        xi = -1
        for i in range(0, n):
            if (x >= xp[i]) & (x <= xp[i + 1]):
                xi = i

        if xi == -1:
            y = yp[len(yp) - 1]
            return y
        y = 0
        y += xs[xi * 4]
        y += xs[xi * 4 + 1] * (x - xp[xi])
        y += xs[xi * 4 + 2] * (x - xp[xi]) ** 2
        y += xs[xi * 4 + 3] * (x - xp[xi]) ** 3
        return y

    @staticmethod
    def prepSplines(xp, yp):
        n = len(xp) - 1
        N = n * 4
        h = abs(xp[1] - xp[0])
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
        equationSolver = EquationSolver(M, b, N)
        xs = equationSolver.Solve()
        return xs
