from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(u), 'Test User')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=team)
        a = Activity.objects.create(user=u, type='Run', duration=10, points=5, date='2024-01-01')
        self.assertEqual(a.type, 'Run')
    def test_workout_create(self):
        w = Workout.objects.create(name='Test Workout', description='desc', suggested_for='all')
        self.assertEqual(str(w.name), 'Test Workout')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        l = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(l.points, 100)
