# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Required, 255 characters or fewer. Only letters, numbers, and @, ., +, -, or _ characters.', unique=True, max_length=255, verbose_name='email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Required, 255 characters or fewer. Only letters, numbers, and @, ., +, -, or _ characters.', unique=True, max_length=255, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')]),
            preserve_default=True,
        ),
    ]

    def mutate_state(self, project_state, preserve=True):
        """
        This is a workaround that allows to store ``auth``
        migration outside the directory it should be stored.
        """
        app_label = self.app_label
        self.app_label = 'auth'
        state = super(Migration, self).mutate_state(project_state)
        self.app_label = app_label
        return state

    def apply(self, project_state, schema_editor, collect_sql=False):
        """
        Same workaround as described in ``mutate_state`` method.
        """
        app_label = self.app_label
        self.app_label = 'auth'
        state = super(Migration, self).apply(project_state, schema_editor, collect_sql)
        self.app_label = app_label
        return state
