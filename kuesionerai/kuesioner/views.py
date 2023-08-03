from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from datetime import datetime
from .models import Tb_test_kategori, Tb_answer, Tb_kategori_soal, Tb_soal_kepuasan_umum, Tb_soal_kepentingan, Tb_soal_kepuasan, m_position, m_location, user_data, UserResponse, UserResponse1, UserResponse2, m_gender, m_education, m_korsa, m_jenis_jabatan,count_user_umum,count_user_kepentingan,count_user_kepuasan,score_lvl_kepentingan,score_lvl_kepuasan,dimensi_kepentingan,dimensi_kepuasan,score_dimensi, tb_score_lvl, UserComment
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import SignUpForm, KuesionerForm,KepentinganForm,KepuasanForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from django.db.models import Count, Sum, F, ExpressionWrapper, IntegerField, Avg
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.db import models
from collections import Counter
import re

# contoh memasukkan data ke dalam model Tb_master_answer
# kat1 = Tb_test_kategori.objects.get(id=2)
# kat2 = Tb_test_kategori.objects.get(id=3)

# kategori = [
#     Tb_kategori_soal(id = 1,  kategori_soal = 'Tempat & Lingkungan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 2,  kategori_soal = 'Lingkungan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 3,  kategori_soal = 'Keterlibatan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 4,  kategori_soal = 'Kerjasama', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 5,  kategori_soal = 'Kepemimpinan & Management', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 6,  kategori_soal = 'Perbaikan Terus Menerus', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 7,  kategori_soal = 'Ketepatan dan kecepatan  informasi  mengenai:', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 8,  kategori_soal = 'Pelatihan /pengembangan pribadi  untuk meningkatkan:', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 9,  kategori_soal = 'Sistem penggajian dan tunjangan', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 10,  kategori_soal = 'Kinerja Perusahaan', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 11,  kategori_soal = 'Tempat & Lingkungan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 12,  kategori_soal = 'Lingkungan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 13,  kategori_soal = 'Keterlibatan Kerja', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 14,  kategori_soal = 'Kerjasama', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 15,  kategori_soal = 'Kepemimpinan & Management', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 16,  kategori_soal = 'Perbaikan Terus Menerus', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 17,  kategori_soal = 'Ketepatan dan kecepatan  informasi  mengenai:', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 18,  kategori_soal = 'Pelatihan /pengembangan pribadi  untuk meningkatkan:', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 19,  kategori_soal = 'Sistem penggajian dan tunjangan', pub_date=timezone.now()),
#     Tb_kategori_soal(id = 20,  kategori_soal = 'Kinerja Perusahaan', pub_date=timezone.now())]
# for q in kategori:
#     try:
#         q.save()
#     except IntegrityError:
#         # Handle the duplicate question here, e.g. print an error message
#         print(f"Question '{q.pertanyaan}' already exists in the database.")
# answer.save()

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the kuesioner index.")


# kat = Tb_test_kategori.objects.get(id=1)
# answer = [
#     Tb_soal_kepuasan_umum(id = 1, pertanyaan = 'Saya senang bekerja di PT. KAI', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 2, pertanyaan = 'Saya akan merekomendasikan PT. KAI kepada teman-teman atau saudara bila ada lowongan pekerjaan.', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 3, pertanyaan = 'Sistem/prosedur di PT. KAI cukup baik.', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 4, pertanyaan = 'Saya puas dengan lingkungan pekerjaan saya (misalnya : suasana, sarana fisik).', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 5, pertanyaan = 'Secara umum, saya puas dengan atasan langsung saya.', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 6, pertanyaan = 'Saya puas bekerjasama dengan  rekan sekerja.', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 7, pertanyaan = 'Saya  mendapatkan imbalan/gaji yang memadai.', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 8, pertanyaan = 'Saya puas dengan tunjangan perusahaan (misalnya,  bonus, pensiun, asuransi kesehatan dsb.).', pub_date=timezone.now()),
#     Tb_soal_kepuasan_umum(id = 9, pertanyaan = 'Saya puas dengan pekerjaan yang saya lakukan.', pub_date=timezone.now())]
# for q in answer:
#     try:
#         q.save()
#     except IntegrityError:
#         # Handle the duplicate question here, e.g. print an error message
#         print(f"Question '{q.pertanyaan}' already exists in the database.")

# kategori1 = Tb_kategori_soal.objects.get(id=1)
# kategori2 = Tb_kategori_soal.objects.get(id=2)
# kategori3 = Tb_kategori_soal.objects.get(id=3)
# kategori4 = Tb_kategori_soal.objects.get(id=4)
# kategori5 = Tb_kategori_soal.objects.get(id=5)
# kategori6 = Tb_kategori_soal.objects.get(id=6)
# kategori7 = Tb_kategori_soal.objects.get(id=7)
# kategori8 = Tb_kategori_soal.objects.get(id=8)
# kategori9 = Tb_kategori_soal.objects.get(id=9)
# kategori10 = Tb_kategori_soal.objects.get(id=10)

