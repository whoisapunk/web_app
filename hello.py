from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('test message')
    return '<h1>Hello, YoYoYo_!!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


def mean(numbers):
    return  sum(numbers) / len(numbers) 


@app.route('/avg/<nums>')
def avg(nums):
    nums = nums.split(',')
    nums =[int(num) for num in nums]
    nums_mean = mean(nums)
    print(nums_mean)
    return str(nums_mean)

@app.route('/iris/<param>')
def iris(param):

    param =param.split(',')
    param =[float(num) for num in param]

    import numpy as np 
    from sklearn import datasets
    iris = datasets.load_iris()
    iris_X = iris.data 
    iris_y = iris.target
    np.unique(iris_y)

    np.random.seed()
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)
    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
    weights='uniform')
    knn.predict(iris_X_test)

    param = np.array(param).reshape(1,-1)

    predict  = knn.predict(param)


    return str(predict)