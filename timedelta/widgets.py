import datetime

from django import forms
from django.utils import six
from django.conf import settings

from timedelta.helpers import nice_repr, parse


class TimedeltaWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super(TimedeltaWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, **kwargs):
        if value is None:
            value = ""
        elif isinstance(value, six.string_types):
            pass
        else:
            if isinstance(value, int):
                value = datetime.timedelta(seconds=value)
            value = nice_repr(value)
        return super(TimedeltaWidget, self).render(name, value, **kwargs)

    def _has_changed(self, initial, data):
        """
        We need to make sure the objects are of the canonical form, as a
        string comparison may needlessly fail.
        """
        if initial in ["", None] and data in ["", None]:
            return False

        if initial in ["", None] or data in ["", None]:
            return True

        if initial:
            if not isinstance(initial, datetime.timedelta):
                initial = parse(initial, language=settings.LANGUAGE_CODE)

        if not isinstance(data, datetime.timedelta):
            try:
                data = parse(data, language=settings.LANGUAGE_CODE)
            except TypeError:
                # initial didn't throw a TypeError, so this must be different
                # from initial
                return True

        return initial != data
