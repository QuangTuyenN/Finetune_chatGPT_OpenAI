python 3.9

RUN pip install openai

RUN pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai langchain-chroma bs4

Prepare data to finetune on .jsonl format. role: system is the context you give

RUN python sendDataToGpt.py to send jsonl data to openai and when print response you will get the id of file

Change the id file in trainingFineTuneData.py and RUN python trainingFineTuneData.py

Change model name on email you get in useFinetuneModel.py file


