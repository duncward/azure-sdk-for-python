# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class UpgradeMode(str, Enum):

    manual = "Manual"
    automatic = "Automatic"


class RetentionPeriod(str, Enum):

    session = "Session"
    persistent = "Persistent"


class CredentialDataFormat(str, Enum):

    rsa_encrypted = "RsaEncrypted"


class PromptFieldType(str, Enum):

    string = "String"
    secure_string = "SecureString"
    credential = "Credential"


class GatewayExpandOption(str, Enum):

    status = "status"
    download = "download"


class PowerShellExpandOption(str, Enum):

    output = "output"
