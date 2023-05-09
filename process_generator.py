import simulus
import objgraph



def process_fun(i):
   x = i
 
    
def generate_processes(sim):
    for i in range(100000000):
        sim.sleep(1)
        for j in range (10):
          sim.process(process_fun,i)
        """
        if x == 10000:
            objgraph.show_chain(
                objgraph.find_backref_chain(
                    random.choice(objgraph.by_type('greenlet')),
                    objgraph.is_proper_module),
                filename='greenlet.png')
            input("image made ")
        """
            




sim1 = simulus.simulator("sim1")


sim1.process(generate_processes,sim1)



sim1.run()
