from rest_framework.views import APIView
from rest_framework.response import Response
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

  
class VoiceAssistantAPIView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        llm = ChatOllama(model="llama3.1:8b", temperature=0.5, num_predict=80) 
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a voice assistant. Give very short, natural answers in 1 sentence. No markdown."),
            ("user", "{input}")
        ])
        
        chain = prompt | llm | StrOutputParser()
        reply = chain.invoke({"input": user_message})
        return Response({"reply": reply})