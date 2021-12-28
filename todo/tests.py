import time
from django.contrib.auth import get_user_model
from django.forms.forms import DeclarativeFieldsMetaclass
from django.http import response
from django.test import TestCase, SimpleTestCase, Client, client
from django.urls import reverse
from django.urls.base import resolve
from .views import hello, updatetask, deletetask
from .models import Task


# Create your tests here.

class TestUrls(SimpleTestCase):
    def setUp(self):
        self.sleep = time.sleep(3)

    def test_task_url_is_resolved(self):
        url = reverse('tasks')
        print(f"Testing '{url}' URL")

        self.assertEqual(resolve(url).func, hello)


    def test_update_url_is_resolved(self):
        url = reverse('update', args=[1])
        print(f"Testing '{url}' URL")

        self.assertEqual(resolve(url).func, updatetask)


    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=[1])
        print(f"Testing '{url}' URL")

        self.assertEqual(resolve(url).func, deletetask)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tasks_url = reverse('tasks')
        self.sleep = time.sleep(3)
        self.test_case_task = Task.objects.create(
            title = 'test case task'
        )
        self.update_url = reverse('update', args=[self.test_case_task.id])
        self.delete_url = reverse('delete', args=[self.test_case_task.id])



    def test_tasks_GET(self):

        response = self.client.get(self.tasks_url)

        print(f'Testing Staus response code..')
        self.assertEqual(response.status_code, 200)
        print(f'Testing Template used in response..')
        self.assertTemplateUsed(response, 'tasks.html')

    def test_tasks_add_new_task_post(self):
        response = self.client.post(self.tasks_url, data={'task':self.test_case_task})

        print(f"Testing '{self.tasks_url}' URL, POST new data")
        self.assertEqual(response.status_code, 200)
        print(f"Testing data posted if exists")
        self.assertEqual(Task.objects.filter(title__exact=self.test_case_task.title).exists(), True)

    def test_update_url_edit_task_post(self):
        print(f"Testing {self.update_url} URL edit the task")
        response = self.client.post(self.update_url, data={'title': 'updated title', 'Completed': True})

        print(f"Testing {self.update_url} URL response code if 302 redirect")
        self.assertEqual(response.status_code, 302)
        print(f"Testing {self.update_url} URL is the task title get updated correctly")
        self.assertTrue(Task.objects.filter(title__exact='updated title').exists())
        print(f"Testing {self.update_url} URL is the task status get updated correctly")
        self.assertTrue(Task.objects.get(id=self.test_case_task.id).Completed)


    def test_delete_task_url_post(self):
        print(f"Testing {self.delete_url} URL deleting the task")
        res = self.client.post(self.delete_url)

        print(f"Testing {self.delete_url} URL response code if 302 redirec")
        self.assertEqual(res.status_code, 302)
        print(f"Testing {self.delete_url} if the database tasks is empty after delete")
        self.assertEqual(Task.objects.all().count(), 0)