from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
from django.shortcuts import render

# LangChain Imports
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ChatAPIView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        user_message = serializer.validated_data.get('message')
        model_name = serializer.validated_data.get('model')

        try:
            # 1. Initialize Model 
            # num_thread is added to ensure CPU/GPU coordination is efficient
            llm = ChatOllama(
                model=model_name,
                temperature=0.7,
                num_predict=250, 
                timeout=30,  # Prevents infinite loading if Ollama hangs
            )

            # 2. Strict System Prompt
            # Added "No special characters" to force natural speech
            prompt = ChatPromptTemplate.from_messages([
                ("system", (
                    "You are a helpful assistant. Provide responses in plain, natural conversational text only. "
                    "Strictly DO NOT use Markdown, bolding (**), italics (*), headers (#), or bullet points. "
                    "Do not use code blocks. Just plain sentences."
                )),
                ("user", "{input}")
            ])

            # 3. Execute Chain
            chain = prompt | llm | StrOutputParser()
            ai_reply = chain.invoke({"input": user_message})

            # 4. Final Polish
            # This regex/replace is a safety net to remove any stray markdown the model might include
            clean_reply = ai_reply.replace("**", "").replace("__", "").replace("#", "").strip()
            
            return Response({
                "status": "success",
                "reply": clean_reply
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def index(request):
    return render(request, 'index.html')