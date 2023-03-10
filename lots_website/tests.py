from django.test import TestCase


class TestHomeViews(TestCase):
    """ Test correct rendering for home url """

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_about_us_page(self):
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about_us.html')

    def test_get_links_page(self):
        response = self.client.get('/links/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/links.html')

    def test_get_membership_page(self):
        response = self.client.get('/membership/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/membership.html')

    def test_get_publications_page(self):
        response = self.client.get('/publications/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/publications.html')

    def test_get_sales_page(self):
        response = self.client.get('/sales/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/sales.html')

    def test_get_news_page(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/news.html')

#     return render(request, "admin/")
#     return render(request, "admin/news/post/add/")
#     return render(request, "home/membership-type/lbm-uk.html")
#    return render(request, "home/membership-type/tlb-uk.html")
#     return render(request, "home/membership-type/tlb-lbm-uk.html")
#     return render(request, "home/membership-type/tlb-lbm-europe.html")
#     return render(request, "home/membership-type/tlb-europe.html")
#     return render(request, "home/membership-type/lbm-europe.html")
#     return render(request, "home/membership-type/tlb-lbm-world.html")
#     return render(request, "home/membership-type/tlb-world.html")
#     return render(request, "home/membership-type/lbm-world.html")
