# coding: utf-8

"""
    CrmPublicObjectsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.associations.v4.configuration import Configuration


class SimplePublicObjectWithAssociations(object):
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
        "associations": "dict[str, CollectionResponseAssociatedId]",
        "created_at": "datetime",
        "archived": "bool",
        "archived_at": "datetime",
        "properties_with_history": "dict[str, list[ValueWithTimestamp]]",
        "id": "str",
        "properties": "dict[str, str]",
        "updated_at": "datetime",
    }

    attribute_map = {
        "associations": "associations",
        "created_at": "createdAt",
        "archived": "archived",
        "archived_at": "archivedAt",
        "properties_with_history": "propertiesWithHistory",
        "id": "id",
        "properties": "properties",
        "updated_at": "updatedAt",
    }

    def __init__(
        self, associations=None, created_at=None, archived=None, archived_at=None, properties_with_history=None, id=None, properties=None, updated_at=None, local_vars_configuration=None
    ):  # noqa: E501
        """SimplePublicObjectWithAssociations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._associations = None
        self._created_at = None
        self._archived = None
        self._archived_at = None
        self._properties_with_history = None
        self._id = None
        self._properties = None
        self._updated_at = None
        self.discriminator = None

        if associations is not None:
            self.associations = associations
        self.created_at = created_at
        if archived is not None:
            self.archived = archived
        if archived_at is not None:
            self.archived_at = archived_at
        if properties_with_history is not None:
            self.properties_with_history = properties_with_history
        self.id = id
        self.properties = properties
        self.updated_at = updated_at

    @property
    def associations(self):
        """Gets the associations of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The associations of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: dict[str, CollectionResponseAssociatedId]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this SimplePublicObjectWithAssociations.


        :param associations: The associations of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type associations: dict[str, CollectionResponseAssociatedId]
        """

        self._associations = associations

    @property
    def created_at(self):
        """Gets the created_at of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The created_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SimplePublicObjectWithAssociations.


        :param created_at: The created_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def archived(self):
        """Gets the archived of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The archived of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SimplePublicObjectWithAssociations.


        :param archived: The archived of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type archived: bool
        """

        self._archived = archived

    @property
    def archived_at(self):
        """Gets the archived_at of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The archived_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this SimplePublicObjectWithAssociations.


        :param archived_at: The archived_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

    @property
    def properties_with_history(self):
        """Gets the properties_with_history of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The properties_with_history of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: dict[str, list[ValueWithTimestamp]]
        """
        return self._properties_with_history

    @properties_with_history.setter
    def properties_with_history(self, properties_with_history):
        """Sets the properties_with_history of this SimplePublicObjectWithAssociations.


        :param properties_with_history: The properties_with_history of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type properties_with_history: dict[str, list[ValueWithTimestamp]]
        """

        self._properties_with_history = properties_with_history

    @property
    def id(self):
        """Gets the id of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The id of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplePublicObjectWithAssociations.


        :param id: The id of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The properties of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SimplePublicObjectWithAssociations.


        :param properties: The properties of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type properties: dict[str, str]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def updated_at(self):
        """Gets the updated_at of this SimplePublicObjectWithAssociations.  # noqa: E501


        :return: The updated_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SimplePublicObjectWithAssociations.


        :param updated_at: The updated_at of this SimplePublicObjectWithAssociations.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, SimplePublicObjectWithAssociations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimplePublicObjectWithAssociations):
            return True

        return self.to_dict() != other.to_dict()
