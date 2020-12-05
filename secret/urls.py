from django.urls import path
from .views import (
    get_secret,
    all_secrets,
    create_secret,
    hug,
    comment_secret
    )

app_name = 'secret'

urlpatterns = [
    path('', all_secrets, name='all_secret'),
    path('create_secret/', create_secret, name='create_secret'),
    path('<secret_id>', get_secret, name='secret'),
    path('<secret_id>/hug/', hug, name='hug'),
    path('<secret_id>/new_comment/', comment_secret, name='comment_secret'),
    path('<secret_id>/comment/<coment_id>/like', like_comment, name='like_comment'),
]
