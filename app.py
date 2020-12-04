from flask import Flask, request 
import pandas as pd
import sqlite3

app = Flask(__name__)

#showing table that contains genres,track,albums,artist (static)
@app.route('/artist')
def artist():
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT artists.Name as Artist, albums.Title as albums, tracks.Name as Track, genres.Name as genre
    FROM artists
    LEFT JOIN albums
    ON artists.ArtistId = albums.ArtistId
    LEFT JOIN tracks
    ON albums.AlbumId = tracks.AlbumID 
    LEFT JOIN genres
    ON tracks.GenreID = genres.GenreId
    """
    data = pd.read_sql_query(query,conn)
    data = data.dropna()
    return data.to_json()

#Showing a table that contain how many album and tracks in spesific artist with a spesific genre
@app.route('/genre/artist/count_albums_and_track')
def hitungtrackalbum ():
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT artists.Name as Artist, albums.Title as albums, tracks.Name as Track, genres.Name as genre
    FROM artists
    LEFT JOIN albums
    ON artists.ArtistId = albums.ArtistId
    LEFT JOIN tracks
    ON albums.AlbumId = tracks.AlbumID 
    LEFT JOIN genres
    ON tracks.GenreID = genres.GenreId
    """
    data = pd.read_sql_query(query, conn)
    data = data.dropna()
    data_gb = data.groupby(['genre','Artist']).count()
    data_ut = data_gb.unstack(1) #using genre as index, so we use level = 1
    data_ut_complete = data_ut.fillna(0) #replace NaN with 0 because of in that genres and track, there is no albums or track
    return data_ut_complete.to_json()


#showing all tracks in genre by request genre name (dynamic)
@app.route('/get_genre/<name>')
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

 #Top 10 genre paling populer (based on most frequency) (static)
@app.route('/Genre/Populer/TOP10')
def top_genre():
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT tracks.Name as Judul, genres.name as genre
    FROM tracks
    JOIN genres ON genres.genreid = tracks.genreid
    """
    data = pd.read_sql_query(query,conn)
    top10_genre = pd.crosstab(
                   index = data['genre'],
                   columns = 'Total'
                   ).sort_values('Total',ascending=False).head(10)
    return top10_genre.to_json()


# Track populer (top 10) berdasarkan bulan (purchased by month)-dynamic
@app.route('/Track/Populer/<month>')
def track(month):
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT invoices.InvoiceDate, tracks.Name as Judul
    FROM invoices 
    LEFT JOIN invoice_items 
    ON invoices.InvoiceID = invoice_items.InvoiceID
    LEFT JOIN tracks 
    ON tracks.TrackId = invoice_items.TrackId 
    """
    df = pd.read_sql_query(query,con = conn , parse_dates='InvoiceDate')
    df['Bulan'] = df['InvoiceDate'].dt.month_name()
    bulan = month
    condition = df['Bulan'] == bulan
    data = df[condition]
    data_new = pd.crosstab(
                index = data['Judul'],
                columns= 'Total'
                ).sort_values('Total',ascending=False).head(10)
    return data_new.to_json()
     





if __name__ == '__main__':
    app.run(debug=True, port=5000) 