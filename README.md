Swarm 

An evolutionary/hill-climbing AI built with Pygame that attempts to perfectly recreate whatever you draw on a canvas by evolving a swarm of circles. 

I built this project to explore how simple evolutionary algorithms and matrix mathematics can be used to optimize a visual image in real-time. Instead of using a traditional neural network, this AI relies completely on "survival of the fittest".

## 🧐 What does it do?

When you launch the app, you get a split-screen view:
1. **The Left Half (Your Canvas):** You use your mouse to draw any white stroke on a dark grey background.
2. **The Right Half (The AI Canvas):** The AI takes 150 (originally 1500!) randomly scattered neon green circles and slowly mutates them until they perfectly match the shape of your drawing.

As you draw, the AI is constantly calculating a "loss" score and evolving its circles to improve its accuracy percentage, which you can see live at the bottom of the screen!

## 🧠 How it Works Under the Hood

The whole process relies on a fast feedback loop of Mutation, Evaluation, and Selection.

### 1. The Swarm (The Candidates)
We start with a list of `Pipe` objects (which are actually circles now!). Every frame, the algorithm creates a mutated copy of this list. It picks a random circle and says:
* *"Move slightly left or right"*
* *"Move slightly up or down"*
* *"Change your radius"*
* **OR (The secret sauce):** *"Do a Frog Jump and teleport to a completely random spot!"*

### 2. The Evaluation (NumPy Matrix Math)
How does it know if a mutation was good or bad? 
Behind the scenes, we convert the Pygame canvases into massive 3D NumPy arrays (Width × Height × RGB). We then subtract the AI's test canvas from the User's drawn canvas. 
Because Neon Green `(0, 255, 150)` is closer to White `(255, 255, 255)` than the Dark Grey background `(20, 20, 20)` is, any circle that lands on your white strokes will mathematically reduce the total error (the "loss"). 

### 3. Selection (Survival of the Fittest)
* If the loss goes **UP** 📈: The mutation was bad (the circle hit the black background). The AI scraps the change.
* If the loss goes **DOWN** 📉 (or stays the same): The mutation was good! The AI accepts the new mutated list and keeps going.

### 4. Escaping Local Minima
Sometimes circles get "stuck" in a corner where any small nudge makes the loss worse. This is why I added the **Frog Jump** mechanic. By randomly teleporting a circle across the screen, the AI can jump out of "local minima" and discover entirely new strokes it was missing before. We even track "Frog Hits" in the UI to see how many teleports successfully stuck!

## 🚀 How to Run It

Make sure you have Python and Pygame installed:
```bash
pip install pygame numpy
```

Then simply clone the repo and run:
```bash
python3 main.py
```

## 🎮 Controls
* **Mouse Left Click:** Draw on the left canvas.
* **C Key:** Clear the canvas and start a new drawing.

*Note: The AI stops calculating once it hits 99.99% accuracy to save CPU!*
