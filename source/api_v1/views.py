import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers import ArticleSerializer
from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


# class ArticleCreateView(View):
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         slr = ArticleSerializer(data=data)
#         if slr.is_valid():
#             article = slr.save()
#             return JsonResponse(slr.data, safe=False)
#         else:
#             response = JsonResponse(slr.errors, safe=False)
#             response.status_code = 400
#             return response

class AddView(View):
    def post(self, request, *args,**kwargs):
        data = json.loads(request.body)
        try:
            data['A'] = float(data['A'])
            data['B'] = float(data['B'])
            if request.path.split('/')[3] == 'add':
                answer = data['A'] + data['B']
            elif request.path.split('/')[3] == 'subtract':
                answer = data['A'] - data['B']
            elif request.path.split('/')[3] == 'multiply':
                answer = data['A'] * data['B']
            elif request.path.split('/')[3] == 'divide':
                answer = data['A'] / data['B']
            else:
                answer = None
            return JsonResponse({
                'answer': answer
            })
        except Exception as e:
            response = JsonResponse({'error': str(e)})
            response.status_code = 400
            return response


# class ArticleListView(View):
#     def get(self, request, *args, **kwargs):
#         objects = Article.objects.all()
#         slr = ArticleSerializer(objects, many=True)
#         return JsonResponse(slr.data, safe=False)

class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs.keys():
            article = get_object_or_404(Article, pk=kwargs.get('pk'))
            slr = ArticleSerializer(article)
            return Response(slr.data)
        else:
            articles = Article.objects.all()
            slr = ArticleSerializer(articles, many=True)
            return Response(slr.data)

    def post(self, request, *args, **kwargs):
        slr = ArticleSerializer(data=request.data)
        if slr.is_valid():
            article = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        slr = ArticleSerializer(data=request.data)
        if slr.is_valid():
            article =slr.update(article, slr.validated_data)
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article.delete()
        return JsonResponse({"pk": kwargs.get('pk')})
