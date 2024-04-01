from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    assets = cursor.fetchall()
    conn.close()
    return render_template('inventory.html', assets=assets)

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        asset_name = request.form['asset_name']
        serial_number = request.form['serial_number']
        category = request.form['category']
        location = request.form['location']
        status = request.form['status']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO assets (asset_name, serial_number, category, location, status) VALUES (%s, %s, %s, %s, %s)",
                       (asset_name, serial_number, category, location, status))
        conn.commit()
        conn.close()
        return redirect(url_for('inventory'))

    return render_template('add_asset.html')

@app.route('/edit_asset/<int:asset_id>', methods=['GET', 'POST'])
def edit_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets WHERE id = %s", (asset_id,))
    asset = cursor.fetchone()

    if request.method == 'POST':
        asset_name = request.form['asset_name']
        serial_number = request.form['serial_number']
        category = request.form['category']
        location = request.form['location']
        status = request.form['status']

        cursor.execute("UPDATE assets SET asset_name=%s, serial_number=%s, category=%s, location=%s, status=%s WHERE id=%s",
                        (asset_name, serial_number, category, location, status, asset_id))
        conn.commit()
        conn.close()
        return redirect(url_for('inventory'))

    conn.close()
    return render_template('edit_asset.html', asset=asset)

@app.route('/delete_asset/<int:asset_id>', methods=['POST'])
def delete_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assets WHERE id = %s", (asset_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('inventory'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assets WHERE asset_name LIKE %s", ('%' + search_term + '%',))
        assets = cursor.fetchall()
        conn.close()
        return render_template('search_results.html', assets=assets)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
