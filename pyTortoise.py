
been_init = False

def init():
    global been_init
    been_init = True
    print("Using pyTortoise")
    print("pyTortoise is made by: Darion Knighton-Fitt")
    print("version: 1.1")
    print(" \n \n")

def genorate_neural_tree(inputs, outputs):
    global been_init
    if been_init == True:
        import random
        weights = []
        gradients = []
        post_sterio = []
        final_weights = []
        final_gradients = []
        final_post_sterio = []
        for a in range(inputs):
            for i in range(inputs-a):
                weights = []
                weights = weights + [random.randint(10000, 99999) // 1000]
                gradients = gradients + [random.randint(1, 2)]
                post_sterio = post_sterio + [random.randint(1, 9)]
                final_weights = final_weights + [weights]
                final_gradients = final_gradients + [gradients]
                final_post_sterio = final_post_sterio + [post_sterio]
        for a in range(inputs):
            for i in range(1+i):
                weights = weights + [random.randint(10000, 99999) // 1000]
                gradients = gradients + [random.randint(1, 2)]
                post_sterio = post_sterio + [random.randint(1, 9)]
                final_weights = final_weights + [weights]
                final_gradients = final_gradients + [gradients]
                final_post_sterio = final_post_sterio + [post_sterio]
        final_value = ([final_weights],[final_gradients],[final_post_sterio])
        return final_value
    else:
        return None