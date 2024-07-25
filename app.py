from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_divisibility():
    number = int(request.form['number'])
    divisors = find_divisors(number)
    return render_template('result.html', number=number, divisors=divisors)

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    app.run(debug=True)
