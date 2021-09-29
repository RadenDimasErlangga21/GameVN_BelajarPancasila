

define rdn = Character("Raden")
define tgr = Character("Tegar")
define ash = Character("Penjaga Cafe")
define narator = Character("Tutorial")
define dsn = Character("Dosen")
define sol = Character("Soal")

label start:
    $ nilai = 0
    scene building
    play music "acnh_visitorarrive.mp3"
    "selamat datang di game : Mari Belajar Pancasila"
    "game ini adalah projek tugas akhir mata kuliah pancasila ber-genre visual novel yang membahas mengenai materi pancasila " 
    "game ini berbasis dialog dan pilihan, opsi pilihan yang di pilih akan menentukan akhir cerita dari game ini"
    narator "klik 1 kali setiap selesai membaca, untuk melanjutkan dialog"
    narator "pemain juga bisa mengaktifkan mode auto play, dimana dialog akan melanjutkan ke dialog selanjutnya secara automatis"
    narator "pemain juga bisa menggunakan fitur save dan load yang terdapat pada game ini"
    narator "selamat bermain game "
    stop music
    scene classroom with fade
    play music"acnh_2pm.mp3"
    "jam 9:00 hari rabu di gedung kuliah"
    show raden2 
    rdn "Halo selamat pagi"
    hide raden2 
    show tegar at right 
    tgr "Halo selamat pagi, aku baru saja selesai sarapan"
    show raden2 
    rdn "aku disini tidak bermaksud untuk minta bekal mu sih..."
    show tegar at right 
    tgr "oh maaf, ada apa?"
    hide tegar
    rdn "nanti ada rencana untuk belajar materi bersama nggak? dikarenakan besok ada ulangan pancasila"
    hide raden2 
    show tegar 
    tgr "boleh, aku juga lagi bingung dengan materi pancasila, dan besok juga ada ulangan, jadi seperti nya itu ide yang bagus"
    hide tegar 
    show raden2 
    rdn "oke, selesai kuliah kita ke kafe buku seperti biasa nya ya, kita belajar sambil menikmati coklat hangat"
    hide raden2 
    show tegar 
    tgr "wahhh oke, jam berapa kalau boleh tau?"
    hide tegar 
    show raden2 
    rdn "2 jam setelah mata kuliah hari rabu"
    hide raden2
    show tegar 
    tgr "oke berarti jam 7 ya?"
    hide tegar
    show raden2
    rdn "yup, nanti jam 7 kita ke cafe buku itu, jangan lupa bawa buku catatan pancasila ya!"
    hide raden2
    show tegar
    tgr "oke siap..."
    hide tegar
    pause
    "mereka pun setuju untuk berdiskusi mengenai materi pancasila"
    stop music
    scene cafe with fade 
    "jam 7:24 di cafe buku"
    play music "acnh_9pm.mp3"
    show penjagacafe1
    ash "halo selamat datang di cafe buku, ada yang bisa di bantu?"
    hide penjagacafe1
    show raden2
    rdn "aku disini ingin memesan 2 coklat panas"
    hide raden2
    show tegar2 with vpunch
    tgr "halo, wah kamu ternyata baru memesan, aku kira aku telat hahaha"
    hide tegar2 
    show raden with zoomin
    rdn "tidak masalah, aku sudah memesan 2 coklat panas"
    hide raden 
    show penjagacafe3
    ash "baik pesanaan sudah siap"
    "mereka pun mencari tempat duduk dan siap untuk belajar"
    hide penjagacafe3 
    show raden2 
    rdn "baik kita akan memulai pembelajaran nya"
    hide raden2
    show cafe with fade 
    "mereka pun belajar"
    ".............."
    "......................"
    "waktu sudah berlalu selama 1 jam"
    show tegar2 
    tgr "baik ini waktu nya sesi tanya jawab"
    hide tegar2
    show raden
    rdn "aku rasa aku belum cukup siap, tapi ayo kita akan memulai latihan nya"
    hide raden
    show tegar2
    tgr "baik materi pertama adalah, mengenai pancasila sebagai ideologi indonesia"
    tgr "apakah bentuk awal pancasila? "

    menu: 
       "pilih jawaban :"
       "A.Pancasila berupa gagasan dasar negara dari Ir.Soekarno dan disempurnakan oleh panitia 9": 
               jump opsiA
       "B. Pancasila berupa gagasan dasar negara dari Ir.Soekarno dan disempurnakan oleh panitia BPUPKI": 
               jump opsiB
       "C. Pancasila berupa gagasan dasar negara dari Bj.Habibie dan disempurnakan oleh panitia 9": 
               jump opsiC

    label opsiA :
            tgr "yap benar sekali, pancasila awalnya berupa gagasan dasar negara dari Ir Soekarno dan di sempurnakan oleh panitia 9"
            tgr "hasil dari penyempurnaan tersebut adalah piagam jakarta, yang kemudian di sahkan oleh PPKI"
            tgr "dengan tujuan pancasila sebagai dasar negara"
            jump dialog_cafe
    label opsiB :
            tgr "jawaban salah, pancasila awalnya berupa gagasan dasar negara dari Ir Soekarno dan di sempurnakan oleh pantia 9"
            tgr "hasil dari penyempurnaan tersebut adalah piagam jakarta, yang kemudian di sahkan oleh PPKI"
            tgr "dengan tujuan pancasila sebagai dasar negara"
            jump dialog_cafe 
    label opsiC :
            tgr "jawaban salah, pancasila awalnya berupa gagasan dasar negara dari Ir Soekarno dan di sempurnakan oleh pantia 9"
            tgr "hasil dari penyempurnaan tersebut adalah piagam jakarta, yang kemudian di sahkan oleh PPKI"
            tgr "dengan tujuan pancasila sebagai dasar negara"
            jump dialog_cafe 
    label dialog_cafe : 
    hide tegar2
    show raden 
    rdn "terima kasih penjelasan nya, soal nya tadi sedikit menjebak"
    hide raden
    show tegar2
    tgr "aku memang sengaja melakukan hal itu hehe..."
    hide tegar2
    show raden  
    rdn "........"
    hide raden
    show tegar2 
    tgr "baik pertanyaan ke 2"
    tgr "sebutkan simbol-simbol yang ada pada garuda pancasila"
    menu:
       "pilih jawaban :"
       "A.ada 5 yaitu Bintang, Rantai, Pohon Beringin, Kepala Banteng, Padi dan Kapas": 
               jump opsA
       "B.ada 6 yaitu Perisai, Bintang, Rantai, Pohon Beringin, Kepala Banteng, Padi dan Kapas": 
               jump opsB
       "C.ada 4 yaitu Bintang, Pohon Beringin, Padi dan Kapas, Kepala Banteng": 
               jump opsC
    label opsA :
            tgr "yap benar sekali, bintang memiliki arti ketuhanan yang maha esa, layak nya tuhan yang menjadi cahaya setiap manusia"
            tgr "Rantai, berarti Kemanusiaan yang adil dan beadab, hubungan manusia yang saling membantu satu sama lain, bentuk rantai sendiri ada dua yaitu persegi dan lingkaran"
            tgr "persegi menggambar kan laki-laki dan lingkaran menggambarkan perempuan"
            tgr "Pohon Beringin, persatuan indonesia, pohon berinin bermakna kesatuan dan persatuan, akar yang menggantung pada pohon beringin menggambarkan berbagai macam latar belakang manusia yang berbeda-beda"
            tgr "kepala banteng, kerakyatan yang di pimpin oleh hikmat kebijaksanaan dalam permusyawaratan atau perwakilan, banteng sendiri merupakan binatang yang suka berkumpul"
            tgr "jadi banteng melambangkan kebersamaan itu sendiri, lalu kepala banteng melambangkan tentang musyawarah dalam menggambil keputusan bersama"
            tgr "dan terakhir adalah padi dan kapas, keadilan sosial bagi seluruh rakyat indonesia."
            tgr "padi dan kapas melambangkan kesejahteraan."
            jump belajar_cafe
    label opsB :
            tgr "yap salah... yang benar ada 5. bintang memiliki arti ketuhanan yang maha esa, layak nya tuhan yang menjadi cahaya setiap manusia"
            tgr "Rantai, berarti Kemanusiaan yang adil dan beadab, hubungan manusia yang saling membantu satu sama lain, bentuk rantai sendiri ada dua yaitu persegi dan lingkaran"
            tgr "persegi menggambar kan laki-laki dan lingkaran menggambarkan perempuan"
            tgr "Pohon Beringin, persatuan indonesia, pohon berinin bermakna kesatuan dan persatuan, akar yang menggantung pada pohon beringin menggambarkan berbagai macam latar belakang manusia yang berbeda-beda"
            tgr "kepala banteng, kerakyatan yang di pimpin oleh hikmat kebijaksanaan dalam permusyawaratan atau perwakilan, banteng sendiri merupakan binatang yang suka berkumpul"
            tgr "jadi banteng melambangkan kebersamaan itu sendiri, lalu kepala banteng melambangkan tentang musyawarah dalam menggambil keputusan bersama"
            tgr "dan terakhir adalah padi dan kapas, keadilan sosial bagi seluruh rakyat indonesia."
            tgr "padi dan kapas melambangkan kesejahteraan."
            jump belajar_cafe 
    label opsC :
            tgr "hmm apakah kamu bercanda? salah, yang benar ada 5. bintang memiliki arti ketuhanan yang maha esa, layak nya tuhan yang menjadi cahaya setiap manusia"
            tgr "Rantai, berarti Kemanusiaan yang adil dan beadab, hubungan manusia yang saling membantu satu sama lain, bentuk rantai sendiri ada dua yaitu persegi dan lingkaran"
            tgr "persegi menggambar kan laki-laki dan lingkaran menggambarkan perempuan"
            tgr "Pohon Beringin, persatuan indonesia, pohon berinin bermakna kesatuan dan persatuan, akar yang menggantung pada pohon beringin menggambarkan berbagai macam latar belakang manusia yang berbeda-beda"
            tgr "kepala banteng, kerakyatan yang di pimpin oleh hikmat kebijaksanaan dalam permusyawaratan atau perwakilan, banteng sendiri merupakan binatang yang suka berkumpul"
            tgr "jadi banteng melambangkan kebersamaan itu sendiri, lalu kepala banteng melambangkan tentang musyawarah dalam menggambil keputusan bersama"
            tgr "dan terakhir adalah padi dan kapas, keadilan sosial bagi seluruh rakyat indonesia."
            tgr "padi dan kapas melambangkan kesejahteraan."
            jump belajar_cafe 
    label belajar_cafe :
    hide tegar2
    show raden 
    rdn "baiklah seperti nya aku sudah paham"
    rdn "dari materi yang kubaca, pancasila terdapat dalam pembukaan UUD 1945 dan secara resmi telah disahkan oleh PPKI pada tanggal 18 agustus 1945 sebagai dasar negarai Republik indonesia"
    rdn "pancasila sendiri berdasarkan 5 moral principle dari agama buddha, yaitu dilarang membunuh, mabuk-mabuk an, berbuat zina, berbohong, dan mencuri"
    rdn "lalu selain itu, materi mengenai lambang-lambang tadi"
    rdn "bulu garuda juga memiliki makna setiap jumlah nya"
    hide raden
    show tegar2
    tgr "wah apa saja itu?"
    hide tegar2
    show raden
    rdn "17 helai bulu sayap itu arti nya tanggal 17, 8 helai bulu ekor arti nya bulan 8, lalu 19 helai bulu pangkal ekor arti nya tahun"
    rdn "dan terakhir.... 45 helai bulu di leher itu juga diartikan sebagai tahun 45"
    rdn "jadi pada jumlah bulu pada lambang garuda itu memiliki angka yang ketika di susun menjadi..."
    hide raden 
    show raden with vpunch 
    rdn "17 AGUSTUS TAHUN 1945"
    hide raden
    show tegar2
    tgr "hmmm menarik, tidak kusangka se-detail itu"
    hide tegar2
    "mereka pun belajar sampai larut..."
    stop music
    scene building with fade
    "hari ujian telah tiba"
    "persiapkan semua materi yang anda pelajari tadi malam"
    "semoga beruntung!"
    scene classroom with fade 
    play music "acnh_12pm.mp3"
    show raden2
    rdn "semoga saja aku lolos test ini, aku akan belajar lagi terlebih dahulu"
    "......"
    ".........."
    hide raden2
    show dosen
    dsn "baik semua nya, pada pertemuan ini kita akan melakukan ujian kuis 1, dengan materi pancasila dasar"
    dsn "oke, saya akan bacakan ketentuan kuis kali ini"
    dsn "pertama tidak boleh mencontek" with vpunch
    dsn "kedua jawaban benar atau tidak akan di tampilkan saat kalian telah memilih jawaban"
    dsn "nilai akan di tampilkan saat ujian selesai" 
    hide dosen
    show raden2
    rdn "(berbicara dalam hati) oke, aku harus tenang seperti nya aku sudah menguasai materi ini"
    hide raden2
    sol "soal ke 1"
    sol "apakah lambang pancasila pada sila ke-3"
    menu: 
      "A. Padi & Kapas":
         "jawaban salah"

      "B. Rantai":
         "jawaban salah"

      "C. Bintang":
         "jawaban salah"

      "D. Kepala Banteng":
         "jawaban salah"

      "E. Pohon Beringin":
         $ nilai += 1
         "jawaban benar"

    sol "soal ke 2"
    sol "persatuan indonesia adalah isi dari pancasila, sila ke?"
    menu: 
      "A. 1":
         "jawaban salah"

      "B. 2":
         "jawaban salah"

      "C. 3":
         $ nilai += 1
         "jawaban benar"

      "D. 4":
         "jawaban salah"

      "E. 5":
         "jawaban salah"

    sol "soal ke 3"
    sol "bentuk rumusan dari sila-sila Pancasila Bersifat Abstrak. Hal itu karena Pancasila Berupa.."
    menu: 
      "A. Benda":
         "jawaban salah"

      "B. Materi":
         "jawaban salah"

      "C. Nilai":
         $ nilai += 1
         "jawaban benar"

      "D. Psikis":
         "jawaban salah"

      "E. Makluk Hidup":
         "jawaban salah"

    sol "soal ke 4"
    sol "Ideologi secara struktural diartikan sebagai sistem..."
    menu:
      "A. dasar":
         $ nilai += 1
         "jawaban benar"

      "B. Pembenaran":
         "jawaban salah"
 
      "C. Politik":
         "jawaban salah"

      "D. Kekuatan":
         "jawaban salah"

      "E. Strategi":
         "jawaban salah"

    sol "soal ke 5"
    sol "dasar negara pancasila dapat mempersatukan bangsa indonesia yang terdiri dari banyak suku agama, dan adat istiadat atau kebudayaan. dalam hal ini pancasila berfungsi sebagai ?"
    menu:
      "A. pembentuk solidaritas":
         $ nilai += 1
         "jawaban benar"

      "B. identitas bangsa":
         "jawaban salah"

      "C. sumber hukum":
         "jawaban salah"

      "D. Kekuatan":
         "jawaban salah"

      "E. sumber nilai":
         "jawaban salah"

    sol "soal ke 6"
    sol "Kehidupan sosial yang suka berkumpul dan berdiskusi untuk mendapatkan suatu keputusan adalah arti lambang pancasila sila ke-"
    menu:
      "A. Satu":
         "jawaban salah"

      "B. Dua":
         "jawaban salah"

      "C. Tiga":
         "jawaban salah"

      "D. Empat":
         "jawaban salah"

      "E. Lima":
         $ nilai += 1
         "jawaban benar"

    sol "soal 7"
    sol "Hidup berdampingan dan saling berkaitan antara laki-laki dengan perempuan adalah arti dari lambang sila pancasila.."
    menu:
      "A. Padi dan Kapas":
         "jawaban salah"

      "B. Pohon Beringin":
         "jawaban salah"

      "C. Bintang":
         "jawaban salah"

      "D. Banteng":
         "jawaban salah"

      "E. Rantai Emas":
         $ nilai += 1
         "jawaban benar"

    sol "soal ke 8"
    sol "berikut ini yang merupakan ciri khas demokrasi pancasila adalah : "
    menu:
      "A. pemerintah mempunyai kekuasaan yang tidak terbatas":
         "jawaban salah"

      "B. Memberi arti yanng kuat terhadap manusia pribadi":
         "jawaban salah"

      "C. Pemerintah merupakan kekuasaan yang terbatas dan tidak sewenang wenang":
         "jawaban salah"

      "D. Menekankan kepada keselarasan, keseimbangan, dan keserasian antara individu dan masyarakat":
         $ nilai +=1
         "jawaban benar"

      "E. Pemerintah memberikan arti hidup secara damai":
         "jawaban salah"
    sol "soal ke 9"
    sol "Melaksanakan peraturan perundang-undangan bernafaskan pancasila berarti :"
    menu:
      "A. mengamalkan pancasila secara subjektif":
         "jawaban salah"

      "B. mengamalkan pancasila secara teoritis":
         "jawaban salah"

      "C. mengamalkan pancasila secara objektif":
         $ nilai +=1
         "jawaban benar"

      "D. mengamalkan pancasila secara praktis":
         "jawaban salah"

      "E. mengamalkan pancasila secara sekularisme":
         "jawaban salah"
    sol "soal ke 10"
    sol "Mengamalkan Pancasila untuk mengatur penyelenggaraan pemerintahan negara Republik Indonesia, merupakan pengamalan pancasila sebagai :"
    menu:
      "A. dasar negara":
         $ nilai +=1
         "jawaban benar"

      "B. cita-cita dan tujuan bangsa indonesia":
         "jawaban salah"

      "C. falsafah bangsa indonesia":
         "jawaban benar"

      "D. pedoman hidup manusia":
         "jawaban salah"

      "E. sumber dari ketertiban hukum":
         "jawaban salah"
    show dosen 
    dsn "baik, semua nya waktu sudah habis silahkan cek nilai masing-masing ya"
    hide dosen 
    show tegar2 
    tgr "wahhh, ternyata materi yang kita pelajari kurang cukup aku dapat 70"
    rdn "sebentar... aku belum mengecek nilai ku....."
    if nilai == 10:
      "selamat kamu mendapatkan nilai A dengan benar 10"
      show tegar2
      tgr "mustahil, kamu belajar apa semalam"
      hide tegar2
      show raden2
      rdn "materi yang sama, namun menggunakan logika untuk menjawab soal nya"
      hide raden2
      jump akhir 
    if nilai == 9:
      "selamat kamu mendapatkan nilai A dengan benar 9"
      show tegar2
      hide tegar2
      show raden2
      tgr "mustahil, kamu belajar apa semalam"
      rdn "materi yang sama, namun menggunakan logika untuk menjawab soal nya"
      hide raden2
      jump akhir 
    if nilai == 8:
      "selamat kamu mendapatkan nilai B+ dengan benar 8"
      show tegar2
      tgr "mustahil, kamu belajar apa semalam"
      hide tegar2
      show raden2
      rdn "materi yang sama, namun menggunakan logika untuk menjawab soal nya"
      hide raden2
      jump akhir
    if nilai == 7:
      "selamat kamu mendapatkan nilai B dengan benar 7"
      show tegar2
      tgr "nilai kita sama...."
      hide tegar2
      show raden2
      rdn "T-tapi aku tidak mencontek lhoo"
      hide raden2
      jump akhir
    if nilai == 6:
      "kamu mendapatkan nilai C dengan benar 6, lebih giat belajar lagi ya"
      show tegar2
      tgr "tidak apa-apa kawan, lain kali belajar lebih giat lagi"
      hide tegar2
      show raden2
      rdn "baik lah..."
      hide raden2
      jump akhir
    if nilai == 5:
      "kamu mendapatkan nilai D dengan benar 5, harus lebih giat belajar lagi ya"
      show tegar2
      tgr "...... aku tidak bisa berkomentar"
      hide tegar2
      show raden2
      rdn "................. aku juga"
      hide raden2
      jump akhir
    if nilai == 4:
      "kamu mendapatkan nilai E dengan benar 4, Silahkan lakukan remidi"
      show tegar2
      tgr "apakah kamu melamun?"
      hide tegar2
      show raden2
      rdn "seperti nya ada masalah pada komputer ku saat ujian"
      hide raden2
      jump akhir
    if nilai == 3:
      "kamu mendapatkan nilai E dengan benar 3, Silahkan lakukan remidi"
      show tegar2
      tgr "....."
      hide tegar2
      show raden2
      rdn "..... yang salah soal nya ini"
      hide raden2
      jump akhir
    if nilai == 2:
      "kamu mendapatkan nilai F dengan benar 2, Silahkan lakukan remidi"
      show tegar2
      tgr "wah kamu mendapat kan F"
      hide tegar2
      show raden2
      rdn "oh tidak...."
      hide raden2
      jump akhir
    if nilai == 1:
      "kamu mendapatkan nilai F dengan benar 1, Silahkan lakukan remidi"
      show tegar2
      tgr "wah kamu mendapat kan F"
      hide tegar2
      show raden2
      rdn "oh tidak...."
      hide raden2
      jump akhir
    if nilai == 0:
      "kamu mendapatkan nilai F dengan benar 0, Silahkan lakukan remidi"
      show tegar2
      tgr "seperti nya komputer kamu memiliki masalah sehingga output nya adalah 0"
      hide tegar2
      show raden2
      rdn "................."
      hide raden2
      jump akhir
    label akhir:
    show dosen
    dsn "baik semua nya, jika ada nilai yang bermasalah segera hubungi saya secepat mungkin, saya akan menyuruh kalian untuk membuat resume mengenai materi pancasila"
    dsn "baik perkuliahan saya akhiri, terima kasih sudah hadir semua nya"
    hide dosen
    "game sudah berakhir, apakah ingin mengulang game dari awal?"
    menu:
     "Ya":
      jump start
     "Tidak":
      "Terimakasih sudah bermain"
      "programmer : Raden Dimas Erlangga"
      "Penulis    : Raden Dimas Erlangga, Tegar Dwi Vantoro"
      "Penulis Soal : Wendha Aldafa Putra Heranusa, Reihan Amru, Raviansyah Yudistira Pratama, Siwi Tyas P"
      "kelompok 7 : Raden Dimas Erlangga, Raviansyah Yudistira Pratama, Reihan Amru"
      "kelompok 8 : Siwi Tyas P, Tegar Dwi Vantoro, Wendha Aldafa Putra Heranusa" 
    return