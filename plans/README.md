# Ideas and Plans
1. Allow robot to speak
2. Allow robot to hear speech (interpreted by LLM to be made useful)
3. Allow robot to see objects in the world (YOLO)
4. Allow robot to see faces (face detect)
5. Allow robot to learn a name of a face
6. Allow robot to recognize a face
7. Allow robot to have a map of the locations of objects in 2D space
   Further idea, have each object's confidence level also be stored, and have the confidence degrade over time (degradation is added according to the left side of bell curve)
8. Allow robot to map area
9. Allow robot to navigate to an object
10. Give a set of instructions to the LLM which will interpret down to specific commands. (For example, "run and see if the fish is still there" will get interpreted as "go to object fish", "look at object fish", "tell me if the object fish is present") The commands would be interpreted using normal Python code.
