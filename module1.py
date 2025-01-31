
import mph	
import numpy as np
mph.option('classkit', True)
client=mph.start()
client = mph.start(cores=1) #start the client with 1 core COMMENT
model=client.load('capacitor.mph') #Now that we have the client up and running, we can tell it to load a model file.
client.names() 
client.models()


#Inspecting models
for (name, value) in model.parameters().items():

    description = model.description(name)

    print(f'{description:20} {name} = {value}')
    
    
# model.materials()

# model.physics()
