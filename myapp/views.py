from django.shortcuts import render
import openai

# Set up OpenAI API credentials
openai.api_key = "API Key"

def home(request):
    return render(request, "home.html")

def answer(request):
    if request.method == "POST":
        question = request.POST["question"]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the following question: {question}",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text.strip()
        return render(request, "answer.html", {"question": question, "answer": answer})
    else:
        return home(request)
