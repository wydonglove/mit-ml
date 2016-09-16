import regression
import matplotlib.pyplot as plt

if __name__ == "__main__":
    X, y = regression.loadDataSet('data/ex0.txt');

    rate = 0.01
    maxLoop = 1000
    epsilon = 0.005

    result, timeConsumed = regression.bgd(rate, maxLoop, epsilon, X, y)
    theta,error,iterationCount = result

    fig = plt.figure()
    title = 'bgd: rate=%.2f, maxLoop=%d, epsilon=%.3f \n time: %ds'%(rate,maxLoop,epsilon,timeConsumed)
    ax = fig.add_subplot(111, title=title, )
    ax.scatter(X[:, 1].flatten().A[0], y[:,0].flatten().A[0])

    xCopy = X.copy()
    xCopy.sort(0)
    yHat = xCopy*theta
    ax.plot(xCopy[:,1], yHat)
    plt.show()

