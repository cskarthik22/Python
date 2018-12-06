import pdb
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return '%s by %s' %(self.title, self.author)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('Book object is deleted...')

b = Book('Python Basics', 'Alex', 200)
print b
print len(b)


class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2 )**0.5

    def distance2(self):
        zipval = zip(list(self.coor1),list(self.coor2))
        res = 0
        for x,y in zipval:
            res = (x-y)**2 + res
        return res**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)*1.0 / (x2-x1)

a = Line((3,2),(8,10))
pdb.set_trace()
print(a.distance())
print(a.distance2())
print(a.slope())




