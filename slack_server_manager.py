# coding: utf-8

import logging
import signal
import requests
from slackbot.bot import Bot


logging.basicConfig(
        format='[%(levelname)s] %(asctime)s %(name)s : %(message)s',
        level=logging.INFO
        )


def main():
    """
    Main function which start bot
    """

    try:

        bot = Bot()
        bot.run()

    except requests.exceptions.ConnectionError as err:

        logging.critical('unable to connect Slack API')
        print(err)

    except Exception as err:

        logging.critical('unknown error has occured\n')
        print(err)


if __name__ == "__main__":

    def stop_application(*args, **kwargs):
        """
        Function which is called when the application is killed or terminated
        """

        logging.info('stop the application\nBye')
        exit()

    signal.signal(signal.SIGINT, stop_application)
    signal.signal(signal.SIGTERM, stop_application)

    print('Ctrl-C to stop the application')
    logging.info('start the application')

    main()
