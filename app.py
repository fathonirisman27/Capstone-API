from flask import Flask, request 
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/employees')
def employe():
    conn = sqlite3.connect("data/chinook.db")
    query = """ 
    SELECT * FROM employees
    """
    data = pd.read_sql_query(query,conn)
    return data.to_json()

#showing all genres and track
@app.route('/genre')
def genre():
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT tracks.Name as Judul, genres.name as genre
    FROM tracks
    JOIN genres ON genres.genreid = tracks.genreid
    """
    data = pd.read_sql_query(query,conn)
    return data.to_json()

#dynamic genre, showing all tracks in genre by request genre name
@app.route('/genre/<name>')
def genre_dynamic(name):
    conn  = sqlite3.connect("data/chinook.db")
    query = """
    SELECT tracks.Name as Judul, genres.name as genre
    FROM tracks
    JOIN genres ON genres.genreid = tracks.genreid
    """
    data = pd.read_sql_query(query, conn)
    author = name
    kondisi = data['genre'] == author
    data = data[kondisi]
    return data.to_json()

@app.route('/', methods=['POST'])
def homepage():
    return "welcomeeee"

# mendapatkan buku 
@app.route('/ambil_buku')
def ambilbuku():
    data = pd.read_csv('data/books_c.csv')
    return data.to_json() # atau integer, atau string

# buat endpoint yang menghasilkan hasil crosstabulasi dari data books_c.csv
@app.route('/top_rating_book')
def topratingbook():
    books = pd.read_csv('data/books_c.csv')
    condition  = books['average_rating'] == 5
    books = books[condition]
    return books.to_json()

@app.route('/get_author/<name>')
def getauthor(name):
    author = name
    books = pd.read_csv('data/books_c.csv')
    condition = books['authors'] == author
    books = books[condition]
    return books.to_json()


# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())
 

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 