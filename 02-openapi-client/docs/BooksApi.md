# swagger_client.BooksApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_book**](BooksApi.md#delete_book) | **DELETE** /api/books/{bookId} | 
[**delete_book_borrower**](BooksApi.md#delete_book_borrower) | **DELETE** /api/books/{bookId}/borrower | 
[**get_book**](BooksApi.md#get_book) | **GET** /api/books/{bookId} | 
[**get_book_borrower**](BooksApi.md#get_book_borrower) | **GET** /api/books/{bookId}/borrower | 
[**get_books**](BooksApi.md#get_books) | **GET** /api/books | 
[**put_book**](BooksApi.md#put_book) | **PUT** /api/books/{bookId} | 
[**put_book_borrower**](BooksApi.md#put_book_borrower) | **PUT** /api/books/{bookId}/borrower | 

# **delete_book**
> delete_book(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
book_id = 56 # int | 

try:
    api_instance.delete_book(book_id)
except ApiException as e:
    print("Exception when calling BooksApi->delete_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_book_borrower**
> delete_book_borrower(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
book_id = 56 # int | 

try:
    api_instance.delete_book_borrower(book_id)
except ApiException as e:
    print("Exception when calling BooksApi->delete_book_borrower: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book**
> Book get_book(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
book_id = 56 # int | 

try:
    api_response = api_instance.get_book(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BooksApi->get_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_borrower**
> User get_book_borrower(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
book_id = 56 # int | 

try:
    api_response = api_instance.get_book_borrower(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BooksApi->get_book_borrower: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_books**
> list[Book] get_books()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()

try:
    api_response = api_instance.get_books()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BooksApi->get_books: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Book]**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_book**
> Book put_book(body, book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
body = swagger_client.Book() # Book | 
book_id = 56 # int | 

try:
    api_response = api_instance.put_book(body, book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BooksApi->put_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)|  | 
 **book_id** | **int**|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_book_borrower**
> User put_book_borrower(body, book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BooksApi()
body = swagger_client.User() # User | 
book_id = 56 # int | 

try:
    api_response = api_instance.put_book_borrower(body, book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BooksApi->put_book_borrower: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 
 **book_id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

