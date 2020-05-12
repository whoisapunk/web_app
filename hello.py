from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('test message')
    return '<h1>Hello, YoYoYo!</h1>'

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