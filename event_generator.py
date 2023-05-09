import simulus
import objgraph



def process_fun(i):
   x = i
 
    
def generate_processes(sim):
    for i in range(100000000):
        sim.sleep(1)
        for j in range (10):
            sim.sched(process_fun,i,offset=1)
      
            




sim1 = simulus.simulator("sim1")


sim1.process(generate_processes,sim1)



sim1.run()
