from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses', methods=['GET', 'POST'])
def manage_expenses():
    if request.method == 'GET':
        return jsonify(expenses)
    elif request.method == 'POST':
        data = request.json
        expenses.append(data)
        return jsonify({
            'message': 'Expense added.'
        })

@app.route('/expenses/<int:expense_id>', methods=['GET','PUT','DELETE'])
def manage_expense(expense_id):
    if request.method == 'GET':
        if expense_id < len(expenses):
            return jsonify(expenses[expense_id])
        else:
            return jsonify({
                'message':'Expense not found'
            }), 404
    elif request.method == 'PUT':
        data = request.json
        expenses[expense_id] = data
        return jsonify({
            'message': 'Expense updated.'
        })
    elif request.method == 'DELETE':
        if expense_id < len(expenses):
            del expenses[expense_id]
            return jsonify({
                'message': 'Expense deleted.'
            })
        else:
            return jsonify({
                'message': 'Expense not found'
            }), 404

if __name__ == "__main__":
    app.run(debug=True)
