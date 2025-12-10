"""
Management command to add email addresses to existing users
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Update email addresses for existing users'

    def handle(self, *args, **kwargs):
        users_without_email = User.objects.filter(email='') | User.objects.filter(email__isnull=True)
        
        if not users_without_email.exists():
            self.stdout.write(self.style.SUCCESS('✅ All users already have email addresses!'))
            return
        
        self.stdout.write(f'\nFound {users_without_email.count()} users without email addresses:\n')
        
        for user in users_without_email:
            self.stdout.write(f'Username: {user.username}')
            email = input(f'  Enter email for {user.username}: ').strip()
            
            if email:
                user.email = email
                user.save()
                self.stdout.write(self.style.SUCCESS(f'  ✅ Updated {user.username} with email: {email}\n'))
            else:
                self.stdout.write(self.style.WARNING(f'  ⚠️  Skipped {user.username}\n'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ Email update complete!'))
