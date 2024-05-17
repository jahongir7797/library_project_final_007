from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book
from books.serializers import BookSerializer


from rest_framework import generics

# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

       
class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDeleteApiView(APIView):
    
    def delete(self,request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': True,
                'message':'seccesfully deleted'
            } , )
        except Exception:
            return Response({
                'status': False,
                'Message': 'Book is not found'
            }   )         
    

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookUpdateApiView(APIView):
    
   def put(self, requst, pk):
        book = Book.objects.get(id=pk) 
        date = requst.date 
        serializer = BookSerializer(instance=book, data=date, partial=True)
        if serializer.is_valid(raise_exception=True):
          book_saved = serializer.save()
        return Response(
            {'status': True,
             'message': f'Book {book_saved} updated successfully '
             }
        )        
    
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer      

        
    
    
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer     
    
class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    