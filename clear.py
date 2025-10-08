import os
import sys

print("📦  Collecting static files...")
exit_code = os.system('python manage.py collectstatic --noinput --ignore "*.map" --ignore "*.scss"')
if exit_code == 0:
    print("✅ Static files collected successfully.")
else:
    print("❌ An error occurred.")
    sys.exit(exit_code)
