from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api.testcode.factories import NoticeFactory
from api.testcode.factories import UserFactory


class NoticeUpdateTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

        # Old setup data code
        # user_data = {
        #     "username": "hello",
        #     "password": "12345678"
        # }
        # user = User.objects.create_user(**user_data)
        # cls.client.login(**user_data)
        #
        # cls.notice = Notice.objects.create(
        #     user=user,
        #     title="test title",
        #     context="test context"
        # )
        #
        # cls.url = f"/api/testcode/notice/{cls.notice.id}/"

        user = UserFactory()
        cls.client.login(username=user.username, password=user.password)
        cls.notice = NoticeFactory(user=user)
        
        cls.url = reverse("notice-detail", kwargs={"pk": cls.notice.id})

    def setUp(self):
        self.data = {
            "title": "Modified title",
            "context": "Modified context"
        }
    
    def test_notice_update_success(self):
        response  = self.client.patch(
            self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.data["title"])
        self.assertEqual(response.data["context"], self.data["context"])

    def test_notice_update_with_missing_title(self):
        self.data.pop("title")
        response  = self.client.patch(
            self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.notice.title)
        self.assertEqual(response.data["context"], self.data["context"])
        
    def test_notice_update_with_missing_context(self):
        self.data.pop("context")
        response  = self.client.patch(
            self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.data["title"])
        self.assertEqual(response.data["context"], self.notice.context)
