#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # set your django setting module here
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmstest.settings")

    from django.core.management import execute_from_command_line

    # hack to prevent admin prompt
    if len(sys.argv) >= 2 and sys.argv[1] == 'syncdb':
        sys.argv.append('--noinput')

    execute_from_command_line(sys.argv)

    # additional process for creation additional user, misc data, and anything
    for arg in sys.argv:
        # if syncdb occurs and users don't exist, create them
        if arg.lower() == 'syncdb':
            print 'syncdb post process...'
            from django.contrib.auth.models import User

            admin_id = 'admin'
            admin_email = 'junk@mail.com'
            admin_password = 'adminpw'
            additional_users = [
                                ['tempuser', 'user_email@mail.com', 'tempuser_password']
                                ]

            # admin exists?
            user_list = User.objects.filter(username=admin_id)
            if len(user_list) == 0:
                print 'create superuser: ' + admin_id
                new_admin = User.objects.create_superuser(admin_id, admin_email, admin_password)

            # additional user exists?
            for additional_user in additional_users:
                user_list = User.objects.filter(username=additional_user[0])
                if len(user_list) == 0:
                    print 'create additional user: ' + additional_user[0]
                    new_admin = User.objects.create_user(additional_user[0], additional_user[1], additional_user[2])
