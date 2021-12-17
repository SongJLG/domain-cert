from datetime import datetime
from urllib3.contrib import pyopenssl as reqs

def load_certificate(method, obj):
    if method == 0:
        cert = reqs.ssl.get_server_certificate((obj, 443))
    elif method == 1:
        cert = obj
    else:
        return {}
    try:
        x509 = reqs.OpenSSL.crypto.load_certificate(reqs.OpenSSL.crypto.FILETYPE_PEM, cert)
        notbefore = datetime.strptime(x509.get_notBefore().decode()[0:-1], '%Y%m%d%H%M%S')
        notafter = datetime.strptime(x509.get_notAfter().decode()[0:-1], '%Y%m%d%H%M%S')
        remain_days = notafter - datetime.now()
        organization_name = x509.get_subject().organizationName
        serial_number = x509.get_subject().serialNumber

        if serial_number:
            cert_type = "EV"
        elif not organization_name:
            cert_type = "DV"
        else:
            cert_type = "OV"

        ret = {
            'domain': x509.get_subject().CN,
            'orther_domain': reqs.get_subj_alt_name(x509),
            'organization_name': organization_name,
            'serial_number': serial_number,
            'issued_by': x509.get_issuer().CN,
            'cert_type': cert_type,
            'notbefore': notbefore.strftime('%Y-%m-%d %H:%M:%S'),
            'notafter': notafter.strftime('%Y-%m-%d %H:%M:%S'),
            'remain_days': remain_days.days,
        }
    except Exception as e:
        raise Exception(e)
    return ret