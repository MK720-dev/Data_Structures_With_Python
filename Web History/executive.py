from webBrowser import WebBrowser

class Executive():
    def __init__(self):
        Browser = WebBrowser()
        input_file = input('enter a sample test file name: ')
        f = open(input_file, 'r')
        for line in f:
            if line.split()[0] == 'NAVIGATE':
                Browser.navigate_to(line.split()[1])
            elif line.split()[0] == 'BACK':
                Browser.back()
            elif line.split()[0] == 'FORWARD':
                Browser.forward()
            else:
                Browser.history()

excex = Executive()