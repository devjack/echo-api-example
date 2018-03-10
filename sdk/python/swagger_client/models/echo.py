# coding: utf-8

"""
    Echo example

    A simple API to echo back messages.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Echo(object):
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
        'hello': 'str',
        'echo': 'str'
    }

    attribute_map = {
        'hello': 'hello',
        'echo': 'echo'
    }

    def __init__(self, hello=None, echo=None):  # noqa: E501
        """Echo - a model defined in Swagger"""  # noqa: E501

        self._hello = None
        self._echo = None
        self.discriminator = None

        if hello is not None:
            self.hello = hello
        if echo is not None:
            self.echo = echo

    @property
    def hello(self):
        """Gets the hello of this Echo.  # noqa: E501


        :return: The hello of this Echo.  # noqa: E501
        :rtype: str
        """
        return self._hello

    @hello.setter
    def hello(self, hello):
        """Sets the hello of this Echo.


        :param hello: The hello of this Echo.  # noqa: E501
        :type: str
        """

        self._hello = hello

    @property
    def echo(self):
        """Gets the echo of this Echo.  # noqa: E501


        :return: The echo of this Echo.  # noqa: E501
        :rtype: str
        """
        return self._echo

    @echo.setter
    def echo(self, echo):
        """Sets the echo of this Echo.


        :param echo: The echo of this Echo.  # noqa: E501
        :type: str
        """

        self._echo = echo

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Echo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other