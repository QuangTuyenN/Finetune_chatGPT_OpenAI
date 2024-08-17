# import openai
#
# response = openai.File.create(
#   file=open("datafinetune.jsonl", "rb"),
#   purpose='fine-tune'
# )
#
# print(response)

from openai import OpenAI
import os
from apikey import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()


response_openai_file = client.files.create(
  file=open("datafinetune.jsonl", "rb"),
  purpose="fine-tune"
)
print(response_openai_file)
# {
#   "object": "file",
#   "id": "file-kTPxsdHNFhT755CFyFkV68Pi",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 8385,
#   "created_at": 1692801844,
#   "status": "uploaded",
#   "status_details": null
# }

# FileObject(id='file-VFaTUgkPsXz30lfHwNNpt9kl', bytes=73083, created_at=1719389095, filename='datafinetune.jsonl', object='file', purpose='fine-tune', status='processed', status_details=None)



