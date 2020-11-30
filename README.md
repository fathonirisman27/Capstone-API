# Capstone Web- API
Ini adalah projek dalam rangka membuat Web API menggunakan python flask. API dibutuhkan untuk menghubungkan antara user (pihak 3) dengan database yang saya miliki. Dalam hal ini saya menggunakan database bernama chinook.db. Database ini berisikan kumpulan dari tabel-tabel, yang diantaranya : genre, album, track, invoice, dsb. Adapun skema hubungan antara masing-masing tabel saya lampirkan dalam folder data.

Dalam Web ini saya membuat 4 endpoints, (2 statis dan 2 dynamic), berikut diantaranya :
1. ('/artist') , return dalam format JSON berupa tabel yang berisikan kolom genre,track,album dan artist (endpoint statis)
2. ('/get_genre/<nama_genre>'), return dalam format JSON berupa semua track yang terkandung dalam genre . (endpoint dinamis)
3. ('/Genre/Populer/TOP10'), return dalam format JSON berupa genre populer (berdasarkan total kemunculan)
4. ('/Track/Populer/<nama_bulan>'), return dalam format JSON berupa Top 10 Track populer (berdasarkan total yang sering dibeli) di setiap bulan. (endpoint dinamis)

Jika kamu ingin mencobanya, kamu dapat mengakses lewat link di bawah ini : 
- https://fathonirisman27.herokuapp.com/artist 
- https://fathonirisman27.herokuapp.com/get_genre/<nama_genre>
- https://fathonirisman27.herokuapp.com/Genre/Populer/TOP10
- https://fathonirisman27.herokuapp.com/Track/Populer/<nama_bulan>
 
  
