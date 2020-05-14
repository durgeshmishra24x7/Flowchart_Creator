from graphviz import Digraph

g= Digraph("flowtest1",node_attr={'color':'lightblue2','style':'filled'})
g.attr(size='7,7')
global step1,step2,step3,step5,action,step6

class step:
    def __init__(self):
        self.step1 = input("Enter the initials :- ")
        self.step2 = input("Enter next statement :- ")
        self.step3 = input("Input/Output :- ")

class oper(step):

    def proc1(self):
        self.step6=['Addition','Subtraction','Multiplication','Divison']

    def begin(self):

        #step.__init__(self)    
        g.attr('node', shape='box')
        g.node(self.step2)  #DTN

        g.attr('node', shape='ellipse')
        g.node(self.step1) #START

        g.attr('node',shape='parallelogram')
        g.node(self.step3) #RTN

        g.edge(self.step1, self.step2)
        g.edge(self.step2,self.step3)

    def proc(self):
        g.attr('node', shape='box')
        for i in range(len(self.step6)):
            #g.node(self.step2,self.step6[i])
            g.edge(self.step3,self.step6[i])


        action=input("Are you Sure (Y/N):- ")
        
        act=['Y','y','YES','Yes','yes']
        neg=['N','n','No','NO','no']
        #g.view()    

        i=0
        while i <=0:
            if action in act:
                #OPER.begin()
                #OPER.proc()
                g.view()
                i+=1
            elif action in neg:
                print("Restart the program")
                i+=1
            else:
                print("Wrong input!, Restart the program")
                break

if __name__=="__main__":
    #STEP=step()
    #STEP.full()
    OPER = oper()
    OPER.proc1()
    OPER.begin()
    OPER.proc()




