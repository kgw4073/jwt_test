import json
from rest_framework.renderers import JSONRenderer
from selling.models import SellingPost
class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, meida_type=None, renderer_context=None):
        a = SellingPost.objects.get(title=data.title)
        print('aaaaaaaaa', a)
        title = a.title
        content = a.content
        print('title, content ')

        return json.dumps({
            'title': title,
            'content': content
        })