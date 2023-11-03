from django.shortcuts import render
import openai

def askGHQ(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        prevQuestions = request.POST.get('prevQ')
        prevResponses = request.POST.get('prevR')
        resp = ""

        prevQlist = []
        prevRlist = []

        preguntas_respuestas = []

        if isinstance(prevQuestions, str) and isinstance(prevResponses, str):
            prevQlist = prevQuestions.split("^$^")
            prevRlist = prevResponses.split("^$^")
        else:
            prevQuestions = ""
            prevResponses = ""

        contextoMensajes =[
                    {"role": "system", "content": "You are a helpful assistant."},
                ]
        
        for i in range(len(prevQlist)):
            contextoMensajes.append({"role": "user", "content": prevQlist[i]})
            contextoMensajes.append({"role": "assistant", "content": prevRlist[i] })

            if prevQlist[i] != "" and prevRlist[i] != "":
                preguntas_respuestas.append({'pregunta': prevQlist[i], 'respuesta': prevRlist[i]})
            

        contextoMensajes.append({"role": "user", "content": texto}) #ultima pregunta enviada
        #llamada a la API 
        
        openai.api_key = "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"
        openai.Model.list()

        MODEL = "gpt-3.5-turbo"
    
        def preguntar(contexto):
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=contexto,
                temperature=0,
                max_tokens=100, 
            )
            return response["choices"][0]["message"]["content"]

        resp = preguntar(contextoMensajes)
        print(resp)
        

        responseGHQ = resp
        preguntas_respuestas.append({'pregunta': texto, 'respuesta': resp})

        prevQuestions = prevQuestions + "^$^" + texto
        prevResponses = prevResponses + "^$^" + resp

        print(prevQuestions)
        print(prevResponses)

        return render(request, 'mi_aplicacion/AskGHQ.html', {'preguntas_respuestas': preguntas_respuestas,'question': texto ,'responseGHQ': responseGHQ,'prevQ': prevQuestions,'prevR': prevResponses})
    return render(request, 'mi_aplicacion/AskGHQ.html', {'preguntas_respuestas': "", 'question': "",'responseGHQ': ""})

