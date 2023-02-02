<!-- PROJECT LOGO -->
<br />

  <h3 align="center"> # ros-noetic-coral-detection</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#Step-by-step Demonstration">Step-by-step Demonstration</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

**Author:** Baker Herrin
**GatorID:** 5153-5125
**ROS version:** ROS Noetic
**OS Version:** Ubuntu 20.04
**ROS Package name:** coral_detector

Description:
Currently face detection using opencv cascades for the detection, but will be updated to detect coral heads.
Repository works as is and is stable on master, but still under development.

<!-- QUICKSTART -->
## TL;DR quickstart
To replicate results:
If you don't already have ROS installed or don't have the correct version...
- install ROS noetic on Ubuntu 20.04. I used Vmware Player on my System76 Gazelle.
- Create your catkin workspace
- Follow the ROS installation tutorials at http://wiki.ros.org/noetic/Installation/Ubuntu if you are new to ROS
- After making sure your setup.bash files are properly sourced:

```
roscd catkin_ws/src
git clone https://github.com/abubake/ros-noetic-coral-detection.git
roscd catkin_ws
catkin_make
roslaunch coral_detector coral_detector_py.launch
```
<!-- Step-by-step Demonstration -->
## Step-by-step Demonstration

Start by opening up 3 terminals, I used Tilix.

![Screenshot from 2023-02-02 08-56-41](https://user-images.githubusercontent.com/32299736/216391496-b5d76817-48ae-4d8c-add5-264510f6c79c.png)

Then run roscore. Make sure you have properly sourced your workspace.
![Screenshot from 2023-02-02 09-01-04](https://user-images.githubusercontent.com/32299736/216392017-9acedeb7-020a-4570-a543-a0588d9cce17.png)

For proper sourcing, add these lines to your bashrc as seen below. I used "vim ~/.bashrc to open it in the terminal to edit it.
```
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
```
Then roscd into coral_detector and then run roslaunch coral_detector coral_detector_py.launch
Unfortunately it only detects faces for now, but hopefully coral soon!
![Screenshot from 2023-02-02 09-12-48](https://user-images.githubusercontent.com/32299736/216394899-b36326d3-8a4f-4366-9caf-72e92474fe75.png)


Here is an example of the face detection. I have a node that outputs each frame undetected (just a video steam) and also the frame with the detection.
![Screenshot from 2023-02-02 09-09-45](https://user-images.githubusercontent.com/32299736/216394111-1b0be9bb-01f5-4309-b064-ad60b452571a.png)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- Authors -->
## Authors

Baker Herrin - eherrin@ufl.edu

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Catia Silva](https://faculty.eng.ufl.edu/catia-silva/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Awesome readme template!](https://github.com/catiaspsilva/README-template)

## Thank you

<!-- If this is useful: [![Buy me a coffee](https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg)](https://www.buymeacoffee.com/catiaspsilva) -->
