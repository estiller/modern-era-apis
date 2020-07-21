# coding: utf-8

"""
    Library API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.books_api import BooksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBooksApi(unittest.TestCase):
    """BooksApi unit test stubs"""

    def setUp(self):
        self.api = api.books_api.BooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_book(self):
        """Test case for delete_book

        """
        pass

    def test_delete_book_borrower(self):
        """Test case for delete_book_borrower

        """
        pass

    def test_get_book(self):
        """Test case for get_book

        """
        pass

    def test_get_book_borrower(self):
        """Test case for get_book_borrower

        """
        pass

    def test_get_books(self):
        """Test case for get_books

        """
        pass

    def test_put_book(self):
        """Test case for put_book

        """
        pass

    def test_put_book_borrower(self):
        """Test case for put_book_borrower

        """
        pass


if __name__ == '__main__':
    unittest.main()