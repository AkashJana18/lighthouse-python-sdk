#!/usr/bin/env python3

import io
import os
from typing import Any, Dict

from .functions import create_wallet as createWallet
from .functions import deal_status
from .functions import download as _download
from .functions import get_api_key as getApiKey
from .functions import get_balance as getBalance
from .functions import get_file_info as getFileInfo
from .functions import get_ipns_record as getIpnsRecord
from .functions import get_uploads as getUploads
from .functions import ipns_generate_key as ipnsGenerateKey
from .functions import ipns_publish_record as ipnsPublishRecord
from .functions import kavach_generate
from .functions import remove_ipns_record as removeIpnsRecord
from .functions import upload as d


class Lighthouse:
    def __init__(self, token: str = ""):
        self.token = token or os.environ.get("LIGHTHOUSE_TOKEN", "")
        if not self.token:
            raise Exception(
                "No token provided: Please provide a token or set the LIGHTHOUSE_TOKEN environment variable"
            )

    def upload(self, source: str, tag: str = ''):
        try:
            return d.upload(source, self.token, tag)
        except Exception as e:
            raise e

    def uploadBlob(self, source: io.BufferedReader, filename: str, tag: str = ''):
        if not (hasattr(source, 'read') and hasattr(source, 'close')):
            raise TypeError("source must have 'read' and 'close' methods")
        try:
            return d.uploadBlob(source, filename, self.token, tag)
        except Exception as e:
            raise e

    def getBalance(self):
        try:
            return getBalance.get_balance(self.token)
        except Exception as e:
            raise e

    def generateKey(self):
        try:
            return ipnsGenerateKey.ipns_generate_key(self.token)
        except Exception as e:
            raise e

    def publishRecord(self, cid: str, keyName: str):
        try:
            return ipnsPublishRecord.ipns_publish_record(self.token, cid, keyName)
        except Exception as e:
            raise e

    def getAllKeys(self):
        try:
            return getIpnsRecord.get_ipns_records(self.token)
        except Exception as e:
            raise e

    def removeKey(self, keyName: str):
        try:
            return removeIpnsRecord.remove_ipns_record(self.token, keyName)
        except Exception as e:
            raise e

    @staticmethod
    def createWallet(password: str):
        try:
            return createWallet.create_wallet(password)
        except Exception as e:
            raise e

    @staticmethod
    def downloadBlob(dist: io.BufferedWriter, cid: str, chunk_size=1024*1024*10):
        if not (hasattr(dist, 'read') and hasattr(dist, 'close')):
            raise TypeError("source must have 'read' and 'close' methods")
        try:
            return _download.download_file_into_writable(cid, dist, chunk_size)
        except Exception as e:
            raise e

    @staticmethod
    def getDealStatus(cid: str):
        try:
            return deal_status.get_deal_status(cid)
        except Exception as e:
            raise e

    def getUploads(self, lastKey: str = None):
        try:
            return getUploads.get_uploads(self.token, lastKey)
        except Exception as e:
            raise e

    @staticmethod
    def download(cid: str):
        try:
            return _download.get_file(cid)
        except Exception as e:
            raise e

    @staticmethod
    def getFileInfo(cid: str):
        try:
            return getFileInfo.get_file_info(cid)
        except Exception as e:
            raise e

    @staticmethod
    def getApiKey(publicKey: str, signedMessage: str):
        try:
            return getApiKey.get_api_key(publicKey, signedMessage)
        except Exception as e:
            raise e

    def getTagged(self, tag: str):
        try:
            return _download.getTaggedCid(tag, self.token)
        except Exception as e:
            raise e

    async def generateEncryptionKey(self, threshold: int = 3, key_count: int = 5) -> Dict[str, Any]:
        """
        Generate a master encryption key and threshold-based key shards.

        :param threshold: Minimum number of shards required to reconstruct the master key.
        :param key_count: Total number of shards to generate (must be >= threshold).
        :return: Dict with 'masterKey' and 'keyShards'
        """
        try:
            return await kavach_generate(threshold, key_count)
        except Exception as e:
            raise e
