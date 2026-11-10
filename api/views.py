from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import ImageMetadata



@csrf_exempt
@require_POST
def add_image_meta(requests):
    try:
        data = json.loads(requests.body)
    except ValueError:
        return HttpResponse("invalid image url", status=400)
    image_url = data.get("url")
    image_tags = data.get("tags", "")
    print(image_url,image_tags)
    if len(image_tags) > 10:
        return HttpResponse("Each image can only store 10 tags", status=400)
    image, created = ImageMetadata.objects.get_or_create(image_url= image_url, image_tags = ",".join(image_tags))
    print(image)
    if created:
        return HttpResponse("Image add succussfully", status=201)
    else:
        return HttpResponse("This image already exist", status=400)


@require_GET
def get_image_meta(request):
    tag = request.GET.get('tag', '')
    iamges = ImageMetadata.objects.filter(tag__iscontain=tag).order_by("tag").values_list("tag",flat=True)[:10]
    urls = [img.url for img in iamges]
    return JsonResponse({"images_urls": {[img.url for img in iamges]}}, status=201)