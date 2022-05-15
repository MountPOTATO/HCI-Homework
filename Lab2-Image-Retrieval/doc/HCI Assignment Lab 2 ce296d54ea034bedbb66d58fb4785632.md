# HCI Assignment Lab 2

- Course: Human Computer Interaction
- Student: Kaixin Chen
- ID: 1951724
- Tutor: Shen Ying

## How to Run

Activate an flask environment and locate to the project directory, and enter:

```bash
cd server
flask run
```

**Due to limited upload size,  some files are not included in the repo. Please make sure you added the follow folders and files.**

1. database folder
2. imagenet folder
3. Saved_features_recom.txt on ./server

PLUS, **Make sure to have full tags loaded in server/database/tags directory!!!**

```shell
in server/database/tags:

.
├── README.txt
├── animals.txt
├── baby.txt
├── baby_r1.txt
├── bird.txt
├── bird_r1.txt
├── car.txt
├── car_r1.txt
├── clouds.txt
├── clouds_r1.txt
├── dog.txt
├── dog_r1.txt
├── female.txt
├── female_r1.txt
├── flower.txt
├── flower_r1.txt
├── food.txt
├── indoor.txt
├── lake.txt
├── male.txt
├── male_r1.txt
├── night.txt
├── night_r1.txt
├── people.txt
├── people_r1.txt
├── plant_life.txt
├── portrait.txt
├── portrait_r1.txt
├── river.txt
├── river_r1.txt
├── sea.txt
├── sea_r1.txt
├── sky.txt
├── structures.txt
├── sunset.txt
├── transport.txt
├── tree.txt
├── tree_r1.txt
└── water.txt
```



## Snapshots and Functionality:

### Home Page (Formulation)

3 buttons are given: an upload button (**Formulation: contains an input box to upload an image**), a search button (**Initiation: has a search button**) and a favorite button.

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled.png)

### Upload Image (Formulation)

**Formulation: Users can preview the query image in the searching window**

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%201.png)

### Search

**Review: Provides an overview of the results (top 6 in total)**

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%202.png)

### Filter

**Refinement: allows changing the tag when reviewing results.**

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%203.png)

### Favorite

**Use: users can add selected images to a favorite list**

The results will be memorized during the runtime of this project.

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%204.png)

The favorite mark is still on when launching another search.

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%205.png)

The favorite button is given.

![Untitled](HCI%20Assignment%20Lab%202%20ce296d54ea034bedbb66d58fb4785632/Untitled%206.png)