import openai
import render
from django.http                  import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf                  import settings

@csrf_exempt
@require_http_methods(["POST"])
def chat_with_openai(request):

    # プロンプトからメッセージを取得
    user_input     = request.POST.get('message')
    openai.api_key = settings.OPENAI_API_KEY

    # メッセージに対する回答を設定
    response = openai.ChatCompletion.create(
        model    = "gpt-4",
        messages = [
            {"role": "user", "content": user_input},
        ],
    )

    # 回答をフロント側に送信
    return render(
        request, 
        'codequalify_app/chat.html', 
        context = {'response': response.choices[0]["message"]["content"].strip()}
    )

    # 回答をフロント側に送信
    '''
    return JsonResponse({
        'response': response.choices[0]["message"]["content"].strip()
    })
    '''