from django.contrib import admin
from .models import Tb_test_kategori, Tb_answer, Tb_kategori_soal, Tb_soal_kepuasan_umum, Tb_soal_kepentingan, Tb_soal_kepuasan, m_location, m_position, user_data, m_gender, m_education, m_korsa, m_jenis_jabatan, tb_dimensi, dimensi_kepentingan, dimensi_kepuasan


admin.site.register(Tb_test_kategori)
admin.site.register(Tb_kategori_soal)
admin.site.register(Tb_answer)
admin.site.register(Tb_soal_kepuasan_umum)
admin.site.register(Tb_soal_kepentingan)
admin.site.register(Tb_soal_kepuasan)
admin.site.register(m_position)
admin.site.register(m_location)
admin.site.register(m_gender)
admin.site.register(user_data)
admin.site.register(m_education)
admin.site.register(m_korsa)
admin.site.register(m_jenis_jabatan)
admin.site.register(tb_dimensi)
admin.site.register(dimensi_kepuasan)
admin.site.register(dimensi_kepentingan)