# answer1 = [
#     Tb_soal_kepentingan(id = 1, id_kat_soal = kategori1, pertanyaan = 'Perlengkapan Kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 2, id_kat_soal = kategori1, pertanyaan = 'Keselamatan kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 3, id_kat_soal = kategori1, pertanyaan = 'Kondisi fisik tempat kerja (mis. Kebersihan, suhu/AC, ruangan, penerangan)', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 4, id_kat_soal = kategori2, pertanyaan = 'Prosedur Kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 5, id_kat_soal = kategori2, pertanyaan = 'Penempatan karyawan berdasarkan keahlian dan kemampuanProsedur Kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 6, id_kat_soal = kategori2, pertanyaan = 'Struktur organisasi dan pembagian kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 7, id_kat_soal = kategori2, pertanyaan = 'Beban kerja yang memadai dan berimbang', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 8, id_kat_soal = kategori2, pertanyaan = 'Kesempatan untuk dipromosikan di perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 9, id_kat_soal = kategori2, pertanyaan = 'Adanya jam kerja yang Fleksibel', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 10, id_kat_soal = kategori2, pertanyaan = 'Disiplin dalam mematuhi jam kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 11, id_kat_soal = kategori3, pertanyaan = 'Turut berperan dalam menetapkan sasaran bagian/organisasi', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 12, id_kat_soal = kategori3, pertanyaan = 'Adanya kemungkinan bekerja secara mandiri dan diberi tanggungjawab penuh', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 13, id_kat_soal = kategori3, pertanyaan = 'Kesempatan berperan serta secara effektif dalam mencapai keberhasilan perusahaan/bagian', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 14, id_kat_soal = kategori3, pertanyaan = 'Terlibat dalam pembuatan  keputusan  yang berkaitan dengan pekerjaan Anda sendiri ', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 15, id_kat_soal = kategori4, pertanyaan = 'Suasana/Iklim Kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 16, id_kat_soal = kategori4, pertanyaan = 'Suasana/Iklim KerjaKerjasama dengan rekan sekerja di bagian Anda', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 17, id_kat_soal = kategori4, pertanyaan = 'Kerjasama dengan rekan dari bagian lain', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 18, id_kat_soal = kategori4, pertanyaan = 'Kritik yang membangun diterima dengan baik', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 19, id_kat_soal = kategori4, pertanyaan = 'Adanya kelompok kerja lintas bagian', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 20, id_kat_soal = kategori4, pertanyaan = 'Saling memahami dan menghargai tugas dan wewenang rekan kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 21, id_kat_soal = kategori5, pertanyaan = 'Keputusan pimpinan perusahaan dibuat berdasarkan data dan fakta', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 22, id_kat_soal = kategori5, pertanyaan = 'Keputusan atasan langsung  dibuat berdasarkan data dan fakta', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 23, id_kat_soal = kategori5, pertanyaan = 'Ketegasan pimpinan perusahaan dalam mengambil keputusan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 24, id_kat_soal = kategori5, pertanyaan = 'Ketegasan atasan langsung dalam mengambil keputusan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 25, id_kat_soal = kategori5, pertanyaan = 'Pendelegasian tugas dan tanggung jawab yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 26, id_kat_soal = kategori5, pertanyaan = 'Dukungan atasan langsung  dalam melaksanakan pekerjaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 27, id_kat_soal = kategori5, pertanyaan = 'Kesempatan berkomunikasi secara informal dan bebas dengan atasan langsung', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 28, id_kat_soal = kategori5, pertanyaan = 'Kesempatan berkomunikasi  secara informal dan bebas dengan pimpinan perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 29, id_kat_soal = kategori5, pertanyaan = 'Atasan langsung yang terbuka dan transparan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 30, id_kat_soal = kategori5, pertanyaan = 'Pimpinan perusahaan yang terbuka dan transparan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 31, id_kat_soal = kategori5, pertanyaan = 'Penilaian prestasi kerja dilakukan  secara  terbuka dan adil', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 32, id_kat_soal = kategori6, pertanyaan = 'Penghargaan  untuk  saran perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 33, id_kat_soal = kategori6, pertanyaan = 'Saran-saran   perbaikan dilaksanakan ', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 34, id_kat_soal = kategori6, pertanyaan = 'Masalah yang muncul  dilihat sebagai peluang untuk perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 35, id_kat_soal = kategori6, pertanyaan = 'Meluangkan  waktu untuk perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 36, id_kat_soal = kategori7, pertanyaan = 'Hal yang menentukan keberhasilan pekerjaan saya', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 37, id_kat_soal = kategori7, pertanyaan = 'Visi dan sasaran perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 38, id_kat_soal = kategori7, pertanyaan = 'Perubahan-perubahan penting dalam perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 39, id_kat_soal = kategori7, pertanyaan = 'Pencapaian sasaran bagian', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 40, id_kat_soal = kategori7, pertanyaan = 'Kepuasan pelanggan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 41, id_kat_soal = kategori8, pertanyaan = 'Ketrampilan teknis pekerjaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 42, id_kat_soal = kategori8, pertanyaan = 'Ketrampilan bersosialisasi', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 43, id_kat_soal = kategori8, pertanyaan = 'Karir dalam perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 44, id_kat_soal = kategori8, pertanyaan = 'Kemampuan melakukan pekerjaan lain di perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 45, id_kat_soal = kategori9, pertanyaan = 'Gaji yang berdasarkan prestasi kerja', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 46, id_kat_soal = kategori9, pertanyaan = 'Gaji yang berdasarkan lama kerja/senioritas', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 47, id_kat_soal = kategori9, pertanyaan = 'Bonus yang terkait Keuntungan perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 48, id_kat_soal = kategori9, pertanyaan = 'Pensiun dari perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 49, id_kat_soal = kategori9, pertanyaan = 'Fasilitas lain (makan siang, Kesehatan, transportasi)', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 50, id_kat_soal = kategori10, pertanyaan = 'Kualitas Produk dan pelayanannya', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 51, id_kat_soal = kategori10, pertanyaan = 'Selalu menepati janji  waktu pengiriman', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 52, id_kat_soal = kategori10, pertanyaan = 'Flexibilitas terhadap perubahan waktu pengiriman yang telah disepakati', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 53, id_kat_soal = kategori10, pertanyaan = 'Harga yang bersaing', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 54, id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang berorientasi pada pelanggan', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 55, id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang bonafide', pub_date=timezone.now()),
#     Tb_soal_kepentingan(id = 56, id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang  memperhatikan kesejahteraan karyawan', pub_date=timezone.now())]

# for q in answer1:
#     try:
#         q.save()
#     except IntegrityError:
#         # Handle the duplicate question here, e.g. print an error message
#         print(f"Question '{q.pertanyaan}' already exists in the database.")

# kategori11 = Tb_kategori_soal.objects.get(id=11)
# kategori12 = Tb_kategori_soal.objects.get(id=12)
# kategori13 = Tb_kategori_soal.objects.get(id=13)
# kategori14 = Tb_kategori_soal.objects.get(id=14)
# kategori15 = Tb_kategori_soal.objects.get(id=15)
# kategori16 = Tb_kategori_soal.objects.get(id=16)
# kategori17 = Tb_kategori_soal.objects.get(id=17)
# kategori18 = Tb_kategori_soal.objects.get(id=18)
# kategori19 = Tb_kategori_soal.objects.get(id=19)
# kategori20 = Tb_kategori_soal.objects.get(id=20)

