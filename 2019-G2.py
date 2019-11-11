case_num = int(input('Please input case number:'))

class Case:
    def __init__(self, name):
        self.name = name
        print('...Initializing Case: {}...'.format(self.name))

        inputNMQ = input('Please input N, M:').split()
        self.n = int(inputNMQ[0])
        self.m = int(inputNMQ[1])
        print('N=%d, M=%d'%(self.n,self.m))

        self.numbers = input('Please input An(N={}):'.format(self.n)).split()
        self.numbers = list(map(int,self.numbers))
        print('The N numbers are:{}'.format(self.numbers))

        print('!--Initialized Case: {}--!'.format(self.name))

    def result(self):
        for k in range(max(max(self.numbers),self.m),-1,-1):
            sum = 0
            for i in range(0,self.n):
                sum = sum + (self.numbers[i]^k)
            if sum <= self.m:
                return k
        return -1

for i in range(1,case_num+1):
    caseName = 'Case #'+str(i)
    ans = Case(caseName).result()
    print('%s:%d'% (caseName, ans))