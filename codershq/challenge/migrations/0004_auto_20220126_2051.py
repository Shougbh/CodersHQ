# Generated by Django 3.2.11 on 2022-01-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_remove_sponsorships_sprint'),
        ('challenge', '0003_auto_20220123_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='sprintenrollment',
            name='sprint',
        ),
        migrations.RemoveField(
            model_name='sprintenrollment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='slack_group',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website link'),
        ),
        migrations.DeleteModel(
            name='ChallengeScore',
        ),
        migrations.DeleteModel(
            name='ScoreCategory',
        ),
        migrations.DeleteModel(
            name='Sprint',
        ),
        migrations.DeleteModel(
            name='SprintEnrollment',
        ),
    ]