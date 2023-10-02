from linkedlist import LinkedList

class WebBrowser():

    def __init__(self):
        self._browser = LinkedList()
        self._back = 0
        self._forward = 0 
        
    def navigate_to(self, url):
        if self._back == 0:
            self._browser.insert(self._browser.length(), url)
        else:
            self._browser.set_entry(self._browser.length() - (self._back), url)
            index = 0
            for i in range(self._browser.length()):
                if self._browser.get_entry(i) == url:
                    index = i
            for i in range(self._browser.length() - self._back + 1, self._browser.length()):
                self._browser.remove(index+1)
            self._back = 0

    def forward(self):
        if self._browser.length() > 0 and self._forward <= self._browser.length():
            self._forward += 1
            if self._back != 0:
                self._back -= 1
        
    def back(self):
        if (self._browser.length() > 0) and self._back >= 0:
            self._back += 1
            if self._forward != 0:
                self._forward -= 1
    
    def history(self):
        print('Oldest')
        print('===========')
        if self._back == 0:
            for i in range(self._browser.length()):
                if i == self._browser.length() - 1:
                    print(f'{self._browser.get_entry(i)} <== current')
                else:
                    print(f'{self._browser.get_entry(i)}')
        elif self._back != 0:
            for i in range(self._browser.length()):
                if i == self._browser.length() - (1 + self._back):
                    print(f'{self._browser.get_entry(i)} <== current')
                else:
                    print(f'{self._browser.get_entry(i)}')
        print('===========')
        print('Newest')
        print('\n')
            

            
        
    







    
