from langchain_core.language_models import GenericFakeChatModel
from langchain_core.messages import AIMessage, SystemMessage
from faker import Faker
import time
import random


def create_message_generator(fake: Faker):
    while True:
        random_sentence = fake.sentence(nb_words=10, variable_nb_words=True)
        time.sleep(1 + random.random() * 2)
        yield AIMessage(content=random_sentence)


def create_llm(fake):
    messages = create_message_generator(fake)
    llm = GenericFakeChatModel(messages=messages)

    return llm