# answer2 = [
#     Tb_soal_kepuasan(id = 1, id_kat_soal = kategori1, pertanyaan = 'Perlengkapan Kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 2, id_kat_soal = kategori1, pertanyaan = 'Keselamatan kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 3, id_kat_soal = kategori1, pertanyaan = 'Kondisi fisik tempat kerja (mis. Kebersihan, suhu/AC, ruangan, penerangan)', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 4, id_kat_soal = kategori2, pertanyaan = 'Prosedur Kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 5, id_kat_soal = kategori2, pertanyaan = 'Penempatan karyawan berdasarkan keahlian dan kemampuanProsedur Kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 6, id_kat_soal = kategori2, pertanyaan = 'Struktur organisasi dan pembagian kerja yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 7, id_kat_soal = kategori2, pertanyaan = 'Beban kerja yang memadai dan berimbang', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 8, id_kat_soal = kategori2, pertanyaan = 'Kesempatan untuk dipromosikan di perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 9, id_kat_soal = kategori2, pertanyaan = 'Adanya jam kerja yang Fleksibel', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 10,id_kat_soal = kategori2, pertanyaan = 'Disiplin dalam mematuhi jam kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 11,id_kat_soal = kategori3, pertanyaan = 'Turut berperan dalam menetapkan sasaran bagian/organisasi', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 12,id_kat_soal = kategori3, pertanyaan = 'Adanya kemungkinan bekerja secara mandiri dan diberi tanggungjawab penuh', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 13,id_kat_soal = kategori3, pertanyaan = 'Kesempatan berperan serta secara effektif dalam mencapai keberhasilan perusahaan/bagian', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 14,id_kat_soal = kategori3, pertanyaan = 'Terlibat dalam pembuatan  keputusan  yang berkaitan dengan pekerjaan Anda sendiri ', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 15,id_kat_soal = kategori4, pertanyaan = 'Suasana/Iklim Kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 16,id_kat_soal = kategori4, pertanyaan = 'Suasana/Iklim KerjaKerjasama dengan rekan sekerja di bagian Anda', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 17,id_kat_soal = kategori4, pertanyaan = 'Kerjasama dengan rekan dari bagian lain', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 18,id_kat_soal = kategori4, pertanyaan = 'Kritik yang membangun diterima dengan baik', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 19,id_kat_soal = kategori4, pertanyaan = 'Adanya kelompok kerja lintas bagian', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 20,id_kat_soal = kategori4, pertanyaan = 'Saling memahami dan menghargai tugas dan wewenang rekan kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 21,id_kat_soal = kategori5, pertanyaan = 'Keputusan pimpinan perusahaan dibuat berdasarkan data dan fakta', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 22,id_kat_soal = kategori5, pertanyaan = 'Keputusan atasan langsung  dibuat berdasarkan data dan fakta', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 23,id_kat_soal = kategori5, pertanyaan = 'Ketegasan pimpinan perusahaan dalam mengambil keputusan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 24,id_kat_soal = kategori5, pertanyaan = 'Ketegasan atasan langsung dalam mengambil keputusan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 25,id_kat_soal = kategori5, pertanyaan = 'Pendelegasian tugas dan tanggung jawab yang jelas', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 26,id_kat_soal = kategori5, pertanyaan = 'Dukungan atasan langsung  dalam melaksanakan pekerjaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 27,id_kat_soal = kategori5, pertanyaan = 'Kesempatan berkomunikasi secara informal dan bebas dengan atasan langsung', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 28,id_kat_soal = kategori5, pertanyaan = 'Kesempatan berkomunikasi  secara informal dan bebas dengan pimpinan perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 29,id_kat_soal = kategori5, pertanyaan = 'Atasan langsung yang terbuka dan transparan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 30,id_kat_soal = kategori5, pertanyaan = 'Pimpinan perusahaan yang terbuka dan transparan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 31,id_kat_soal = kategori5, pertanyaan = 'Penilaian prestasi kerja dilakukan  secara  terbuka dan adil', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 32,id_kat_soal = kategori6, pertanyaan = 'Penghargaan  untuk  saran perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 33,id_kat_soal = kategori6, pertanyaan = 'Saran-saran   perbaikan dilaksanakan ', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 34,id_kat_soal = kategori6, pertanyaan = 'Masalah yang muncul  dilihat sebagai peluang untuk perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 35,id_kat_soal = kategori6, pertanyaan = 'Meluangkan  waktu untuk perbaikan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 36,id_kat_soal = kategori7, pertanyaan = 'Hal yang menentukan keberhasilan pekerjaan saya', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 37,id_kat_soal = kategori7, pertanyaan = 'Visi dan sasaran perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 38,id_kat_soal = kategori7, pertanyaan = 'Perubahan-perubahan penting dalam perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 39,id_kat_soal = kategori7, pertanyaan = 'Pencapaian sasaran bagian', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 40,id_kat_soal = kategori7, pertanyaan = 'Kepuasan pelanggan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 41,id_kat_soal = kategori8, pertanyaan = 'Ketrampilan teknis pekerjaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 42,id_kat_soal = kategori8, pertanyaan = 'Ketrampilan bersosialisasi', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 43,id_kat_soal = kategori8, pertanyaan = 'Karir dalam perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 44,id_kat_soal = kategori8, pertanyaan = 'Kemampuan melakukan pekerjaan lain di perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 45,id_kat_soal = kategori9, pertanyaan = 'Gaji yang berdasarkan prestasi kerja', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 46,id_kat_soal = kategori9, pertanyaan = 'Gaji yang berdasarkan lama kerja/senioritas', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 47,id_kat_soal = kategori9, pertanyaan = 'Bonus yang terkait Keuntungan perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 48,id_kat_soal = kategori9, pertanyaan = 'Pensiun dari perusahaan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 49,id_kat_soal = kategori9, pertanyaan = 'Fasilitas lain (makan siang, Kesehatan, transportasi)', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 50,id_kat_soal = kategori10, pertanyaan = 'Kualitas Produk dan pelayanannya', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 51,id_kat_soal = kategori10, pertanyaan = 'Selalu menepati janji  waktu pengiriman', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 52,id_kat_soal = kategori10, pertanyaan = 'Flexibilitas terhadap perubahan waktu pengiriman yang telah disepakati', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 53,id_kat_soal = kategori10, pertanyaan = 'Harga yang bersaing', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 54,id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang berorientasi pada pelanggan', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 55,id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang bonafide', pub_date=timezone.now()),
#     Tb_soal_kepuasan(id = 56,id_kat_soal = kategori10, pertanyaan = 'Perusahaan yang  memperhatikan kesejahteraan karyawan', pub_date=timezone.now())]

# for q in answer2:
#     try:
#         q.save()
#     except IntegrityError:
#         # Handle the duplicate question here, e.g. print an error message
#         print(f"Question '{q.pertanyaan}' already exists in the database.")

class CustomLoginView(LoginView):
	
    template_name = 'auth-login-basic.html'
	
    redirect_authenticated_user = False
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    
class CustomLogoutView(LogoutView):
    template_name = 'auth-login-basic.html'
    next_page = 'login'

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

class RegisterView(View):
    template_name = 'auth-register-basic.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('registersuccess')
        
        return render(request, self.template_name, {'form': form})

def forgotpass(request):
    template = loader.get_template('auth-password-basic.html')
    return HttpResponse(template.render())

def registerSuccess(request):
    template = loader.get_template('success-register.html')
    return HttpResponse(template.render())

