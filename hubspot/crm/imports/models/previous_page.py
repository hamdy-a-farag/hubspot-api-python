# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.imports.configuration import Configuration


class PreviousPage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"before": "str", "link": "str"}

    attribute_map = {"before": "before", "link": "link"}

    def __init__(
        self, before=None, link=None, local_vars_configuration=None
    ):  # noqa: E501
        """PreviousPage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._before = None
        self._link = None
        self.discriminator = None

        self.before = before
        if link is not None:
            self.link = link

    @property
    def before(self):
        """Gets the before of this PreviousPage.  # noqa: E501


        :return: The before of this PreviousPage.  # noqa: E501
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this PreviousPage.


        :param before: The before of this PreviousPage.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and before is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `before`, must not be `None`"
            )  # noqa: E501

        self._before = before

    @property
    def link(self):
        """Gets the link of this PreviousPage.  # noqa: E501


        :return: The link of this PreviousPage.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this PreviousPage.


        :param link: The link of this PreviousPage.  # noqa: E501
        :type: str
        """

        self._link = link

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, PreviousPage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreviousPage):
            return True

        return self.to_dict() != other.to_dict()
