# Earthling Virtual Avatar(EVA)

AGI

# Magnum Opus:
Constructing an artificial brain based on the structure of a real brain is a highly complex endeavor that spans multiple fields including neuroscience, computer science, and artificial intelligence. Here’s an approach to this challenge:

Lets go for the original intention of NN!
Producing a real brain, a true neural network


### Approach:

1. *Understand Brain Structure and Function:*
   - *Neuroanatomy:* Study the anatomy of the brain, including regions such as the cortex, hippocampus, and cerebellum, and understand their specific functions.
   - *Neuronal Dynamics:* Understand how neurons communicate through synapses, including action potentials, neurotransmitters, and synaptic plasticity.
   - *Network Architecture:* Study how neurons form networks and the overall connectivity patterns in different brain regions.

2. *Data Collection and Preprocessing:*
   Brain Imaging Data: Open Neuro
     - *MRI/fMRI:* To get structural and functional information about the brain.
     - *DTI (Diffusion Tensor Imaging):* To understand the white matter tracts and connectivity.
   Electrophysiological Data: Open Neuro
     - *EEG/MEG:* To capture electrical activity of the brain.
     - *Single-Neuron Recordings:* To understand the firing patterns of individual neurons.
   - *Behavioral Data:*
     - *Cognitive Tests:* To relate brain activity to behavior and cognition.
     - *Sensory Inputs and Motor Outputs:* To understand the input-output relationships in the brain.

3. *Modeling Neurons and Synapses:*
   - *Biophysical Models:*
     - *Hodgkin-Huxley Model:* For detailed ionic mechanisms.
     - *Izhikevich Model:* For simpler yet biologically plausible simulations.
   - *Synaptic Plasticity:*
     - *Hebbian Learning:* To simulate learning processes.
     - *STDP (Spike-Timing-Dependent Plasticity):* To model temporal learning rules.

4. *Building Neural Networks:*
   - *Microcircuits:*
     - Simulate small networks of neurons to understand local processing.
   - *Macro-scale Networks:*
     - Integrate microcircuits to form larger brain regions and interconnect them.
   - *Connectivity Patterns:*
     - Use connectome data to define the connections between different regions.

5. *Training and Validation:*
   - *Data-Driven Models:*
     - Use machine learning to train networks based on brain data (e.g., using deep learning architectures like CNNs, RNNs).
   - *Reinforcement Learning:*
     - Implement learning mechanisms where the artificial brain can learn from interactions with the environment.
   - *Comparison with Biological Data:*
     - Validate the artificial brain’s behavior and activity patterns against real brain data.

### Relevant Data for Machine Learning Training:

1. *Neuroimaging Data:*
   - MRI/fMRI for structural and functional brain mapping.
   - DTI for understanding connectivity.
   
2. *Electrophysiological Data:*
   - EEG/MEG for large-scale brain activity.
   - Local field potentials and single-neuron recordings for detailed neuronal dynamics.
   
3. *Genomic and Proteomic Data:*
   - To understand the molecular basis of brain function and variability.
   
4. *Behavioral and Cognitive Data:*
   - Data from cognitive tests, sensory inputs, and motor outputs to relate brain activity to function.
   
5. *Connectomics Data:*
   - Detailed maps of neuronal connections (e.g., from initiatives like the Human Connectome Project).
   
6. *Simulated Data:*
   - Data from biophysical simulations to understand how changes at the microscopic level affect overall brain function.
   
7. *Environmental Interaction Data:*
   - Data on how the brain interacts with and learns from the environment, potentially from virtual reality setups or robotic interfaces.

### Summary:

The approach involves a comprehensive understanding of brain structure and function, collecting a wide array of data, building detailed models of neurons and synapses, and constructing neural networks that mimic the connectivity and dynamics of the brain. The artificial brain is then trained using relevant machine learning techniques and validated against real brain data. This multidisciplinary effort would require collaboration across neuroscience, computer science, and related fields.

The first step: Steering - See Roombas
Valence - good and bad - turning - modulate valence based on state
Affect: Arousal - valence: side 60
Classification of input into differrent emetions - physicsl output

Basic Vertebrate brain:
Cortex, basal ganglia, Thalamus, hypothalamus, midbrain, hindbrain

Reinforcement learning: trial and error
Temporal difference learning: learning on the go - critic and actor

Basal ganglia: learns to repeat and maximize dopamine releasing actions - the actor

Hypothalamus: house the valence neurouns and controls dopamine release, control cold, warmth, hunger and so on - more advanced steering brain - the critic

Basal ganglia is a student who tries to satisfy its judge - hypothalamus is the decider of the actual rewards

With time the dopamine rewards are given from the basal ganglias predictions instead of the actual hypothalamus rewards

Cortex and the sensory neurons are what give info about the external world
Few olfactory neurons connect to many cortex neurons, but the cells only connect to a few cells.

