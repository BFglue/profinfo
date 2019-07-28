# -*- coding: utf-8 -*-

from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from decimal import Decimal

from num2t4ru import num2text


def group_required(group, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)

        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)


def create_pdf_response(result, file_name=None):
    response = HttpResponse(content_type='application/pdf')
    if file_name:
        response['Content-Disposition'] = 'inline; filename="%s.pdf"' % file_name
    else:
        response['Content-Disposition'] = 'inline; filename="11.pdf"'
    response.write(result)
    return response


def text_price(decimal_price):
    decimal_price = Decimal(round(decimal_price * 100)/100)
    male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
    female_units = ((u'копейка', u'копейки', u'копеек'), 'f')
    if len(str(decimal_price).split('.')) > 1:
        total_cost_rubles, total_cost_copecks = str(decimal_price).split('.')
        total_cost_copecks = total_cost_copecks[:2]
    else:
        total_cost_rubles = str(decimal_price)
        total_cost_copecks = str(00)
    text_result = num2text(int(total_cost_rubles), male_units)
    text_result += ' ' + num2text(int(total_cost_copecks), female_units)
    return text_result


