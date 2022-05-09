# VirtualCamera
Program written in python and pygame, which implements simple virtual camera with painters algorithm. I decided to implement:
  - movement in each direction: x, y, z, upward, downward, backward, forward
  - rotation of camera in 3 direction by: x, y, z axis
  - and zoom
  - removal of hidden surfaces 

To simplify this problem this camera do not implement:
  - clipping
  - depth of field

<p align="center">
  <img src="https://user-images.githubusercontent.com/66008982/167433037-8d34d2d3-e974-48c9-8b3d-8efdd13ae3d6.png" />
</p>

To improve painters algorith, I split each wall into n smaller walls, because of this operation, painters algorithm is cappable of working with overlapping cubes.

<p align="center">
  <img src="https://user-images.githubusercontent.com/66008982/167432785-65147c50-383e-42f0-bbef-38e8500d4837.png" />
</p>


