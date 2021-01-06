# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class InstitutionStatus(object):
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
        'item_logins': 'ProductStatus',
        'transactions_updates': 'ProductStatus',
        'auth': 'ProductStatus',
        'balance': 'ProductStatus',
        'identity': 'ProductStatus'
    }

    attribute_map = {
        'item_logins': 'item_logins',
        'transactions_updates': 'transactions_updates',
        'auth': 'auth',
        'balance': 'balance',
        'identity': 'identity'
    }

    def __init__(self, item_logins=None, transactions_updates=None, auth=None, balance=None, identity=None, local_vars_configuration=None):  # noqa: E501
        """InstitutionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_logins = None
        self._transactions_updates = None
        self._auth = None
        self._balance = None
        self._identity = None
        self.discriminator = None

        if item_logins is not None:
            self.item_logins = item_logins
        if transactions_updates is not None:
            self.transactions_updates = transactions_updates
        if auth is not None:
            self.auth = auth
        if balance is not None:
            self.balance = balance
        if identity is not None:
            self.identity = identity

    @property
    def item_logins(self):
        """Gets the item_logins of this InstitutionStatus.  # noqa: E501


        :return: The item_logins of this InstitutionStatus.  # noqa: E501
        :rtype: ProductStatus
        """
        return self._item_logins

    @item_logins.setter
    def item_logins(self, item_logins):
        """Sets the item_logins of this InstitutionStatus.


        :param item_logins: The item_logins of this InstitutionStatus.  # noqa: E501
        :type item_logins: ProductStatus
        """

        self._item_logins = item_logins

    @property
    def transactions_updates(self):
        """Gets the transactions_updates of this InstitutionStatus.  # noqa: E501


        :return: The transactions_updates of this InstitutionStatus.  # noqa: E501
        :rtype: ProductStatus
        """
        return self._transactions_updates

    @transactions_updates.setter
    def transactions_updates(self, transactions_updates):
        """Sets the transactions_updates of this InstitutionStatus.


        :param transactions_updates: The transactions_updates of this InstitutionStatus.  # noqa: E501
        :type transactions_updates: ProductStatus
        """

        self._transactions_updates = transactions_updates

    @property
    def auth(self):
        """Gets the auth of this InstitutionStatus.  # noqa: E501


        :return: The auth of this InstitutionStatus.  # noqa: E501
        :rtype: ProductStatus
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this InstitutionStatus.


        :param auth: The auth of this InstitutionStatus.  # noqa: E501
        :type auth: ProductStatus
        """

        self._auth = auth

    @property
    def balance(self):
        """Gets the balance of this InstitutionStatus.  # noqa: E501


        :return: The balance of this InstitutionStatus.  # noqa: E501
        :rtype: ProductStatus
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this InstitutionStatus.


        :param balance: The balance of this InstitutionStatus.  # noqa: E501
        :type balance: ProductStatus
        """

        self._balance = balance

    @property
    def identity(self):
        """Gets the identity of this InstitutionStatus.  # noqa: E501


        :return: The identity of this InstitutionStatus.  # noqa: E501
        :rtype: ProductStatus
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this InstitutionStatus.


        :param identity: The identity of this InstitutionStatus.  # noqa: E501
        :type identity: ProductStatus
        """

        self._identity = identity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, InstitutionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionStatus):
            return True

        return self.to_dict() != other.to_dict()
