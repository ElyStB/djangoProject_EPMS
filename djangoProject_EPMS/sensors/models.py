from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

UserModel = get_user_model()


class SensorModel(models.Model):

    MIN_VALUE_VALIDATOR_LATITUDE = -90.0
    MAX_VALUE_VALIDATOR_LATITUDE = 90.0
    MIN_VALUE_VALIDATOR_LONGITUDE = -180.0
    MAX_VALUE_VALIDATOR_LONGITUDE = 180.0
    MAX_TYPE_LENGTH = 25
    MAX_DESCRIPTION_LENGTH = 300

    location_latitude = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_VALUE_VALIDATOR_LATITUDE),
            MaxValueValidator(MAX_VALUE_VALIDATOR_LATITUDE),
        )
    )

    Location_longitude = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_VALUE_VALIDATOR_LONGITUDE),
            MaxValueValidator(MAX_VALUE_VALIDATOR_LONGITUDE),
        )
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
    )

    serial_number = models.IntegerField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=False,
        blank=False,
    )

    created_at = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    is_rented = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )


class UsedSensorsModel(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='used_sensors',
    )

    sensor = models.ManyToManyField(
        SensorModel,
        related_name='used_sensors',
    )

    # the value must be in this format: "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"
    time_stamp = models.DateTimeField(
        auto_now_add=True,

    )




