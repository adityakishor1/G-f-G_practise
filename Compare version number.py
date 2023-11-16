class Solution(object):
    def compareVersion(self, version1, version2):
        def getVersion(version, start):
            if start==-1: return 0, -1
            for i in xrange(start, len(version)):
                if version[i]=='.':
                    return int(version[start:i]), i+1
            return int(version[start:]), -1 #[0]
            
        i1 = i2 = 0
        
        while True:
            sub_version1, i1 = getVersion(version1, i1)
            sub_version2, i2 = getVersion(version2, i2)
            
            if sub_version1>sub_version2:
                return 1
            elif sub_version1<sub_version2:
                return -1
            elif i1==-1 and i2==-1: #[1]
                return 0
