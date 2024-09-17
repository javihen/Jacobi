import numpy as np

A= np.array([[3, -0.1, -0.2],
            [0.1, 7, -0.3],
            [0.3, -8.2, 10]])

b=np.array([7.85, 19.3, 71.43])

x= np.zeros_like(b)
n_iteraciones = 10
tolerancia = 0.001 

print("Resultados de cada Iteración:")
for iteracion in range(n_iteraciones):
  x_old = x.copy()
  for i in range(len(b)):
    sigma = sum(A[i][j] * x[j] for j in range(len(b)) if j != i)
    x[i]=(b[i]-sigma)/A[i][i]
    
    print(f"Iteracion {iteracion + 1}: {x}")
    if np.linalg.norm(x-x_old,ord=np.inf) < tolerancia:
       print(f"convergio en {iteracion + 1} iteraciones.")
       break

print("Soluciones finales:")
print(x)
