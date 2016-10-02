import logging

def main():
    logger = logging.getLogger()
    logger.debug('Entering Main')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
