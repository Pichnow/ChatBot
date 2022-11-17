pip install chatterbot


from chatterbot import ChatBot
chatbot = ChatBot("Rosmeri")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hola",
    "¿Hola cómo estás?",
    "¿Qué haces?",
    "Que lindo día hace hoy.",
    "Espero tengas un lindodía"
   
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)


response = chatbot.get_response("Good morning!")
print(response)