@login_required
def accountprofile(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    if request.method == "POST":
        if 'upload_picture' in request.POST:
            # Handle profile picture upload
            profile_picture = request.FILES.get('profile_picture')
            if user_data_obj is None:
                user_data_obj = user_data.objects.create(id_auth_user=request.user)
            if profile_picture:
                user_data_obj.profile_picture = profile_picture
            else:
                user_data_obj.profile_picture = None
            user_data_obj.save()
            # Optionally, you can add a success message or perform other actions
            # related to profile picture upload
            messages.success(request, 'Profile picture saved successfully.')
        elif 'update_biodata' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            if first_name:
                User.objects.filter(id=request.user.id).update(first_name=first_name)
            if last_name:
                User.objects.filter(id=request.user.id).update(last_name=last_name)
            if email:
                User.objects.filter(id=request.user.id).update(email=email)
            position_id = request.POST.get('position')
            location_id = request.POST.get('location')
            gender_id = request.POST.get('gender')
            education_id = request.POST.get('education')
            korsa_id = request.POST.get('korsa')
            jenis_jabatan_id = request.POST.get('jenis_jabatan')
            phone_number = request.POST.get('phone_number')
            birthday = request.POST.get('birthday')
            
            try:
                position = m_position.objects.get(id=position_id)
            except m_position.DoesNotExist:
                position = None
            try:
                location = m_location.objects.get(id=location_id)
            except m_location.DoesNotExist:
                location = None
            try:
                gender = m_gender.objects.get(id=gender_id)  # Get the gender object based on the selected ID
            except m_gender.DoesNotExist:
                gender = None
            try:
                education = m_education.objects.get(id=education_id)  # Get the gender object based on the selected ID
            except m_education.DoesNotExist:
                education = None
            try:
                korsa = m_korsa.objects.get(id=korsa_id)  # Get the gender object based on the selected ID
            except m_korsa.DoesNotExist:
                korsa = None
            try:
                jenis_jabatan = m_jenis_jabatan.objects.get(id=jenis_jabatan_id)  # Get the gender object based on the selected ID
            except m_jenis_jabatan.DoesNotExist:
                jenis_jabatan = None

            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            # Check if user_data already exists for the authenticated user
            user_data_obj, created = user_data.objects.get_or_create(id_auth_user=request.user)

            if position:
                user_data_obj.position = position
            if location:
                user_data_obj.location = location
            if phone_number:
                user_data_obj.phone_number = phone_number
            if birthday:
                user_data_obj.birthday = birthday
            if gender:
                user_data_obj.gender = gender
            if education:
                user_data_obj.education = education
            if korsa:
                user_data_obj.korsa = korsa
            if jenis_jabatan:
                user_data_obj.jenis_jabatan = jenis_jabatan

            user_data_obj.save()
            request.session['user_data_obj'] = user_data_obj.id
            # Optionally, you can add a success message or perform other actions
            # related to updating biodata
            return redirect('profile')
        
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    id = request.user.id
    positions = m_position.objects.all()
    locations = m_location.objects.all()
    genders = m_gender.objects.all()
    educations = m_education.objects.all()
    korsas = m_korsa.objects.all()
    jenis_jabatans = m_jenis_jabatan.objects.all()
    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'id': id,
        'positions': positions,
        'locations': locations,
        'genders': genders,
        'educations': educations,
        'korsas': korsas,
        'jenis_jabatans': jenis_jabatans,
        'user_data_obj': user_data_obj, 
    }
    return render(request, 'account-profile.html', context)
    # return render(request, 'content-profile.html', context)

@login_required
def quesionaire(request):
    template = loader.get_template('quesionaire.html')
    return HttpResponse(template.render())

@login_required
def kuesioner(request):
    if request.method == 'POST':
        user = request.user  # Assuming you have authentication enabled
        # user_data_obj = None
        question_number = request.session.get('question_number', 1)
        answer_id = request.POST.get('answer')

        if answer_id is None:
            # Render the page with an error message
            question = Tb_soal_kepuasan_umum.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)
            error_message = 'Please select an answer'
            context = {
                'question': question,
                'answers': answers,
                'error_message': error_message,
            }
            return render(request, 'quesionaire.html', context)
        
        question = Tb_soal_kepuasan_umum.objects.get(id=question_number)
        answer = Tb_answer.objects.get(id=answer_id)

        try:
            response = UserResponse.objects.get(user=user, question=question)
        except UserResponse.DoesNotExist:
            response = UserResponse(user=user, question=question)

        response.answer = answer
        response.save()
        
        question_number += 1
        request.session['question_number'] = question_number

        if question_number > Tb_soal_kepuasan_umum.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1
            return redirect('thank_you')
        else:
            return redirect('kuesioner')

    else:
        question_number = request.session.get('question_number', 1)

        if question_number > Tb_soal_kepuasan_umum.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1

            return redirect('thank_you')

        try:
            user_data_obj = user_data.objects.get(id_auth_user=request.user)
            question = Tb_soal_kepuasan_umum.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)

            context = {
                'question': question,
                'answers': answers,
                'user_data_obj': user_data_obj,
            }
            return render(request, 'quesionaire.html', context)

        except Tb_soal_kepuasan_umum.DoesNotExist:
            return redirect('thank_you')

@login_required
def kuesioner1(request):
    if request.method == 'POST':
        user = request.user  # Assuming you have authentication enabled
        
        question_number = request.session.get('question_number', 1)
        answer_id = request.POST.get('answer')

        if answer_id is None:
            # Render the page with an error message
            question = Tb_soal_kepentingan.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)
            error_message = 'Please select an answer'
            context = {
                'question': question,
                'answers': answers,
                'error_message': error_message,
            }
            return render(request, 'quesionaire1.html', context)

        question = Tb_soal_kepentingan.objects.get(id=question_number)
        answer = Tb_answer.objects.get(id=answer_id)

        try:
            response = UserResponse1.objects.get(user=user, question=question)
        except UserResponse1.DoesNotExist:
            response = UserResponse1(user=user, question=question, lvl_kepuasan=question.lvl_kepuasan)

        response.answer = answer
        response.save()

        question_number += 1
        request.session['question_number'] = question_number

        if question_number > Tb_soal_kepentingan.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1

            return redirect('thank_you1')
        else:
            return redirect('kuesioner1')

    else:
        question_number = request.session.get('question_number', 1)

        if question_number > Tb_soal_kepentingan.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1

            return redirect('thank_you1')

        try:
            user_data_obj = user_data.objects.get(id_auth_user=request.user)
            question = Tb_soal_kepentingan.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)

            context = {
                'question': question,
                'answers': answers,
                'user_data_obj': user_data_obj,
            }
            return render(request, 'quesionaire1.html', context)

        except Tb_soal_kepentingan.DoesNotExist:
            request.session['question_number'] = 1
            return redirect('thank_you1')



@login_required
def kuesioner2(request):
    if request.method == 'POST':
        user = request.user  # Assuming you have authentication enabled

        question_number = request.session.get('question_number', 1)
        answer_id = request.POST.get('answer')

        if answer_id is None:
            # Render the page with an error message
            question = Tb_soal_kepuasan.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)
            error_message = 'Please select an answer'
            context = {
                'question': question,
                'answers': answers,
                'error_message': error_message,
            }
            return render(request, 'quesionaire2.html', context)

        question = Tb_soal_kepuasan.objects.get(id=question_number)
        answer = Tb_answer.objects.get(id=answer_id)

        try:
            response = UserResponse2.objects.get(user=user, question=question)
        except UserResponse2.DoesNotExist:
            response = UserResponse2(user=user, question=question, lvl_kepuasan=question.lvl_kepuasan)

        response.answer = answer
        response.save()

        question_number += 1
        request.session['question_number'] = question_number

        if question_number > Tb_soal_kepuasan.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1

            return redirect('user_comment')
        else:
            return redirect('kuesioner2')

    else:
        question_number = request.session.get('question_number', 1)

        if question_number > Tb_soal_kepuasan.objects.count():
            request.session['question_number'] = 1  # Reset the question_number to 1

            return redirect('thank_you2')

        try:
            user_data_obj = user_data.objects.get(id_auth_user=request.user)
            question = Tb_soal_kepuasan.objects.get(id=question_number)
            answers = Tb_answer.objects.filter(test_kategori=question.test)

            context = {
                'question': question,
                'answers': answers,
                'user_data_obj': user_data_obj
            }
            return render(request, 'quesionaire2.html', context)

        except Tb_soal_kepuasan.DoesNotExist:
            return redirect('thank_you2')



