from __future__ import absolute_import

from django.db import models
from django.utils import timezone

from sentry.db.models import BoundedPositiveIntegerField, FlexibleForeignKey, Model


class Feature(object):
    API = 0
    ISSUE_LINK = 1
    STACKTRACE_LINK = 2
    EVENT_HOOKS = 3

    @classmethod
    def as_choices(cls):
        return (
            (cls.API, 'integrations-api'),
            (cls.ISSUE_LINK, 'integrations-issue-link'),
            (cls.STACKTRACE_LINK, 'integrations-stacktrace-link'),
            (cls.EVENT_HOOKS, 'integrations-event-hooks'),
        )

    @classmethod
    def as_str(cls, feature):
        if feature == cls.API:
            return 'integrations-api'
        elif feature == cls.ISSUE_LINK:
            return 'integrations-issue-link'
        elif feature == cls.STACKTRACE_LINK:
            return 'integrations-stacktrace-link'
        elif feature == cls.EVENT_HOOKS:
            return 'integrations-event-hooks'

    @classmethod
    def description(cls, feature):
        if feature == cls.API:
            return "This integration can utilize the Sentry API (with the permissions granted) to pull data or update resources in Sentry!"
        elif feature == cls.ISSUE_LINK:
            return "This integration can allow your organization to create or link Sentry issues to another service!"
        elif feature == cls.STACKTRACE_LINK:
            return "This integration allows your organization to open a line in Sentry's stack trace in another service!"
        elif feature == cls.EVENT_HOOKS:
            return "This integration allows your organization to forward events to another service!"


class IntegrationFeature(Model):
    __core__ = False

    sentry_app = FlexibleForeignKey('sentry.SentryApp')
    user_description = models.TextField(null=True)
    feature = BoundedPositiveIntegerField(
        default=0,
        choices=Feature.as_choices(),
    )
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_integrationfeature'
        unique_together = (('sentry_app', 'feature'),)

    def feature_str(self):
        return Feature.as_str(self.feature)

    @property
    def description(self):
        if self.user_description:
            return self.user_description
        else:
            return Feature.description(self.feature)
