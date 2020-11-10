import datetime

from django.db import models

from timedelta import TimedeltaField


class MinMaxTestModel(models.Model):
    min = TimedeltaField(min_value=datetime.timedelta(1))
    max = TimedeltaField(max_value=datetime.timedelta(1))
    minmax = TimedeltaField(min_value=datetime.timedelta(1), max_value=datetime.timedelta(7))


class IntTestModel(models.Model):
    field = TimedeltaField(min_value=1, max_value=86400)


class FloatTestModel(models.Model):
    field = TimedeltaField(min_value=1.0, max_value=86400.0)