# coding: utf-8

"""
    Library API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Book(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'borrower': 'OneOfBookBorrower'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'borrower': 'borrower'
    }

    def __init__(self, id=None, name=None, borrower=None):  # noqa: E501
        """Book - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._borrower = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if borrower is not None:
            self.borrower = borrower

    @property
    def id(self):
        """Gets the id of this Book.  # noqa: E501


        :return: The id of this Book.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Book.


        :param id: The id of this Book.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Book.  # noqa: E501


        :return: The name of this Book.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Book.


        :param name: The name of this Book.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def borrower(self):
        """Gets the borrower of this Book.  # noqa: E501


        :return: The borrower of this Book.  # noqa: E501
        :rtype: OneOfBookBorrower
        """
        return self._borrower

    @borrower.setter
    def borrower(self, borrower):
        """Sets the borrower of this Book.


        :param borrower: The borrower of this Book.  # noqa: E501
        :type: OneOfBookBorrower
        """

        self._borrower = borrower

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Book, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Book):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other