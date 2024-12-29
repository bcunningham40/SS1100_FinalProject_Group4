# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

### Cunningham	McCabe	Ryan (Cole)	Henderson

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

#### Project Writeup
1.	What was your experience in collaborating? Talk about what steps you used to ensure the inputs from group members worked - code testing, GitHub branch management, etc. - and how you divided up the workload for the project.

   Collaboration on GitHub was much easier than emailing or TEAMS messaging a .py or MATLAB file between the team. We used TEAMS messaging to provide status updates to the group, request help from each other, or provide input on how to tackle the next task. Everybody started with one section: Propulsion - Cole, Thermal - Billy, Attitude - Will, and Data Handling - Chris. We collaborated to finish those sections and then handled the last two sections with remaining bandwidth after finishing individual sections. The repository was a great common area to make updates and then save so everybody could see it.  We tested the code on each other’s IDE once everybody was completed, and ensured the code has compatibility between platforms. 
Lastly, the GitHub desktop was helpful when working with PyCharm. The PyCharm community function enabled opening of the code directly into PyCharm for edits.

2.	What was the most challenging section, and why? Feel free to provide more than one response if there is a difference of opinion in the group.

   The ACS section was difficult because it was hard to decipher what the end goal actually was. The other difficult apart of ACS was that it required import of code and functions from other python script. Where the code was located and and CWD gave us trouble because we did not understand the functionality of CWD.

   RCS was also challenging.  We decided to do the RCS section using MATLAB to fulfill the requirement of one section being done in MATLAB. Utilizing MATLAB proved difficult because some of the functionality is not as intuitive as Python. Additionally, there is a lot of code for almost any function you may need available online for Python, which is not necessarily the case for MATLAB. We had to search documentation within MATLAB to find the correct way to utilize the built-in functions that are already created in MATLAB. Overall, this manual research of functionality took a lot of time, whereas it can just be downloaded from a python library on the internet.

   Lastly, the Payload section was difficult.  We had little experience using the other library repositories beyond the examples in class.  Therefore, we used a great deal of ChatGPT assistance to show which functions to use and how everything worked for the remote sensing data analysis. 

3.	If you employed Generative AI tools, how did you do so? Discuss which tools you used, the prompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.
   
   Various sections required us to use ChatGPT to check our code and find better ways to accomplish some functionality.  Overall, it was very useful in explaining what steps were required and how to code to achieve the end state we wanted.  Lastly, it was very helpful using ChatGPT to review the code block and provide feedback or revisions with explanations.  Below are some specific examples of how we used Gen AI:
   
   ACS- ChatGPT 4o. Gave many prompts based on tasking. From there would give it step-by-step delineated tasks that I wanted to see happen. I would try the small portions and see if they worked as intended. If they did not, I replied with errors or incorrect outputs. With so many tasks within ACS it was important to give it instructions one at a time. If too many instructions were given, mistakes would compound themselves and I would have to start from the top once again.
   
   CD&H- ChatGPT 4o. I used a prompt along the lines of "How to match an item in a list with an item in a nested dictionary in python" to make the parsed input to the specific subsystems, codes, and parameters within the dictionary. While the result certainly was not perfect, it provided a jumping off point to tweak until the code worked. I tested the code provided in a python file and used trial and error until the code was working in the way that I wanted.
   
   Payload- ChatGPT 4o. Also provided many prompts based on tasking. The project task mentioned using Numpy, but Chat also recommended several other included Panda and MatPlotLib which I remembered from one of our periods of instruction. We used Chat to remediate issues we were having with the code. The code was resulting in a plot that was completely white. I entered the code into ChatGPT and asked why the plot was showing all white. It recommended checking the min/max values for each CSV. This returned a NaN error which ChatGPT recommended rectifying with conversion of the NaN to a numeric value. This resolved the problem and the image was visualized.
   
4.	What other resources did you use to find solutions? Online sites, books, references, etc.

   ACS- I looked up what CWD and its functionality via Google because it was giving me the hardest time. I also watched YouTube videos on how GitHub worked and how to update GitHub from the desktop app.
   
   Payload - I used a simple google search to figure out if it was possible and subsequently how to use a file path directly from GitHub to avoid computer specific path issues when loading the CSV files.

5.	In what way could this project be improved for future quarters?

   GitHub has been a bit of a learning curve. You have already mentioned in class that you plan to use it from the beginning of the quarter in the future. I think this would be helpful to address up front in the curriculum.  It's a great collaboration tool - in a separate class, we discussed software project management, and I can see how GitHub would be useful for a team to collaborate and use as a repository for something like Kanban project boards. We also found the GitLab website, which it looks like NPS may have an account. We would possibly recommend this for future quarters: https://gitlab.nps.edu/dashboard/projects
