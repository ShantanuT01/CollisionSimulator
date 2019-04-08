# CollisionSimulator
Physics elastic and inelastic collision simulator 
## Elastic Collision
Momentum is conserved but objects do not stick to each other in a collision. <br />
Formula for velocities: <br />
given that object A and B's mass are equal to m and M, respectively, and initial velocity of A and B is v and u,respectively <br />
final velocity of A = (m - M)/(m+M) * v + 2M/(m+M) * u <br />
final velocity of B = 2m/(m+M) * v + (M-m)/(m+M) * u <br />

## Assumptions
Assumptions made in the system (Python Canvas) is that there is no friction between the spheres and the surface and that momentum is conserved in collisions. When the sphere hits the edge of the canvas, its velocity is reflected. For example, if a sphere hits the top with a y-velocity of 4 m/s, the sphere's new y-velocity would be -4 m/s. It basically delivers an impluse of 2p, where p is the initial momentum before hitting the wall. 

## Running the Collision Simulator
Download the files and put them in the same folder. Run the Runner.py through your IDE or through Terminal/Command Prompt. 
