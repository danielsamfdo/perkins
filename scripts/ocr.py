from web3 import Web3, HTTPProvider
from solc import compile_source
import requests
import json
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from eth_utils import keccak
import contextlib
os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", "/var/www/sunfinite.tech/gkey.json")
def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    s = '\n'.join([text.description for text in texts])
    return s
