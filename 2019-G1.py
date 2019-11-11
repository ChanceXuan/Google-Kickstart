case_num = int(input('Please input case number:'))

class Case:
    def __init__(self, name):
        self.name = name
        print('...Initializing Case: {}...'.format(self.name))

        inputNMQ = input('Please input N, M, Q:').split()
        self.n = int(inputNMQ[0])
        self.m = int(inputNMQ[1])
        self.q = int(inputNMQ[2])
        print('N=%d, M=%d, Q=%d'%(self.n,self.m,self.q))

        self.pageTorn = input('Please input Pm(M={}):'.format(self.m)).split()
        self.pageTorn = list(map(int,self.pageTorn))
        print('The torn pagelist is:{}'.format(self.pageTorn))
    
        self.pageCheck = input('Please input Rq(Q={}):'.format(self.q)).split()
        self.pageCheck = list(map(int,self.pageCheck))
        print('The multipled numbers are:{}'.format(self.pageCheck))

        print('!--Initialized Case: {}--!'.format(self.name))

    def result(self):
        # pass
        self.pageRead = set()
        for page in range(1,(self.n)+1):
            for s in self.pageCheck:
                if page % s == 0:
                    self.pageRead.add(page)
            for t in self.pageTorn:
                if t in self.pageRead:
                    self.pageRead.remove(t)
        print('The read pages are:{}'.format(self.pageRead))
        return len(self.pageRead)

for i in range(1,case_num+1):
    caseName = 'Case #'+str(i)
    ans = Case(caseName).result()
    print('%s:%d'% (caseName, ans))