from django.shortcuts import render
from .models import Question, UserResponse, CreditScore
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def calculate_credit_score(user_responses):
    score = 0
    for response in user_responses:
        if response.answer == 'A':
            score += 10
        elif response.answer == 'B':
            score += 5
        elif response.answer == 'C':
            score += 15
        elif response.answer == 'D':
            score += 0
    return score


def question_view(request):
    questions = Question.objects.all()
    questions_json = json.dumps([{'id': q.id, 'text': q.text} for q in questions])
    return render(request, "credit_score/questions.html", {"questions_json": questions_json})

@csrf_exempt 
def submit_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        try:
            question = Question.objects.get(id=data["question_id"])
            answer = data["answer"]
            UserResponse.objects.create(user=request.user, question=question, answer=answer)
            return JsonResponse({"status": "success"})
        except Question.DoesNotExist:
            return JsonResponse({"status": "failed", "error": "Question not found"}, status=404)
    return JsonResponse({"status": "failed"}, status=400)


def results_view(request):
    user_responses = UserResponse.objects.filter(user=request.user)
    credit_score = calculate_credit_score(user_responses)
    credit_score_record, created = CreditScore.objects.get_or_create(user=request.user)
    credit_score_record.score = credit_score
    credit_score_record.save()
    return render(request, "credit_score/results.html", {"credit_score": credit_score})