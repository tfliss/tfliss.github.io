class App: 
    def __init__(self):
        pass

    def go(self, message):
        '''Main loop for the application.

        Parameters
        ----------

        '''
        print(message)


if __name__ == '__main__':
    import sys

    a = App()
    a.go(sys.argv[-1])
