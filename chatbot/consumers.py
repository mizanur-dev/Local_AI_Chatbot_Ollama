import json
from channels.generic.websocket import AsyncWebsocketConsumer
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_message = text_data_json['message']
        model_name = text_data_json.get('model', 'llama2')

        try:
            llm = ChatOllama(
                model=model_name,
                temperature=0.7,
                num_predict=250,
                timeout=30,
            )

            prompt = ChatPromptTemplate.from_messages([
                ("system", (
                    "You are a helpful assistant. Provide responses in plain, natural conversational text only. "
                    "Strictly DO NOT use Markdown, bolding (**), italics (*), headers (#), or bullet points. "
                    "Do not use code blocks. Just plain sentences."
                )),
                ("user", "{input}")
            ])

            chain = prompt | llm | StrOutputParser()
            
            # Use astream for streaming responses
            full_reply = ""
            async for chunk in chain.astream({"input": user_message}):
                full_reply += chunk
            
            await self.send(text_data=json.dumps({
                'reply': full_reply
            }))

        except Exception as e:
            await self.send(text_data=json.dumps({
                'error': str(e)
            }))
