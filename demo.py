from text.logger import logging
from text.exception import CustomException
import sys

from text.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("text-speech-live-2024", "dataset.zip", "dataset.zip")