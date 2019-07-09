from rest_framework.renderers import JSONRenderer

# https://github.com/jpadilla/django-rest-framework-jsonp 参照


class JSONPRenderer(JSONRenderer):
    """
    Renderer which serializes to json,
    wrapping the json output in a callback function.
    """

    media_type = 'application/javascript'
    format = 'jsonp'
    default_callback = 'callback'
    charset = 'utf-8'

    def render(self, data, params={}, callback_parameter=None):
        """
        Renders into jsonp, wrapping the json output in a callback function.
        Clients may set the callback function name using a query parameter
        on the URL, for example: ?callback=exampleCallbackName
        """
        callback = params.get(callback_parameter, self.default_callback)
        json = super(JSONPRenderer, self).render(
            data, accepted_media_type=None, renderer_context=None
        )
        return callback.encode(self.charset) + b'(' + json + b');'


def get_query_params(request):
    if hasattr(request, 'query_params'):
        params = request.query_params
    else:
        # DRF < 3.2
        params = request.QUERY_PARAMS

    return params

