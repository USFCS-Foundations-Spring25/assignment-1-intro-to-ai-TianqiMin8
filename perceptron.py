import random

## for each element, the first six items are the input, and the last is the
## expected output.

training_examples = [
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
]


def threshold(val):
    if val < 0:
        return 0
    else:
        return 1


def perceptron_training():
    alpha = 0.1
    bias = -0.1
    weights = [0] * 6
    ## each weight will be between -0.05 and 0.05
    for i in range(5):
        weights[i] = (random.random() / 10) - 0.05

    converged = False
    while not converged:
        converged = True
        for example in training_examples:
            ## you complete this part.
            ## first, compute actual output
            inputs = example[:-1]
            to = example[-1]
            # get output with current weights
            current = bias
            for i in range(0,5):
                current += weights[i]*inputs[i]

            o = threshold(current)
            err = to-o
            print(current, err)
            if err != 0:
                converged = False
                for i in range(0,5):
                    weights[i] = weights[i] + alpha * example[i] * err



            # just for checking:
            # after = 0
            # for i in range(0,5):
            #     after += weights[i]*inputs[i]
            # print(threshold(after+bias), example[-1])
            # w = w+alpha*tin[i]*Error // if error is negative, decrease from the old way
            # get errors amd try to update the weights


    ## print results
    for example in training_examples:
        total = bias
        inputs = example[:-1]
        for i in range(len(inputs)):
            total += weights[i] * inputs[i]
        output = threshold(total)
        print(f"Expected: {example[-1]} Actual: {output}")


perceptron_training()
