import mlflow

def calcPower(x, n):
    return x**n

if __name__ == '__main__':
    with mlflow.start_run():
        x, n = 3, 6
        y = calcPower(x, n)
        mlflow.log_param("x", x)
        mlflow.log_param("n", n)
        mlflow.log_param("y", y)