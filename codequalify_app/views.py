import openai
import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
@require_http_methods(["POST"])
def chat_with_openai(request):

    # プロンプトからメッセージを取得
    user_input     = request.POST.get('message')
    openai.api_key = settings.OPENAI_API_KEY

    # メッセージに対する回答を設定
    response = openai.Completion.create(
        engine            = "text-davinci-003", # 使用するエンジンを指定
        prompt            = user_input,         # 入力されたメッセージ
        max_tokens        = 150,                # 単語の数
        top_p             = 1.0,                # 上位10個まで表示
        frequency_penalty = 0.0                 # 同じ単語を繰り返し使う文章にする際に設定
    )

    # 回答をフロント側に送信
    return render(request, 'codequalify_app/chat.html', context={'response': response.choices[0].text.strip()})

    '''
    return JsonResponse({
        'response': response.choices[0].text.strip()
    })
    '''