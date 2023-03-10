from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_about_us_url_is_resolved(self):
        url = reverse('about_us')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about_us)

    def test_publications_url_is_resolved(self):
        url = reverse('publications')
        print(resolve(url))
        self.assertEquals(resolve(url).func, publications)

    def test_links_url_is_resolved(self):
        url = reverse('links')
        print(resolve(url))
        self.assertEquals(resolve(url).func, links)

    def test_membership_url_is_resolved(self):
        url = reverse('membership')
        print(resolve(url))
        self.assertEquals(resolve(url).func, membership)

    def test_sales_url_is_resolved(self):
        url = reverse('sales')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sales)

    # def test_admin_url_is_resolved(self):
    #     url = reverse('admin/')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url), admin/)

    # def test_add_post_url_is_resolved(self):
    #     url = reverse('add_post')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, add_post)

    def test_luk_url_is_resolved(self):
        url = reverse('luk')
        print(resolve(url))
        self.assertEquals(resolve(url).func, LUk)

    def test_tuk_url_is_resolved(self):
        url = reverse('tuk')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TUk)

    def test_tluk_url_is_resolved(self):
        url = reverse('tluk')
        print(resolve(url))
        self.assertEquals(resolve(url).func,  TLUk)

    def test_tleu_url_is_resolved(self):
        url = reverse('tleu')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TLEu)

    def test_TEu_url_is_resolved(self):
        url = reverse('teu')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TEu)

    def test_leu_url_is_resolved(self):
        url = reverse('leu')
        print(resolve(url))
        self.assertEquals(resolve(url).func, LEu)

    def test_lworld_url_is_resolved(self):
        url = reverse('lworld')
        print(resolve(url))
        self.assertEquals(resolve(url).func, LWorld)

    def test_tlworld_url_is_resolved(self):
        url = reverse('tlworld')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TLWorld)

    def test_tworld_url_is_resolved(self):
        url = reverse('tworld')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TWorld)

    # def test_ _url_is_resolved(self):
    #     url = reverse(' ')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,  )
