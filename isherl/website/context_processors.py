from .models import Footer

def footer_context(request):
    return {
        'footers': Footer.objects.all()
    }



