# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

### Assignment
- **Instructions**: Work in groups of four to complete the steps outlined in the project instructions.
- **Submission**: All of your submission will go here in this repository, to include this README file to hold your writeup.

### Procedure
#### Preparation
- Employ programming skills to solve problems related to spacecraft subsystems.
- Develop code and responses to tasks in various sections.
- Experience working with code and collaborating on a coding project.

#### Requirements
1. Complete all tasks listed in each section, paying attention to the Evaluation subsections.
2. Use MatLab to complete at least one of the tasks.
3. Submit the project using GitHub, replacing the content of this README file with your writeup and presentation of the work.

#### Subsystems and Tasks
Reaction Control Subsystem (RCS): Malfunction detection and velocity change calculation.\
Thermal Control Subsystem (TCS): Temperature control function.\
Attitude Control Subsystem (ACS): Attitude determination and rotation calculations.\
Command and Data Handling (C&DH): Command parsing and routing.\
Electrical Power Subsystem (EPS): Power budget analysis and battery charging calculations.\
Remote Sensing Payload: Data ingestion, radiance to reflectance conversion, and image rescaling.

#### Project Writeup (Update as we go)
1. What was your experience in collaborating? Talk about what steps you used to ensure the
inputs from group members worked - code testing, GitHub branch management, etc. - and
how you divided up the workload for the project.

Collaboration on GitHub was much easier than emailing or TEAMS messaging a .py or matlab file.  We used TEAMS messaging to provide status updates to the group, request help, or provide input on how to tackle the next task.  Everybody started with one section: Propulsion - Cole, Thermal - Billy, Attitude - Will, and Data Handling - Chris.  We collaborated to finish those sections and then handled the last two sections with remaining bandwidth after finishing individual sections.  The repository was a great common area to make updates and then save so everybody could see it.  GitHub desktop was helpful when working with PyCharm.  Pycharm community function enabled opening the code directly into Pycharm to edit.  

2. What was the most challenging section, and why? Feel free to provide more than one response if there is a difference of opinion in the group.

ACS section was difficult because it was hard to decipher what the end goal actually was.  The other difficult apart of ACS was that it required import of code and functions from other python script.  Where the code was located and and CWD gave us trouble because we did not understand the functionality of CWD.  The TCS section was pretty straightforward, and I'm pleased to say the majority of it did not require Gen AI assistance.  

3. If you employed Generative AI tools, how did you do so? Discuss which tools you used, the prompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.

ACS- ChatGPT 4o.  Gave many prompts based on tasking.  From there would give it step by step delinieated tasks that I wanted to see happen.  I would try the small portions and see if they worked as intended.  IF they did not I replied with errors or incorrect outputs.  With so many tasks within ACS it was important to give it instructions one at a time.  If to much was instruction was given mistakes would compound themselves and I would have to start form the top once again. 

CD&H- ChatGPT 4o.  I used a prompt along the lines of "How to match an item in a list with an item in a nested dictionary in python" to make the parsed input to the specific subsystems, codes, and parameters within the dictionary.  While the the result certainly was not perfect, it provided a jumping off point to tweek until the code worked.  I tested the code provided in a python file and used trial and error until the code was working in the way that I wanted.

Payload- ChatGPT 4o.  Also provided many prompts based on tasking. The project task mentioned using Numpy, but Chat also recommended several other included Panda and MatPlotlib which I remembered from one of our periods of instruction.  We used Chat to remediate issues we were having with the code.  The code was resulting in a plot that was completely white.  I entered the code into ChatGPT and asked why the plot was showing all white.  It recommended checking the min/max values for each CSV.  This returned a NaN error which ChatGPT recommended rectifying with conversion of the NaN to a numeric value.  This resolved the problem and the image was visualized.

4. What other resources did you use to find solutions? Online sites, books, references, etc.

ACS- I looked up what CWD and its funcionality via Google because it was giving me the hardest time.  I also watched Youtube videos on how Github worked and how to update Github from the destop app. 

Payload - I used a simple google search to figure out if it was possible and subsequently how to use a file path directly from GitHub to avoid computer specific path issues when loading the CSV files.
   
5. In what way could this project be improved for future quarters?

GitHub has been a bit of a learning curve.  You have already mentioned in class that you plan to use it from the beginning of the quarter in the future.  I think this would definitely be helpful.  It's a great collaboration tool - in a separate class, we discussed software project management, and I can see how GitHub would be useful for a team to collaborate and use as a repository for something like Kanban project boards.  We found the GitLab website, which it looks like NPS may have an account.  Would possibly recommend this for future quarters:https://gitlab.nps.edu/dashboard/projects
