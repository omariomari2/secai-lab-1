# SecAI+ Lab 1: How AI models learn (and fail)

Personal coursework notes for Bright Owusu.

Date: October 14, 2026 (Central Time).

## Part A: Train a neural network

All runs used the spiral dataset, classification, X1 and X2 inputs, Tanh activation, and a learning rate of 0.03.
Batch size was 10. Regularization was None, with a rate of 0.
The default and larger runs used seed 0.25258. The noisy run used seed 0.38080 after the data settings changed.

| Run | Neurons per hidden layer | Noise | Training data | Epochs | Training loss | Test loss |
| --- | --- | --- | --- | --- | --- | --- |
| Default | 4, 2 | 0 | 50% | 325 | 0.433 | 0.486 |
| Larger | 8, 8, 8 | 0 | 50% | 1080 | 0.005 | 0.016 |
| Noisy | 8, 8, 8 | 50 | 10% | 780 | 0.303 | 0.611 |

The default network did not separate the spiral well after 325 epochs, approximately the requested 300 epochs.
The larger network followed the spiral well after 1080 epochs.
The larger run also had more training time, so this comparison does not isolate network size.

### Default network

![Two hidden layers: 4 and 2 neurons. Test loss: 0.486.](docs/images/a1-default.jpg)

Two hidden layers: 4 and 2 neurons. Test loss: 0.486.

### Larger network

![Three hidden layers: 8, 8, and 8 neurons. Test loss: 0.016.](docs/images/a2-larger.jpg)

Three hidden layers: 8, 8, and 8 neurons. Test loss: 0.016.

### Noise and limited training data

![Noise: 50. Training data: 10%. Test loss: 0.611.](docs/images/a3-noisy.jpg)

Noise: 50. Training data: 10%. Test loss: 0.611.

### What happened in step A4?

With noise at 50 and training data at 10%, training loss was 0.303 and test loss was 0.611. The model fit the training examples better than the unseen test examples. This gap is evidence of overfitting: the model learned details that did not apply well to new data.

### Why does data poisoning concern a defender?

An attacker can add false examples or incorrect labels to the training data. The model can learn these errors and miss attacks or flag safe activity as a threat. This attack is called data poisoning.

## Part B: Tokens

Tool: [OpenAI Tokenizer](https://platform.openai.com/tokenizer).
Selected model group: `GPT-5.x & O1/3`.
Inputs contained no leading spaces or final newline.

| Input type | Exact input | Tokens | Characters |
| --- | --- | --- | --- |
| English | `The model learns from training data.` | 7 | 36 |
| Python | `print("Hello, world!")` | 6 | 22 |
| Example string | `Gr@mbl1ng!2026` | 8 | 14 |

Rare strings split into more tokens because the tokenizer represents unfamiliar character sequences with smaller pieces from its vocabulary.

The example string was split into `Gr`, `@m`, `bl`, `1`, `ng`, `!`, `202`, and `6`.

### Tokenizer evidence

![English sentence](docs/images/b1-english.jpg)

![Python code](docs/images/b2-python.jpg)

![Example string](docs/images/b3-rare-string.jpg)

## Run settings

These links restore the settings. They do not restore the trained weights or recorded epoch count.

- [Default](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.25258&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
- [Larger](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=8,8,8&seed=0.25258&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
- [Noisy](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=50&networkShape=8,8,8&seed=0.38080&showTestData=false&discretize=false&percTrainData=10&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

## References

- [TensorFlow Playground](https://playground.tensorflow.org/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
