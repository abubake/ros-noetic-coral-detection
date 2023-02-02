<!-- PROJECT LOGO -->
<br />

  <h3 align="center"> # ros-noetic-coral-detection</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
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
