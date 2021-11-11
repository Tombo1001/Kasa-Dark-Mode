from pyHS100 import Discover
import sys
import argparse

def main(argv):
    # set up arg parser and arguments
    parser = argparse.ArgumentParser(prog='python3 kasa-dark-mode.py', description='A Python tool to turn off kasa plug LEDs')
    parser.add_argument('--debug', default=False, action='store_true', help='Enable debug mode')
    parser.add_argument('-d', '--dark', default=False, action='store_true', help='Turn off smartplug LEDs')
    parser.add_argument('-l', '--light', default=False, action='store_true', help='Turn on smartplug LEDs')
    parser.add_argument('-i', '--interactive', default=False, action='store_true', help='Control smartplug LEDs interactively')
    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled")
        answer = query_yes_no("Is this working?", "yes")
        print(answer)

    if not args.interactive:
        options_mode(args)
    else:
        interactive_mode(args)


def interactive_mode(args):
    print("You have selected interactive mode\nSearching for smartplugs...")
    for plug in Discover.discover().values():
        print("--plug found--")
        if "SmartPlug" in str(plug):
            LEDstate = plug.led
            plugAlias = plug.alias
            print("Plug Alias: %s" % plugAlias)
            print("Current LED state: %s" % LEDstate)
            if LEDstate == True: #LED is on
                question = ("Do you wish to turn OFF '%s' LED" % plugAlias)
                answer = query_yes_no(question, "yes")
                if answer:
                    plug.led = False # turn off LED
                    print("New LED state: %s" % plug.led)
            elif LEDstate == False: #LED is off
                question = ("Do you wish to turn ON '%s' LED" % plugAlias)
                answer = query_yes_no(question, "yes")
                if answer:
                    plug.led = True # turn on LED
                    print("New LED state: %s" % plug.led)
            print("---")


def options_mode(args):
    for plug in Discover.discover().values():
        if "SmartPlug" in str(plug):
            print("Plug Alias: %s" % plug.alias)
            LEDstate = plug.led
            print("Current LED state: %s" % LEDstate)
            if args.dark:
                if not args.light: #check for conflicting otptions
                    if LEDstate == True: #check for current LED state
                        plug.led = False # turn off LED
                        print("New LED state: %s" % plug.led)
                    else:
                        print("Lights are already off, skipping dark mode action")
                else:
                    print("light and dark mode options selected - you can only choose 1")
                    print("---")
                    continue
            if args.light:
                if not args.dark: #check for conflicting otptions
                    if LEDstate == False:
                        plug.led = True # turn on LED
                        print("New LED state: %s" % plug.led)
                    else:
                        print("Lights are already on, skipping light mode action")
                else:
                    print("light and dark mode options selected - you can only choose 1")
                    print("---")
                    continue
        print("---")


def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n]: "
    elif default == "yes":
        prompt = " [Y/n]: "
    elif default == "no":
        prompt = " [y/N]: "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


if __name__ == '__main__':
    main(sys.argv)
