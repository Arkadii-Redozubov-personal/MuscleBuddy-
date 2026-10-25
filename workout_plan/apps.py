from django.apps import AppConfig
from django.db.models.signals import post_migrate

def auto_load_fixtures(sender, **kwargs):
    if sender.name == 'workout_plan':
        from workout_plan.models import TrainingPlan
        try:
            if TrainingPlan.objects.count() == 0:
                from django.core.management import call_command
                call_command('loaddata', 'fixtures/initial_data.json')
                print("[Auto-Seed] Successfully loaded initial_data.json on migrate.")
        except Exception as e:
            print(f"[Auto-Seed] Fixture load skipped: {e}")

class WorkoutPlanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout_plan'

    def ready(self):
        post_migrate.connect(auto_load_fixtures, sender=self)
