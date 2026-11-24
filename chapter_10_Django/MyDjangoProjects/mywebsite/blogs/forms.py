from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__" # use this if you want all the fields of the model to be used in the form. but we don't want all the fields to be used in the form, so we will use the below line instead of this.
        # For a certain fields use below line instead of the above line.
        # fields = ["user_name", "user_email", "comment_text"]
        
        # we can also use exclude to exclude certain fields from the form. for example if we want to exclude the post field from the form, we can use the below line instead of the above line. 
        exclude = ["post"]
        