@login_required
def thank_you(request):
    template = loader.get_template('thank_you.html')
    return HttpResponse(template.render())

@login_required      
def thank_you1(request):
    template = loader.get_template('thank_you1.html')
    return HttpResponse(template.render())

@login_required
def thank_you2(request):
    user = request.user

    if (
        UserResponse.objects.filter(user=user).count() >= Tb_soal_kepuasan_umum.objects.count()
        and UserResponse1.objects.filter(user=user).count() >= Tb_soal_kepentingan.objects.count()
        and UserResponse2.objects.filter(user=user).count() >= Tb_soal_kepuasan.objects.count()
    ):
        return render(request, 'thank_you2.html')
    else:
        return redirect('kuesioner')
    
@login_required(login_url='admin_login')
def dashboard(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None
    locations = m_location.objects.all()

    # Get the selected location from the request
    selected_location = request.GET.get('location')

    # Filter positions based on the selected location
    if selected_location:
        if selected_location == 'all':
            positions = m_position.objects.annotate(count=Count('user_data'))
        else:
            positions = m_position.objects.annotate(count=Count('user_data')).filter(user_data__location=selected_location)
    else:
        positions = m_position.objects.annotate(count=Count('user_data'))

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Generate the chart data based on the selected location
        chart_data = []

        for position in positions:
            chart_data.append({
                'position': position.position,
                'count': position.count,
            })

        return JsonResponse(chart_data, safe=False)

    female_count = user_data.objects.filter(gender__gender='perempuan').count()
    male_count = user_data.objects.filter(gender__gender='laki-laki').count()
    total_count = user_data.objects.count()
    education_SD = user_data.objects.filter(education__education='SD').count()
    education_SLTP = user_data.objects.filter(education__education='SLTP').count()
    education_SLTA = user_data.objects.filter(education__education='SLTA').count()
    education_Diploma = user_data.objects.filter(education__education='Diploma').count()
    education_Sarjana = user_data.objects.filter(education__education='Sarjana').count()
    education_Pasca_Sarjana = user_data.objects.filter(education__education='Pasca Sarjana').count()
    birthday_list = user_data.objects.values_list('birthday', flat=True)
    jabatan_managerial = user_data.objects.filter(jenis_jabatan__jenis_jabatan='Managerial').count()
    jabatan_specialist = user_data.objects.filter(jenis_jabatan__jenis_jabatan='Specialist').count()
    jabatan_technical = user_data.objects.filter(jenis_jabatan__jenis_jabatan='Technical').count()
    jabatan_administrative = user_data.objects.filter(jenis_jabatan__jenis_jabatan='Administrative').count()
    posisi_direktur = user_data.objects.filter(position__position='Corporate Deputy Director/Group Head/Executive Vice President').count()
    posisi_general = user_data.objects.filter(position__position='General Manager/Vice President').count()
    posisi_senior = user_data.objects.filter(position__position='Senior Manajer/Manajer').count()
    posisi_junior = user_data.objects.filter(position__position='Junior Manajer').count()
    posisi_asman = user_data.objects.filter(position__position='Asisten Manajer').count()
    posisi_sspv = user_data.objects.filter(position__position='Senior Supervisor').count()
    posisi_spv = user_data.objects.filter(position__position='Supervisor').count()
    posisi_jspv = user_data.objects.filter(position__position='Junior Supervisor').count()
    posisi_pelaksana = user_data.objects.filter(position__position='Pelaksana').count()
    korsa_utama = user_data.objects.filter(korsa__korsa='Utama').count()
    korsa_niaga = user_data.objects.filter(korsa__korsa='Niaga').count()
    korsa_operasi = user_data.objects.filter(korsa__korsa='Operasi').count()
    korsa_prasarana = user_data.objects.filter(korsa__korsa='Pengelolaan Prasarana').count()
    korsa_keselamatan = user_data.objects.filter(korsa__korsa='Keselamatan & Keamanan').count()
    korsa_SDM = user_data.objects.filter(korsa__korsa='SDM & Umum').count()
    korsa_perencanaan = user_data.objects.filter(korsa__korsa='Perencanaan Strategis dan Pengembangan Usaha').count()
    korsa_keuangan = user_data.objects.filter(korsa__korsa='Keuangan').count()

    context = {
        'female_count': female_count,
        'male_count': male_count,
        'total_count': total_count,
        'education_SD': education_SD,
        'education_SLTP': education_SLTP,
        'education_SLTA': education_SLTA,
        'education_Diploma': education_Diploma,
        'education_Sarjana': education_Sarjana,
        'education_Pasca_Sarjana': education_Pasca_Sarjana,
        'birthday_list': birthday_list,
        'jabatan_managerial': jabatan_managerial,
        'jabatan_specialist': jabatan_specialist,
        'jabatan_technical': jabatan_technical,
        'jabatan_administrative': jabatan_administrative,
        'posisi_direktur': posisi_direktur,
        'posisi_general': posisi_general,
        'posisi_senior': posisi_senior,
        'posisi_junior': posisi_junior,
        'posisi_asman': posisi_asman,
        'posisi_sspv': posisi_sspv,
        'posisi_spv': posisi_spv,
        'posisi_jspv': posisi_jspv,
        'posisi_pelaksana': posisi_pelaksana,
        'korsa_utama': korsa_utama,
        'korsa_niaga': korsa_niaga,
        'korsa_operasi': korsa_operasi,
        'korsa_prasarana': korsa_prasarana,
        'korsa_keselamatan': korsa_keselamatan,
        'korsa_SDM': korsa_SDM,
        'korsa_perencanaan': korsa_perencanaan,
        'korsa_keuangan': korsa_keuangan,
        'user_data_obj' : user_data_obj,
        'locations': locations, 
        'positions': positions, 
        'selected_location': selected_location,
    }
    return render(request, 'dashboard-1.html', context)


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None and (user.is_staff or user.is_superuser):
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Replace 'admin_dashboard' with the appropriate URL for your admin dashboard
        else:
            messages.error(request, 'Invalid login credentials or insufficient privileges.')
    
    return render(request, 'auth-login-admin.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url='admin_login')
def participant_list(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None
    user_data_list = user_data.objects.all()  # Retrieve all data from the UserData table
    user_response_ids = UserResponse.objects.values_list('user_id', flat=True)
    user_response1_ids = UserResponse1.objects.values_list('user_id', flat=True)
    user_response2_ids = UserResponse2.objects.values_list('user_id', flat=True)
    auth_user_list = User.objects.filter(is_staff=0, is_superuser=0)

    num_questions_answered = UserResponse.objects.values('user_id').annotate(num_answers=Count('user_id')).filter(num_answers=9).values_list('user_id', flat=True)

    context = {
        'user_data_list': user_data_list,
        'user_response_ids': user_response_ids,
        'user_data_list': user_data_list,
        'user_response_ids': user_response_ids,
        'user_response1_ids': user_response1_ids,
        'user_response2_ids': user_response2_ids,
        'auth_user_list': auth_user_list,
        'num_questions_answered': num_questions_answered,
        'user_data_obj': user_data_obj,
    }
    
    if request.method == 'POST' and 'delete_user' in request.POST:
        user_id = int(request.POST.get('delete_user'))
        try:
            user = user_data.objects.get(id=user_id)
            user.delete()
        except user_data.DoesNotExist:
            pass  # Handle the case where the user does not exist
        
        return redirect('participant_list')  # Redirect to the participant list page after deleting the user
    
    return render(request, 'participant_list.html', context)

@login_required(login_url='admin_login')
def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('delete_user')
        auth_user_id = request.POST.get('delete_auth_user')
        
        # Delete record from user_data_list table
        user_data.objects.filter(id=user_id).delete()
        
        # Delete record from auth_user table
        User.objects.filter(id=auth_user_id).delete()
        
    return redirect('participant_list')

@login_required(login_url='admin_login')
def add_participant(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    if request.method == 'POST':
        first_name = request.POST['inputFirstName']
        last_name = request.POST['inputLastName']
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Redirect to success page or perform any other actions
        return redirect('participant_list')  # Replace 'success' with the URL name of your success page
    
    context = {
        'user_data_obj': user_data_obj,
    }

    return render(request, 'add_participant.html', context)

@login_required(login_url='admin_login')
def edit_user(request, user_id):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None
    users = user_data.objects.get(id=user_id)
    locations = m_location.objects.all()
    jabatans = m_jenis_jabatan.objects.all()
    genders = m_gender.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        new_password = request.POST.get('new_password')
        location_id = request.POST.get('location')
        jenis_jabatan_id = request.POST.get('jenis_jabatan')
        gender_id = request.POST.get('gender')

        # Update user's first name and last name
        users.id_auth_user.first_name = first_name
        users.id_auth_user.last_name = last_name

        # Update user's password if a new password is provided
        if new_password:
            users.id_auth_user.set_password(new_password)
        
        # Update user's jenis_jabatan
        location = m_location.objects.get(id=location_id)
        users.location = location
        jenis_jabatan = m_jenis_jabatan.objects.get(id=jenis_jabatan_id)
        users.jenis_jabatan = jenis_jabatan
        gender = m_gender.objects.get(id=gender_id)
        users.gender = gender
        
        users.id_auth_user.save()
        users.save()

        return redirect('participant_list')

    context = {
        'users': users,
        'jabatans': jabatans,
        'locations': locations,
        'genders': genders,
        'user_data_obj': user_data_obj,
    }

    return render(request, 'edit_user.html', context)

def count_user_umums(request):
    # Perform the aggregation query
    user_counts = UserResponse.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

    # Iterate over the queryset and update or create UserCount objects
    for item in user_counts:
        question_id = item['question']
        user_count = item['user_count']
        total_score = item['total_score']

        # Update or create the UserCount object
        count_user_umum.objects.update_or_create(
            question_id=question_id,
            defaults={'user_count': user_count, 'total_score': total_score}
        )

    # Retrieve all UserCount objects after the update
    user_count_objects = count_user_umum.objects.all()

    # Pass the user_counts list to the template context
    context = {'user_counts': user_count_objects}

    # Render the template with the context
    return render(request, 'result.html', context)

def count_user_kepentingans(request):
    # Perform the aggregation query
    user_counts = UserResponse1.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

    # Iterate over the queryset and update or create UserCount objects
    for item in user_counts:
        question_id = item['question']
        user_count = item['user_count']
        total_score = item['total_score']

        # Update or create the UserCount object
        count_user_kepentingan.objects.update_or_create(
            question_id=question_id,
            defaults={'user_count': user_count, 'total_score': total_score}
        )

    # Retrieve all UserCount objects after the update
    user_count_objects = count_user_kepentingan.objects.all()

    # Pass the user_counts list to the template context
    context = {'user_counts': user_count_objects}

    # Render the template with the context
    return render(request, 'result1.html', context)

def count_user_kepuasans(request):
    # Perform the aggregation query
    user_counts = UserResponse2.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

    # Iterate over the queryset and update or create UserCount objects
    for item in user_counts:
        question_id = item['question']
        user_count = item['user_count']
        total_score = item['total_score']

        # Update or create the UserCount object
        count_user_kepuasan.objects.update_or_create(
            question_id=question_id,
            defaults={'user_count': user_count, 'total_score': total_score}
        )

    # Retrieve all UserCount objects after the update
    user_count_objects = count_user_kepuasan.objects.all()

    # Pass the user_counts list to the template context
    context = {'user_counts': user_count_objects}

    # Render the template with the context
    return render(request, 'result2.html', context)

@login_required(login_url='admin_login')    
def jabatan_list(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None
    jenis_jabatan_list = m_jenis_jabatan.objects.annotate(user_count=Count('user_data'))
    
    context = {
        'jenis_jabatan_list': jenis_jabatan_list,
        'user_data_obj': user_data_obj,
    }
    return render(request, 'jabatan_list.html', context)

def dashboard2(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    total_count = user_data.objects.count()

    scores = []

    # Calculate and update the score difference for each record in tb_score_lvl
    kepentingan_scores = score_lvl_kepentingan.objects.all()
    for kepuasan_score in score_lvl_kepuasan.objects.all():
        kepentingan_score = kepentingan_scores.filter(lvl_kepuasan=kepuasan_score.lvl_kepuasan).first()
        if kepentingan_score:
            score_difference = kepuasan_score.total_score - kepentingan_score.total_score

            # Update or create the record based on the unique identifier
            obj, created = tb_score_lvl.objects.update_or_create(
                lvl_kepuasan=kepuasan_score.lvl_kepuasan,
                defaults={
                    'total_score_lvl_kepuasan': kepuasan_score.total_score,
                    'total_score_lvl_kepentingan': kepentingan_score.total_score,
                    'score_difference': score_difference,
                }
            )
            scores.append(obj)

    # Perform a bulk update if needed (existing records)
    if scores:
        tb_score_lvl.objects.bulk_update(scores, ['total_score_lvl_kepuasan', 'total_score_lvl_kepentingan', 'score_difference'])

    # Fetch all the updated records from tb_score_lvl
    updated_scores = tb_score_lvl.objects.all()
    updated_scores1 = tb_score_lvl.objects.filter(id=1)
    updated_scores2 = tb_score_lvl.objects.filter(id=2)
    updated_scores3 = tb_score_lvl.objects.filter(id=3)
    updated_scores4 = tb_score_lvl.objects.filter(id=4)
    updated_scores5 = tb_score_lvl.objects.filter(id=5)
    updated_scores6 = tb_score_lvl.objects.filter(id=6)
    updated_scores7 = tb_score_lvl.objects.filter(id=7)
    updated_scores8 = tb_score_lvl.objects.filter(id=8)
    updated_scores9 = tb_score_lvl.objects.filter(id=9)
    updated_scores10 = tb_score_lvl.objects.filter(id=10)

    score_dimensi.calculate_score_difference()
    score_dimensi.update_average_score_difference()

    # Filter the scores where dimensi's 'nama_dimensi' is "Proactive"
    proactive_scores = score_dimensi.objects.filter(dimensi=1).distinct()
    innovative_scores = score_dimensi.objects.filter(dimensi=2).distinct()
    collab_scores = score_dimensi.objects.filter(dimensi=3).distinct()
    pay_scores = score_dimensi.objects.filter(dimensi=4).distinct()
    safety_scores = score_dimensi.objects.filter(dimensi=5).distinct()
    wlb_scores = score_dimensi.objects.filter(dimensi=6).distinct()
    jobsecur_scores = score_dimensi.objects.filter(dimensi=7).distinct()
    workinfra_scores = score_dimensi.objects.filter(dimensi=8).distinct()
    seniorlead_scores = score_dimensi.objects.filter(dimensi=9).distinct()
    perfom_scores = score_dimensi.objects.filter(dimensi=10).distinct()
    career_scores = score_dimensi.objects.filter(dimensi=11).distinct()
    reward_scores = score_dimensi.objects.filter(dimensi=12).distinct()
    reputation_scores = score_dimensi.objects.filter(dimensi=13).distinct()

    avg_score_difference = tb_score_lvl.objects.aggregate(Avg('score_difference'))['score_difference__avg']
    avg_score_difference1 = score_dimensi.objects.aggregate(Avg('score_difference'))['score_difference__avg']

    context = {
        'user_data_obj': user_data_obj,
        'proactive_scores': proactive_scores,
        'innovative_scores': innovative_scores,
        'collab scores': collab_scores,
        'pay_scores': pay_scores,
        'safety_scores': safety_scores,
        'wlb_scores': wlb_scores,
        'jobsecur_scores': jobsecur_scores,
        'workinfra_scores': workinfra_scores,
        'seniorlead_scores': seniorlead_scores,
        'perfom_scores': perfom_scores,
        'career_scores': career_scores,
        'reward_scores': reward_scores,
        'reputation_scores': reputation_scores,
        'scores': updated_scores,
        'updated_scores1': updated_scores1,
        'updated_scores2': updated_scores2,
        'updated_scores3': updated_scores3,
        'updated_scores4': updated_scores4,
        'updated_scores5': updated_scores5,
        'updated_scores6': updated_scores6,
        'updated_scores7': updated_scores7,
        'updated_scores8': updated_scores8,
        'updated_scores9': updated_scores9,
        'updated_scores10': updated_scores10,
        'total_count': total_count,
        'avg_score_difference': avg_score_difference,
        'avg_score_difference1': avg_score_difference1
    }
    return render(request, 'dashboard-2.html', context)

def dashboard3(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    user_comments = UserComment.objects.all()

    # Create a list to store the data for rendering in the template
    def count_sentences(text):
        sentences = re.split(r'[.!?]', text)
        # Filter out empty strings
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

    # Calculate the sentence counts for each comment
    for comment in user_comments:
        comment.komentar_count = count_sentences(comment.komentar)
        comment.saran_count = count_sentences(comment.saran)
    
    context = {
        'user_data_obj': user_data_obj,
        'user_comments': user_comments,
    }
    return render(request, 'dashboard-3.html', context)

def position_chart(request):
    # Get all the locations
    locations = m_location.objects.all()

    # Get the selected location from the request
    selected_location = request.GET.get('location')

    # Filter positions based on the selected location
    if selected_location:
        if selected_location == 'all':
            positions = m_position.objects.annotate(count=Count('user_data'))
        else:
            positions = m_position.objects.annotate(count=Count('user_data')).filter(user_data__location=selected_location)
    else:
        positions = m_position.objects.annotate(count=Count('user_data'))

    # Render the template with the locations, positions, and selected location
    return render(request, 'chart.html', {'locations': locations, 'positions': positions, 'selected_location': selected_location})

def update_chart(request):
    location_id = request.GET.get('location_id')

    # Filter positions based on the selected location
    if location_id == 'all':
        positions = m_position.objects.annotate(count=Count('user_data'))
    else:
        positions = m_position.objects.annotate(count=Count('user_data')).filter(user_data__location=location_id)

    # Prepare the updated positions data
    positions_data = []
    for position in positions:
        positions_data.append({
            'position': position.position,
            'count': position.count
        })

    return JsonResponse(positions_data, safe=False)

@login_required(login_url='admin_login')
def manage_kuesioner(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None
    kepuasan_umum = Tb_soal_kepuasan_umum.objects.all()  # Retrieve all data from the UserData table
    kepentingan = Tb_soal_kepentingan.objects.all()
    kepuasan = Tb_soal_kepuasan.objects.all()

    context = {
        'kepuasan_umum': kepuasan_umum,
        'kepentingan': kepentingan,
        'kepuasan': kepuasan,
        'user_data_obj': user_data_obj,
    }
    
    # if request.method == 'POST' and 'delete_user' in request.POST:
    #     user_id = int(request.POST.get('delete_user'))
    #     try:
    #         user = user_data.objects.get(id=user_id)
    #         user.delete()
    #     except user_data.DoesNotExist:
    #         pass  # Handle the case where the user does not exist
        
    #     return redirect('manage_kuesioner')  # Redirect to the participant list page after deleting the user
    
    return render(request, 'manage_kuesioner.html', context)

@login_required(login_url='admin_login')
def add_kuesioner(request):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    if request.method == 'POST':
        kuesioner_form = KuesionerForm(request.POST)
        kepentingan_form = KepentinganForm(request.POST)
        kepuasan_form = KepuasanForm(request.POST)

        if kuesioner_form.is_valid():
            kuesioner_form.save()
            return redirect('manage_kuesioner')

        if kepentingan_form.is_valid():
            kepentingan_form.save()
            return redirect('manage_kuesioner')

        if kepuasan_form.is_valid():
            kepuasan_form.save()
            return redirect('manage_kuesioner')
    else:
        kuesioner_form = KuesionerForm()
        kepentingan_form = KepentinganForm()
        kepuasan_form = KepuasanForm()
    
    test_kategori_queryset = Tb_test_kategori.objects.all()

    return render(request, 'manage_kuesioner_add.html', {
        'kuesioner_form': kuesioner_form,
        'kepentingan_form': kepentingan_form,
        'kepuasan_form': kepuasan_form,
        'test_kategori_queryset': test_kategori_queryset,
        'user_data_obj': user_data_obj
    })

def edit_kepuasan_umum(request, id):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    data = get_object_or_404(Tb_soal_kepuasan_umum, id=id)

    if request.method == 'POST':
        # Process the form data
        pertanyaan = request.POST.get('pertanyaan')
        
        data.pertanyaan = pertanyaan
        data.save()
        
        # Redirect to a success page
        return redirect('manage_kuesioner')

    return render(request, 'manage_kepuasan_umum.html', {'data': data, 'user_data_obj': user_data_obj})

def edit_kepentingan(request, id):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    data = get_object_or_404(Tb_soal_kepentingan, id=id)

    if request.method == 'POST':
        # Process the form data
        pertanyaan = request.POST.get('pertanyaan')
        
        data.pertanyaan = pertanyaan
        data.save()
        
        # Redirect to a success page
        return redirect('manage_kuesioner')

    return render(request, 'manage_kepentingan.html', {'data': data, 'user_data_obj': user_data_obj })

def edit_kepuasan(request, id):
    try:
        user_data_obj = user_data.objects.get(id_auth_user=request.user)
    except user_data.DoesNotExist:
        user_data_obj = None

    data = get_object_or_404(Tb_soal_kepuasan, id=id)

    if request.method == 'POST':
        # Process the form data
        pertanyaan = request.POST.get('pertanyaan')
        
        data.pertanyaan = pertanyaan
        data.save()
        
        # Redirect to a success page
        return redirect('manage_kuesioner')

    return render(request, 'manage_kepuasan.html', {'data': data, 'user_data_obj': user_data_obj})


def score_sum_kepentingans(request):
    # Aggregate the sum of scores for each unique lvl_kepuasan value
    score_sums = UserResponse1.objects.values('lvl_kepuasan').annotate(total_score=models.Sum('score'))

    # Save or generate records in the QuestionUserCount table
    for score_sum in score_sums:
        lvl_kepuasan_id = score_sum['lvl_kepuasan']
        total_score = score_sum['total_score']

        # Retrieve the corresponding Tb_kategori_soal instance
        lvl_kepuasan = Tb_kategori_soal.objects.get(id=lvl_kepuasan_id)

        # Create or retrieve the score_lvl_kepentingan instance
        question_user_count, created = score_lvl_kepentingan.objects.get_or_create(lvl_kepuasan=lvl_kepuasan)
        question_user_count.total_score = total_score
        question_user_count.save()

    # Pass the aggregated data to the template
    context = {'score_sums': score_sums}
    return render(request, 'lvl_kepentingan.html', context)

def score_sum_kepuasans(request):
    # Aggregate the sum of scores for each unique lvl_kepuasan value
    score_sums = UserResponse2.objects.values('lvl_kepuasan').annotate(total_score=models.Sum('score'))

    # Save or generate records in the QuestionUserCount table
    for score_sum in score_sums:
        lvl_kepuasan_id = score_sum['lvl_kepuasan']
        total_score = score_sum['total_score']

        # Retrieve the corresponding Tb_kategori_soal instance
        lvl_kepuasan = Tb_kategori_soal.objects.get(id=lvl_kepuasan_id)

        # Create or retrieve the score_lvl_kepentingan instance
        question_user_count, created = score_lvl_kepuasan.objects.get_or_create(lvl_kepuasan=lvl_kepuasan)
        question_user_count.total_score = total_score
        question_user_count.save()

    # Pass the aggregated data to the template
    context = {'score_sums': score_sums}
    return render(request, 'lvl_kepuasan.html', context)

def sum_dimensi_kepentingan(request):
    # Perform the aggregation query
    counts = UserResponse1.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

    # Update the dimensi_kepentingan objects with the counts
    for count in counts:
        question_id = count['question']
        total_score = count['total_score']
        if total_score is not None:
            total_score = int(total_score)

        # Use the update() method to update the existing objects
        dimensi_kepentingan.objects.filter(question_id=question_id).update(total_score=total_score)

    # Retrieve all dimensi_kepentingan objects after the update
    dimensi_kepentingans = dimensi_kepentingan.objects.all()

    # Pass the dimensi_kepentingans queryset to the template context
    context = {'dimensi_kepentingans': dimensi_kepentingans}

    # Render the template with the context
    return render(request, 'result2.html', context)

def sum_dimensi_kepuasan(request):
    # Perform the aggregation query
    counts = UserResponse2.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

    # Update the dimensi_kepentingan objects with the counts
    for count in counts:
        question_id = count['question']
        total_score = count['total_score']
        if total_score is not None:
            total_score = int(total_score)

        # Use the update() method to update the existing objects
        dimensi_kepuasan.objects.filter(question_id=question_id).update(total_score=total_score)

    # Retrieve all dimensi_kepentingan objects after the update
    dimensi_kepuasans = dimensi_kepuasan.objects.all()

    # Pass the dimensi_kepentingans queryset to the template context
    context = {'dimensi_kepuasans': dimensi_kepuasans}

    # Render the template with the context
    return render(request, 'result1.html', context)

def display_scores(request):
    score_dimensi.calculate_score_difference()
    score_dimensi.update_average_score_difference()

    scores = score_dimensi.objects.all()

    context = {
        'scores': scores
    }

    return render(request, 'scores.html', context)

def lvl_scores(request):
    scores = []

    # Calculate and update the score difference for each record in tb_score_lvl
    kepentingan_scores = score_lvl_kepentingan.objects.all()
    for kepuasan_score in score_lvl_kepuasan.objects.all():
        kepentingan_score = kepentingan_scores.filter(lvl_kepuasan=kepuasan_score.lvl_kepuasan).first()
        if kepentingan_score:
            score_difference = kepuasan_score.total_score - kepentingan_score.total_score

            # Update or create the record based on the unique identifier
            obj, created = tb_score_lvl.objects.update_or_create(
                lvl_kepuasan=kepuasan_score.lvl_kepuasan,
                defaults={
                    'total_score_lvl_kepuasan': kepuasan_score.total_score,
                    'total_score_lvl_kepentingan': kepentingan_score.total_score,
                    'score_difference': score_difference,
                }
            )
            scores.append(obj)

    # Perform a bulk update if needed (existing records)
    if scores:
        tb_score_lvl.objects.bulk_update(scores, ['total_score_lvl_kepuasan', 'total_score_lvl_kepentingan', 'score_difference'])

    # Fetch all the updated records from tb_score_lvl
    updated_scores = tb_score_lvl.objects.all()

    return render(request, 'lvl_scores.html', {'scores': updated_scores})

@login_required
def user_comment(request):
    if request.method == 'POST':
        # Assuming you have a user associated with the comment, you can get the user from request.user
        user = request.user
        saran = request.POST.get('saran')
        komentar = request.POST.get('komentar')

        # Check if a comment by the same user exists
        existing_comment = UserComment.objects.filter(user=user).first()

        if existing_comment:
            # Update the existing comment
            existing_comment.saran = saran
            existing_comment.komentar = komentar
            existing_comment.save()
        else:
            # Create a new comment
            UserComment.objects.create(user=user, saran=saran, komentar=komentar)

        # Redirect to a success page or any other desired URL
        return redirect('thank_you2')  # Replace 'success_page' with the URL you want to redirect to

    return render(request, 'user-comment.html')
