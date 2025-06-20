#!/usr/bin/env python3

import os
import io
from .functions import (
    upload as d,
    deal_status, 
    get_uploads as getUploads, 
    download as _download,
    get_file_info as getFileInfo,
    get_balance as getBalance,
    get_api_key as getApiKey,
    ipns_generate_key as ipnsGenerateKey,
    ipns_publish_record as ipnsPublishRecord,
    get_ipns_record as getIpnsRecord,
    remove_ipns_record as removeIpnsRecord,
    create_wallet as createWallet
)


class Lighthouse:
    def __init__(self, token: str = ""):
        self.token = token or os.environ.get("LIGHTHOUSE_TOKEN", "")
        if not self.token:
            raise Exception(
                "No token provided: Please provide a token or set the LIGHTHOUSE_TOKEN environment variable"
            )

    def upload(self, source: str, tag: str = ''):
        """
        Upload a file or directory to the Lighthouse.

        :param source: str, path to file or directory
        :return: t.Upload, the upload result
        """
        try:
            return d.upload(source, self.token, tag)
        except Exception as e:
            raise e

    def uploadBlob(self, source: io.BufferedReader, filename: str, tag: str = ''):
        """
        Upload Blob a file or directory to the Lighthouse.

        :param source: str, path to file or directory
        :return: t.Upload, the upload result
        """
        if not (hasattr(source, 'read') and hasattr(source, 'close')):
            raise TypeError("source must have 'read' and 'close' methods")
        try:
            return d.uploadBlob(source, filename, self.token, tag)
        except Exception as e:
            raise e
    
    def getBalance(self):
        """
        Retrieve the balance information of a user from the Lighthouse.

        :param publicKey: str, The public key of the user.
        :return: dict[str, any], A dictionary containing the data usage and data limit details.
        """
        try:
            return getBalance.get_balance(self.token)
        except Exception as e:
            raise e
    
    def generateKey(self):
        """
        Generate a new IPNS key for the authenticated user.

        :return: dict, The generated IPNS key information.
        """
        try:
            return ipnsGenerateKey.ipns_generate_key(self.token)
        except Exception as e:
            raise e

    def publishRecord(self, cid: str, keyName: str):
        """
        Publish an IPNS record for a given CID and key name.

        :param cid: str, Content Identifier to publish
        :param keyName: str, Name of the IPNS key to use
        :return: dict, The published IPNS record information
        """
        try:
            return ipnsPublishRecord.ipns_publish_record(self.token, cid, keyName)
        except Exception as e:
            raise e

    def getAllKeys(self):
        """
        Retrieves all IPNS records associated with the current token.

        :return: list A list of IPNS records retrieved using the provided token.
        """

        try:
            return getIpnsRecord.get_ipns_records(self.token)
        except Exception as e:
            raise e

    def removeKey(self, keyName: str):
        """
        Remove IPNS record of the given keyName

        :param keyName: str, Name of the IPNS key to use
        :return: dict, A dict of removed IPNS record.
        """

        try:
            return removeIpnsRecord.remove_ipns_record(self.token, keyName)
        except Exception as e:
            raise e
    
    @staticmethod
    def createWallet(password: str):
        """
        Creates a new wallet using the provided password.

        :param password: str, The password to secure the wallet.
        :return: dict, The wallet encrypted with the passowrd
        """
        try:
            return createWallet.create_wallet(password)
        except Exception as e:
            raise e

    @staticmethod
    def downloadBlob(dist: io.BufferedWriter, cid: str, chunk_size=1024*1024*10):
        """
        Download a Blob (file or directory) from the Lighthouse.

        :param dist: BufferedWriter, destination to write the downloaded data
        :param cid: str, Content Identifier for the data to be downloaded
        :param chunk_size: int, size of chunks in which the file will be downloaded (default: 10MB)
        :return: t.Upload, the download result
        """
        if not (hasattr(dist, 'read') and hasattr(dist, 'close')):
            raise TypeError("source must have 'read' and 'close' methods")
        try:
            return _download.download_file_into_writable(cid, dist, chunk_size)
        except Exception as e:
            raise e
            
    @staticmethod
    def getDealStatus(cid: str):
        """
        Get deal status from the Lighthouse.

        :param cid: str, content identifier
        :return: List[t.DealData], list of deal data
        """
        try:
            return deal_status.get_deal_status(cid)
        except Exception as e:
            raise e
    
    def getUploads(self, lastKey: str = None):
        """
        Get uploads from the Lighthouse.

        :param lastKey: To navigate to different pages of results
        :return: List[t.DealData], list of deal data
        """
        try:
            return getUploads.get_uploads(self.token, lastKey)
        except Exception as e:
            raise e

    @staticmethod
    def download(cid: str):
        """
        Download content from the Lighthouse using its Content Identifier (CID).

        :param cid: str, Content Identifier for the data to be downloaded
        :param useCidAsTag: bool, flag to use CID as a tag (default: False)
        :return: bytes, the downloaded content
        """
        try:
            return _download.get_file(cid)
        except Exception as e:
            raise e
    
    @staticmethod
    def getFileInfo(cid: str):
        """
        Retrieves information about a file using its CID (Content Identifier).

        :param cid: str, Content Identifier for the data to be downloaded
        :return: dict, A dictionary containing file information.
        """

        try:
            return getFileInfo.get_file_info(cid)
        except Exception as e:
            raise e
    
    @staticmethod
    def getApiKey(publicKey: str, signedMessage: str):
        """
        Generates and returns an API key for the given public key and signed message.

        :param publicKey: str, The public key associated with the user.
        :param signedMessage: str, The message signed by the user's private key.
        :return: dict, A dict with generated API key.
        """


        try:
            return getApiKey.get_api_key(publicKey, signedMessage)
        except Exception as e:
            raise e

    def getTagged(self, tag: str):
        """
        Retrieve an upload from the Lighthouse using its tag.

        :param tag: str, tag associated with the file or directory
        :return: t.Upload, the upload result
        """
        try:
            return _download.getTaggedCid(tag, self.token)
        except Exception as e:
            raise e

