# coding: utf-8

import json
import logging
import shlex
import utils.exec_handler_exception as exception
from subprocess import Popen, PIPE, TimeoutExpired


class ExecutionHandler():
    """
    Class that execute users' commands.

    It has users' working directory and permissions
    and open subprocesses that run users' commands.
    """

    def __init__(self):
        """
        Initializer of this class.
        """

        try:

            with open('users.json', mode='rt') as fin:
                self.users = json.loads(fin.read())

            self.cwd = dict()

            for user in self.users.keys:
                self.cwd[user] = '/'
                print(user)

        except FileNotFoundError:

            logging.warning('no user registered, '
                            'you need to "init" command')

            self.users = None

        except Exception:

            logging.error('unable to open users.json, authorization is unable')

    def __del__(self):
        """
        Destructor of this class.
        """

        try:

            with open('users.json', 'wt') as fout:
                fout.write(json.dumps(self.users))

        except Exception:

            logging.error('unable to save users\' permissions, '
                          '"init" will be need once more')

    def init_users(self, user_id):
        """
        Initializer of users and users.json.
        Register an admin user, and it is allowed only once.
        """

        if self.users is None:

            self.users = {user_id: 'admin'}
            self.cwd = {user_id: '/'}

            try:

                with open('users.json', 'wt') as fout:
                    fout.write(json.dumps(self.users))

            except Exception:

                logging.error('unable to open users.json and initialize it')

                self.users = None

                raise exception.InitializationUnable()

        else:
            raise exception.InitializationNotAllowed()

    def grant(self, user_id, target_user_id, level):
        """
        Grant a user the permission to execute command.
        A user who do this need to be "admin".
        """

        if self.users[user_id] != 'admin':
            raise

        if level != 'admin' and level != 'trust':
            raise exception.GrantNoSuchLevel()

        self.users[target_user_id] = level

    def revoke(self, user_id, target_userd_id):
        """
        Revoke users' permissions to execute commands.
        A user who do this need to be "admin".
        """
        raise NotImplementedError()

    def exec_command(self, command, user_id):
        """
        Execute commands which are given by users.
        Users need to be registered as "admin".
        """

        if user_id not in self.users or\
                (self.users[user_id] != 'admin' and
                 self.users[user_id] != 'trust'):
            raise exception.ExecutionPermissionDenied()

        with Popen(
                shlex.split(command),
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE,
                cwd=self.cwd[user_id],
                shell=True
                ) as proc:

            try:

                proc.wait(timeout=15)  # Wait for 15 seconds

                result = proc.stdout.read().decode()

            except TimeoutExpired:
                raise exception.ExecutionTimeout()

            except Exception:
                raise exception.ExecutionFailure()

        return result