Neurons:
Photosensory
Mechanosensory
Olfactory
Pyramidal

Catastrophic forgetting: networks forget former patterns when introduced to new ones 
The invariance problem: how to recognize patterns as the same despite different inputs

Thalamus: 3D blackboard?

Inductive bias: assumption by the model by design not by learning

The cortex somehow solves invariance, catastrophic forgetting, discriminates patterns and generalizes patterns to new experiences and does it all without supervision.

It is an advantage for reinforcement learning to be able to recognize a lot of stuff.

Explotation-exploration
Reinforced exploring new things

Neural compass: head directions neurons and the vestibular sense. Places cells that only activate at certain locations.

Midbrain, hindbrain: reflexive movement.

The three sub cortexes:
The lateral cortex: smell - olfactory cortex
The ventral cortex: sight and sound - amygdala
The medial cortex: the neural compass - hippocampus

The fourth cortex
Neocortex: ability to simulate
The neocortex in humans contains seperate cortex for all five senses

Neocortical columns, a fundamental algorithm?
Six layers
Layer 6: Project to the thalamus
Layer 5: Project to the basal ganglia, the thalamus and motor area
Layer 4: input from the thalamus
Layer 1: Input from the thalamus

Perception:
Filling in, one at a time, cant unsee
Generative models - predicting without an answer using genrating and recognition

How does the neocortex simulate? Assumptions?

A general AI model that uses narrow assumptions. It doesnt have to learn uneccesary stuff, but assumes it.

World models that predicts consequences of actions and to search and plan to achieve goals, is what is missing from AI

The ability to create a decoupled world in your mind: imagination

Vicarious trial and error: predicting trial and error
Counterfactual learning: learning from wrong choices - causation, when this happens something else also happens

Episodic memory: recall specific past episodes
Procedural memory: remember movements

Hippocampus used to learn patterns quickly, neo cortex simulates the world and brings back old patterns
This is called generative or experience replay and can resolve catastrophic forgetting

Prioritizing, look at the actors best hunches

Adapt to specific situations utilizing different strategies

Sensory neo cortex: simulation of external world - here simulations are rendered

Frontal neocortex: gPFC, aPFC and motor cortex - here simulations are controlled
Granular cells: layer 4 neocortex
Motor and aPFC missing layer 4

Learn the model to explain its own behaviour

Only needs model when there is uncertainth

A voting system for the best choice

Goal driven or habitual behaviour, model based or model free - aPFC has a goal, basal ganglia does not

Passive and active inference: explaining sensory input and explaining behavior

Layer 4 renders simulation that matches incoming sensory data
The aPFC doesnt want to match incoming data, it wants to match intent and correct the basal ganglia mistakes, so no layer 4

So aPFC starts with learning from behaviour of the basal ganglia and then when it has learned it teaches the basal ganglia

Motor cortex controls motor commands. It predicts the next motion and then acts it out vis the somatosensory cortex.
Its like the aPFC, but it learns complex movements instead

Theory of mind, the granular prefrontal cortex and the STS and TPJ, the ability to put yourself in others shoes and understand intention of intention

Mirror neurons that activate when watching others doing stuff

Premotor activation is necessary for imitation learning

Teacher-student drive alongside the AI and teach it on the way

Inverse reinforcement, the system first tries to learn the reward function(intent) before learning the actualt action by trial and error
So it creates it own reward function which is usually hard coded

Predicting needs of future self is likely predicting needs of others - theory of mind

Mentalizing:
Theory of mind, imitation learning and anticipating
This is a second order generative model

Representative heurestic - brain generalization

Shared attention, proto language and labeling

Mentalizing and language has too be combined

Wennickes and brocks area for speech understanding and formulation

Swarm intelligence

Unsupervised learning

## Project structure

The directory structure of the project looks like this:
```txt
├── .github/                  # Github actions and dependabot
│   ├── dependabot.yaml
│   └── workflows/
│       └── tests.yaml
├── configs/                  # Configuration files
├── data/                     # Data directory
│   ├── processed
│   └── raw
├── dockerfiles/              # Dockerfiles
│   ├── api.Dockerfile
│   └── train.Dockerfile
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── models/                   # Trained models
├── notebooks/                # Jupyter notebooks
├── reports/                  # Reports
│   └── figures/
├── src/                      # Source code
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── data.py
│   │   ├── evaluate.py
│   │   ├── models.py
│   │   ├── train.py
│   │   └── visualize.py
└── tests/                    # Tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_data.py
│   └── test_model.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── pyproject.toml            # Python project file
├── README.md                 # Project README
├── requirements.txt          # Project requirements
├── requirements_dev.txt      # Development requirements
└── tasks.py                  # Project tasks
```


Created using [mlops_template](https://github.com/SkafteNicki/mlops_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting
started with Machine Learning Operations (MLOps).
