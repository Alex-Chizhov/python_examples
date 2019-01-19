import sys
import getopt


def get_start_and_end_dates():
    stert_date = None
    end_date = None

    # return a list [path to current working dir, options that we passed in command line(one ore more)]
    argv = sys.argv[1:]
    #print(argv)

    try:
        options, arguments = getopt.getopt(argv, "s:e:", ["start_date=", "end_date="])
    except getopt.GetoptError as err:
        print(err)


    for option, argument in options:
        if option in ['-s', '--start_date']:
            start_date = argument
            print("start_date = {}".format(start_date))
        elif option in ['-e', '--end_date']:
            end_date = argument
            print("end_date = {}".format(end_date))

get_start_and_end_dates()