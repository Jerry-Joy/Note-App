"""
Data migration script from SQLite to PostgreSQL
Run this script to transfer users and notes from db.sqlite3 to PostgreSQL
"""

import os
import django
import sqlite3
from datetime import datetime

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth.models import User
from api.models import Note


def migrate_data():
    print("=" * 60)
    print("Starting data migration from SQLite to PostgreSQL")
    print("=" * 60)

    # Check if SQLite database exists
    sqlite_db = "db.sqlite3"
    if not os.path.exists(sqlite_db):
        print(f"\n❌ Error: {sqlite_db} not found!")
        print("Make sure db.sqlite3 is in the backend directory.")
        return

    # Connect to SQLite
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    try:
        # Migrate Users
        print("\n📦 Migrating users...")
        cursor.execute(
            "SELECT id, username, email, password, is_staff, is_active, is_superuser, date_joined FROM auth_user"
        )
        users = cursor.fetchall()

        user_count = 0
        user_mapping = {}  # Map old user IDs to new user objects

        for user_data in users:
            (
                old_id,
                username,
                email,
                password,
                is_staff,
                is_active,
                is_superuser,
                date_joined,
            ) = user_data

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                print(f"   ⚠️  User '{username}' already exists, skipping...")
                existing_user = User.objects.get(username=username)
                user_mapping[old_id] = existing_user
                continue

            # Create user in PostgreSQL
            user = User.objects.create(
                username=username,
                email=email,
                password=password,  # Already hashed
                is_staff=is_staff,
                is_active=is_active,
                is_superuser=is_superuser,
                date_joined=date_joined,
            )
            user_mapping[old_id] = user
            user_count += 1
            print(f"   ✅ Migrated user: {username}")

        print(f"\n✅ Successfully migrated {user_count} users")

        # Migrate Notes
        print("\n📝 Migrating notes...")
        cursor.execute("SELECT id, title, content, created_at, author_id FROM api_note")
        notes = cursor.fetchall()

        note_count = 0
        for note_data in notes:
            note_id, title, content, created_at, author_id = note_data

            # Get the corresponding user from mapping
            if author_id not in user_mapping:
                print(f"   ⚠️  Skipping note '{title}' - author not found")
                continue

            author = user_mapping[author_id]

            # Create note in PostgreSQL
            Note.objects.create(
                title=title, content=content, created_at=created_at, author=author
            )
            note_count += 1
            print(f"   ✅ Migrated note: {title[:50]}...")

        print(f"\n✅ Successfully migrated {note_count} notes")

        # Summary
        print("\n" + "=" * 60)
        print("MIGRATION SUMMARY")
        print("=" * 60)
        print(f"✅ Users migrated: {user_count}")
        print(f"✅ Notes migrated: {note_count}")
        print("\n🎉 Migration completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        import traceback

        traceback.print_exc()

    finally:
        conn.close()


if __name__ == "__main__":
    # Confirm before proceeding
    print("\n⚠️  WARNING: This will migrate data from SQLite to PostgreSQL")
    print("Make sure:")
    print("  1. Your PostgreSQL database is running")
    print("  2. You've run 'python manage.py migrate'")
    print("  3. The db.sqlite3 file is in the backend directory")

    response = input("\nDo you want to continue? (yes/no): ").strip().lower()

    if response in ["yes", "y"]:
        migrate_data()
    else:
        print("\n❌ Migration cancelled.")
