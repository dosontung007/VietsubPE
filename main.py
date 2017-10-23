import webbrowser
import sys
import logging


def open_problem(input_data):
    webbrowser.open('Problem {} - Project Euler.html'.format(input_data))
    logging.info('Open Problem {}'.format(input_data))


def main():
    num_problem = input('Type the problem which you want open')
    open_problem(num_problem)


if __name__ == '__main__':
    main()
