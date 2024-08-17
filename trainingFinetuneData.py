# import os
# import openai
# from apikey import OPENAI_API_KEY
#
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# file_id = "file-QvivaldXpnoFGwTna75qMf5L"
# response = openai.FineTuningJob.create(training_file=file_id,
#                                        model="gpt-3.5-turbo")
# print(response)
import os
from openai import OpenAI
from apikey import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

response_openai = client.fine_tuning.jobs.create(
  training_file="file-VFaTUgkPsXz30lfHwNNpt9kl",
  model="gpt-3.5-turbo"
)

print(response_openai)


# {
#   "object": "fine_tuning.job",
#   "id": "ftjob-eLvEAv6VEzXllDvPE9Qk45kz",
#   "model": "gpt-3.5-turbo-0613",
#   "created_at": 1692801986,
#   "finished_at": null,
#   "fine_tuned_model": null,
#   "organization_id": "org-sRhvEIyDb8hsq6q04MPW5ViJ",
#   "result_files": [],
#   "status": "created",
#   "validation_file": null,
#   "training_file": "file-yRdnc3zfVwTbvrn0pQ2dsN9I",
#   "hyperparameters": {
#     "n_epochs": 5
#   },
#   "trained_tokens": null
# }


# FineTuningJob(id='ftjob-tLdjhm3wyz2Azuix0FIwv9VZ', created_at=1719389127, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(n_epochs='auto', batch_size='auto', learning_rate_multiplier='auto'), model='gpt-3.5-turbo-0125', object='fine_tuning.job', organization_id='org-UmdVlF11tv5QeH20JuAh9qKC', result_files=[], seed=2015076452, status='validating_files', trained_tokens=None, training_file='file-VFaTUgkPsXz30lfHwNNpt9kl', validation_file=None, estimated_finish=None, integrations=[], user_provided_suffix=None)
