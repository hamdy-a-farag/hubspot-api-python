# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.extensions.cards.configuration import Configuration


class IntegratorObjectResultActionsInner(object):
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
    openapi_types = {
        "type": "str",
        "confirmation": "ActionConfirmationBody",
        "http_method": "str",
        "url": "str",
        "label": "str",
        "property_names_included": "list[str]",
        "width": "int",
        "height": "int",
    }

    attribute_map = {
        "type": "type",
        "confirmation": "confirmation",
        "http_method": "httpMethod",
        "url": "url",
        "label": "label",
        "property_names_included": "propertyNamesIncluded",
        "width": "width",
        "height": "height",
    }

    def __init__(self, type="IFRAME", confirmation=None, http_method=None, url=None, label=None, property_names_included=None, width=None, height=None, local_vars_configuration=None):  # noqa: E501
        """IntegratorObjectResultActionsInner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._confirmation = None
        self._http_method = None
        self._url = None
        self._label = None
        self._property_names_included = None
        self._width = None
        self._height = None
        self.discriminator = None

        self.type = type
        if confirmation is not None:
            self.confirmation = confirmation
        self.http_method = http_method
        self.url = url
        if label is not None:
            self.label = label
        self.property_names_included = property_names_included
        self.width = width
        self.height = height

    @property
    def type(self):
        """Gets the type of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The type of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntegratorObjectResultActionsInner.


        :param type: The type of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["IFRAME"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def confirmation(self):
        """Gets the confirmation of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The confirmation of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: ActionConfirmationBody
        """
        return self._confirmation

    @confirmation.setter
    def confirmation(self, confirmation):
        """Sets the confirmation of this IntegratorObjectResultActionsInner.


        :param confirmation: The confirmation of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type confirmation: ActionConfirmationBody
        """

        self._confirmation = confirmation

    @property
    def http_method(self):
        """Gets the http_method of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The http_method of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this IntegratorObjectResultActionsInner.


        :param http_method: The http_method of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type http_method: str
        """
        if self.local_vars_configuration.client_side_validation and http_method is None:  # noqa: E501
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501
        allowed_values = ["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and http_method not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `http_method` ({0}), must be one of {1}".format(http_method, allowed_values))  # noqa: E501

        self._http_method = http_method

    @property
    def url(self):
        """Gets the url of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The url of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IntegratorObjectResultActionsInner.


        :param url: The url of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def label(self):
        """Gets the label of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The label of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IntegratorObjectResultActionsInner.


        :param label: The label of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def property_names_included(self):
        """Gets the property_names_included of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The property_names_included of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_names_included

    @property_names_included.setter
    def property_names_included(self, property_names_included):
        """Sets the property_names_included of this IntegratorObjectResultActionsInner.


        :param property_names_included: The property_names_included of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type property_names_included: list[str]
        """
        if self.local_vars_configuration.client_side_validation and property_names_included is None:  # noqa: E501
            raise ValueError("Invalid value for `property_names_included`, must not be `None`")  # noqa: E501

        self._property_names_included = property_names_included

    @property
    def width(self):
        """Gets the width of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The width of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this IntegratorObjectResultActionsInner.


        :param width: The width of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type width: int
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this IntegratorObjectResultActionsInner.  # noqa: E501


        :return: The height of this IntegratorObjectResultActionsInner.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this IntegratorObjectResultActionsInner.


        :param height: The height of this IntegratorObjectResultActionsInner.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntegratorObjectResultActionsInner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegratorObjectResultActionsInner):
            return True

        return self.to_dict() != other.to_dict()