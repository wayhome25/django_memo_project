from django.test import TestCase

# Create your tests here.
from .models import Memos

class MemosTestCase(TestCase):
    def test_modify(self):
        g = Memos(name='몽키', title='몽키제목', text='이것은 내용입니다.')
        print('수정전 이름:', g.name)
        print(g.update_date)
        print('------------')
        self.assertTrue(len(g.text) > 1)
