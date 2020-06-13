# coding: utf-8

"""
    Library API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_book(self, book_id, **kwargs):  # noqa: E501
        """delete_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_book(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_book_with_http_info(book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_book_with_http_info(book_id, **kwargs)  # noqa: E501
            return data

    def delete_book_with_http_info(self, book_id, **kwargs):  # noqa: E501
        """delete_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_book_with_http_info(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `delete_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_book_borrower(self, book_id, **kwargs):  # noqa: E501
        """delete_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_book_borrower(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_book_borrower_with_http_info(book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_book_borrower_with_http_info(book_id, **kwargs)  # noqa: E501
            return data

    def delete_book_borrower_with_http_info(self, book_id, **kwargs):  # noqa: E501
        """delete_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_book_borrower_with_http_info(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_book_borrower" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `delete_book_borrower`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}/borrower', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_book(self, book_id, **kwargs):  # noqa: E501
        """get_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_book(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: Book
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_book_with_http_info(book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_book_with_http_info(book_id, **kwargs)  # noqa: E501
            return data

    def get_book_with_http_info(self, book_id, **kwargs):  # noqa: E501
        """get_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_book_with_http_info(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: Book
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `get_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Book',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_book_borrower(self, book_id, **kwargs):  # noqa: E501
        """get_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_book_borrower(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_book_borrower_with_http_info(book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_book_borrower_with_http_info(book_id, **kwargs)  # noqa: E501
            return data

    def get_book_borrower_with_http_info(self, book_id, **kwargs):  # noqa: E501
        """get_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_book_borrower_with_http_info(book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int book_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_book_borrower" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `get_book_borrower`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}/borrower', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_books(self, **kwargs):  # noqa: E501
        """get_books  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_books(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Book]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_books_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_books_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_books_with_http_info(self, **kwargs):  # noqa: E501
        """get_books  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_books_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Book]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_books" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Book]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_book(self, body, book_id, **kwargs):  # noqa: E501
        """put_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_book(body, book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Book body: (required)
        :param int book_id: (required)
        :return: Book
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_book_with_http_info(body, book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_book_with_http_info(body, book_id, **kwargs)  # noqa: E501
            return data

    def put_book_with_http_info(self, body, book_id, **kwargs):  # noqa: E501
        """put_book  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_book_with_http_info(body, book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Book body: (required)
        :param int book_id: (required)
        :return: Book
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_book`")  # noqa: E501
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `put_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Book',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_book_borrower(self, body, book_id, **kwargs):  # noqa: E501
        """put_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_book_borrower(body, book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param int book_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_book_borrower_with_http_info(body, book_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_book_borrower_with_http_info(body, book_id, **kwargs)  # noqa: E501
            return data

    def put_book_borrower_with_http_info(self, body, book_id, **kwargs):  # noqa: E501
        """put_book_borrower  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_book_borrower_with_http_info(body, book_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param int book_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'book_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_book_borrower" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_book_borrower`")  # noqa: E501
        # verify the required parameter 'book_id' is set
        if ('book_id' not in params or
                params['book_id'] is None):
            raise ValueError("Missing the required parameter `book_id` when calling `put_book_borrower`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'book_id' in params:
            path_params['bookId'] = params['book_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/books/{bookId}/borrower', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
