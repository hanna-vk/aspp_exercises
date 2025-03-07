import numpy as np

def mat_mult(N):
    # Generate random matrices
    X = np.random.randint(0, 100, (N, N))
    Y = np.random.randint(0, 100, (N, N + 1))
    
    # Matrix multiplication
    result = np.dot(X, Y)
    return result

N = 250
result = mat_mult(N)
print(result)