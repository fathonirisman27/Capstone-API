# Capstone-api
Ini adalah projek dalam rangka membuat Web API menggunakan python flask. API dibutuhkan untuk menghubungkan antara user (pihak 3) dengan database yang saya miliki. Dalam hal ini saya menggunakan database bernama chinook.db. Database ini berisikan tabel-tabel diantaranya : genre,album,track,invoice,dsb. Adapun skema hubungan antara masing-masing tabel saya lampirkan dalam folder data.

Dalam Web ini saya membuat 4 endpoints, (2 statis dan 2 dynamic), berikut diantaranya : 
1. ('/artist') , return dalam format JSON berupa tabel yang berisikan kolom genre,track,album dan artist (endpoint statis)
2. ('/get_genre/<name>'), return dalam format JSON berupa semua track yang terkandung dalam genre <name>. (endpoint dinamis)
3. ('/Genre/Populer/TOP10'), return dalam format JSON berupa genre populer (berdasarkan total kemunculan)
4. ('/Track/Populer/<month>'), return dalam format JSON berupa Top 10 Track populer (berdasarkan total yang sering dibeli) dalam tiap bulan. Disini nama bulan saya jadikan dynamic.

___


If you want to try it, you can access (copy-paste it) : 
- https://algo-capstone.herokuapp.com
- https://algo-capstone.herokuapp.com/data/get/books_c.csv
- https://algo-capstone.herokuapp.com/data/get/pulsar_stars.csv
- https://algo-capstone.herokuapp.com/data/get/equal/books_c.csv/isbn/0439785960
- https://algo-capstone.herokuapp.com/data/get/equal/books_c.csv/authors/J.K. Rowling
- and so on, just follow the endpoint's pattern
