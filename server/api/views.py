from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import search_equity_by_name
from traceback import print_exc


@api_view(['POST'])
def search_equity_name(request):
    try:
        data = search_equity_by_name(request.data['search'])
        return Response({'success': True, 'data': data})
    except Exception as e:
        print(e)
        # INFO: if I setup clowdwatch traceback wil help he figureout the error if there's any
        print_exc()
        return Response({'success': False, 'error': 'Something went wrong!'}, status=500)
