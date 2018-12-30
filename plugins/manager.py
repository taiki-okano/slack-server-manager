# coding: utf-8

import re
from utils import exec_handler, exec_handler_exception
from slackbot.bot import respond_to


execution_handler = exec_handler.ExecutionHandler()


@respond_to('^run(.*)', re.IGNORECASE)
def command_run(message, *commands):

    try:
        result = execution_handler.exec_command(
                ' '.join(commands),
                message.user['id']
                )

    except exec_handler_exception.ExecutionPermissionDenied:
        message.reply('Error: Permisssion denied')

    except exec_handler_exception.ExecutionTimeout:
        message.reply('Error: Exection timed out')

    except exec_handler_exception.ExecutionFailure:
        message.reply('Error: Execution failed')

    else:
        message.reply('Execution completed\n```' + result + '```')


@respond_to('^init$', re.IGNORECASE)
def command_init(message, *commands):

    try:
        execution_handler.init_users(message.user['id'])

    except exec_handler_exception.InitializationUnable:
        message.reply('Error: Initialization failed')

    except exec_handler_exception.InitializationNotAllowed:
        message.reply('Error: Initialization is not allowed')

    else:
        message.reply('Initialization completed')
