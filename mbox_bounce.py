import simulus
import objgraph
import random

def recv_fun(mbx):
    while True:
        x = mbx.recv(isall=False)
        print(x)

        #Creates a back refrence chart for traps generated using the mailbox.
        #Example run in folder under mailbox_backref.png
        """
        if x == 10000:
            objgraph.show_chain(
                objgraph.find_backref_chain(
                    random.choice(objgraph.by_type('Trap')),
                    objgraph.is_proper_module),
                filename='mailbox_backref.png')
            input("image made ")
        """
def process_fun(sim,target,i):
    sim.sync().send(sim,target+"_mbx",i)
 
    
def generate_processes(sim,mbx,sim_target):
    p = sim.process(recv_fun,mbx)
    print(p)
    for i in range(100000000):
        sim.sleep(1)
        for j in range (10):
            sim.sched(process_fun,sim,sim_target,i,offset=1)
      
            




sim1 = simulus.simulator("sim1")
sim2 = simulus.simulator("sim2")
mbx1 = sim1.mailbox('sim1_mbx',1)
mbx2 = sim2.mailbox('sim2_mbx',1)
sim1.process(generate_processes,sim1,mbx1,"sim2")
sim2.process(generate_processes,sim2,mbx2,"sim1")

sy = simulus.sync([sim1,sim2])



sy.run()
