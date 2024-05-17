from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)
 
      
    def validate(self, date):
        title = date.get('title', None)
        author = date.get('author', None)
        
        #check title if it contain only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'KItob sarlavhasi harflardan tashkil topgan bolishi kerak'
                }
            )    
         #check title and author from database existance
        if Book.objects.filter(title=title, author= author).exists():
             raise ValidationError(
                 {
                     "status": False,
                     "message": "Kitob sarlavhasi va mualifi bir xil bo'lmasligi kerak"
                 }
             )   
        return date     