from typing import List
from ninja import Router,Form,File
from ninja.files import UploadedFile
from django.shortcuts import get_object_or_404
from . import models,schemas

router = Router()

@router.get("/search",response=List[schemas.PostSchema])
def search_posts(request, q: str):
    return models.Post.objects.filter(title__icontains=q, moderated=False).select_related('author')

#@router.post("/newPost", response=schemas.PostSchema)
