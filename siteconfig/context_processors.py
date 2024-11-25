from .models import ContactInfo

def contact_info(request):
    contact = ContactInfo.objects.first()
    return {'whatsapp_number': contact.whatsapp_number if contact else ''}
