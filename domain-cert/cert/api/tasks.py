from logging import exception
from ..models import Certs
from .utils import load_certificate

def refresh_certs_messages_to_db(cert_obj_id=None):
    certs = Certs.objects.filter(id=cert_obj_id) if cert_obj_id else Certs.objects.all()
    for cert in certs:
        Certs._meta.auto_created = True
        try:
            if not cert.method: cert.method = 0
            if cert.method == 0:
                cert_info = load_certificate(cert.method, cert.domain_url)
            else:
                cert_info = load_certificate(cert.method, cert.crt_file)
            for k, v in cert_info.items():
                setattr(cert, k, v)
            cert.save()
        except exception as e:
            print(e)
        finally:
            Certs._meta.auto_created = False
    return 0
