#!/usr/bin/python3
"""
This Module receives inputs and keeps statistics

Lines of text are fed into the stdin continuously
while the module keeps the statistics of part of
the text (File sizes and status codes). After every
10 lines, the cumulative statistics is printed to
the stdout
"""


def print_stats(totalSize, statusCodes, statusChoice):
    """Prints to the stdout"""
    print("File size: {}".format(totalSize))
    for code in statusChoice:
        frequency = statusCodes.count(code)
        if frequency > 0:
            print("{}: {}".format(code, frequency))
    return 1


if __name__ == "__main__":
    import sys

    totalSize = 0
    statusChoice = ['200', '301', '400', '401', '403', '404', '405', '500']
    statusCodes = []

    try:
        i = 0
        for prompt in sys.stdin:
            if i == 10:
                print_stats(totalSize, statusCodes, statusChoice)
                i = 1
            else:
                i += 1
            try:
                promptWords = prompt.split()
                try:
                    totalSize += int(promptWords[-1])
                except ValueError:
                    pass
                try:
                    statusCodes.append(promptWords[-2])
                except IndexError:
                    pass
            except Exception:
                p = print_stats(totalSize, statusCodes, statusChoice)
                if p == 1:
                    raise

        print_stats(totalSize, statusCodes, statusChoice)
    except KeyboardInterrupt:
        p = print_stats(totalSize, statusCodes, statusChoice)
        if p == 1:
            raise
    except ValueError:
        pass
