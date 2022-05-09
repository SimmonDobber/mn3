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





