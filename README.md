# Virtual Try on of clothes

## Project:

The project takes a video of the user as input and attempts at creating a realistic cloth try on video as the output by the methods of pose estimation, mesh movements in unity, bone mapping and superimposition to process the final output.

### Input Video: 
![]()


### Output:
![]()



## Table of Contents
* [About the Project](https://github.com/Mr-MVP/Virtual-Try-On-Products-/tree/Final#about-the-project)
* [Process Flow](https://github.com/Mr-MVP/Virtual-Try-On-Products-/tree/Final#process-flow)
* [Applications](https://github.com/Mr-MVP/Virtual-Try-On-Products-n/blob/Final/README.md#applications)
* [File Structure](https://github.com/Mr-MVP/Virtual-Try-On-Products-/blob/Final/README.md#file-structure)
* [Installations and Execution](https://github.com/Mr-MVP/Virtual-Try-On-Products-/blob/Final/README.md#installations-and-execution)
* [Tech Stack](https://github.com/Mr-MVP/Virtual-Try-On-Products-/tree/Final#tech-stack)
* [Future Prospects](https://github.com/Mr-MVP/Virtual-Try-On-Products-/blob/Final/README.md#future-prospects)
* [Contributors](https://github.com/Mr-MVP/Virtual-Try-On-Products-/blob/Final/README.md#contributors)
* [Acknowledgements and Resources](https://github.com/Mr-MVP/Virtual-Try-On-Products-/blob/Final/README.md#acknowledgements-and-resources)


## About the Project:

Our approach consists of first performing Pose estimation of the given video. The pose received from this step is sent to Unity engine. The keypoints received are mapped on the mesh present in Unity.

We create pose simulation of the cloth using the keypoints received from Mediapipe. This simulation runs on a rigged mesh i.e a mesh skinned to the skeleton and each joint having its weight painted. 

After the simulation is created, this video is then sent to a python script which uses OpenCV functions for superimposition. The script considers the keypoints of the human body while superimposition. The shoulder and hips coordinates are considered.


### Process Flow

![]()
![]()


1. **Input**: The input will be a video of the user. The video file should be in .mp4 file format. 

![]()


2. **Pose estimation:** For the given video, pose estimation will be applied. As we are using Mediapipe for pose estimation we get the coordinates of 33 different keypoints for a single frame. These coordinates are then sent to Unity for creating the cloth simulation video.

![]()


3. **Replicating human pose in Unity**: Using the keypoints received from Mediapipe, each keypoint is mapped to its corresponding bone/joint in the mesh imported in Unity. We also make sure the mesh is rigged to avoid any unexpected movements. Also directions are mapped to the bones to avoid deformations of the mesh while output is being generated. 

![]() 
      
![]()
   
4. **Generating simulation video**: Using the movements of cloth mesh the simulation video is generated. We make sure that the simulation and input video have same length to avoid lagging of cloth mesh in the final output. 

      
![]()

![]()
   
5. **Superimposition of videos**: We use the functions offered by the OpenCV in order to superimpose the input video and simulation video.
   
   ![]()
   


## Applications

* **Online Shopping**: Allows customers to virtually try on clothing before purchasing. Helps customers make more informed decisions, potentially reducing return rates.

* **Lighting**: Visualize different lighting options and their effects.

* **Virtual Photo Booths**: Create fun, shareable images with virtual costumes and props.


## File Structure
```
 📦Virtual-Try-On-Products 
 ┣ 📂assets                            # Contains gifs, objs and images of the results 
 ┣ 📂2D                                # Approaches and scripts for 2D TryOn
 ┃ ┣ ACGPN                               # Used to create and save masks of objects from input image
 ┃ ┣ End-to-End                          # Run this notebook to get results
 ┣ 📂3D
 ┃ ┣ 3D Pose Estimation                # Used to estimate pose and keypoints
 ┃ ┣ Unity                             # Scripts for integrating mediapipe to Unity and pose update scripts
 ┃ ┣ DigiHuman                         # Scripts for rigging and pose update in Unity. 
 ┃ ┣ Superimposition                   # Blend simulated mesh with reference video. 
 ┣ 📜README.md
 ┣ 📜demo_video.gif                    # Demo Video
 ┣ 📜project_report.docx               # Project Report
 ┗ 📜requirements.txt                  # Requirements 
 ```

## Installations and Execution



## Tech Stack

* Unity Engine

* OpenCV
  
* Mediapipe
  
* Python, C#


## Future Prospects

* We are able to create an output *video*. In future we aim at making the project realtime.

* The mesh used is not properly scaled with the human body during superimposition. We aim at improving the quality of mesh either by modifying the mesh we currently use or by making one from scratch.

* Currently, we do not consider the lightning in the video's environment. Therefore we plan to take into consideration the lightning conditions which will improve the output quality in different surroundings of the user.

## Mentor
* [Mrudul Pawar](https://github.com/Mr-MVP)

## Contributors

* [Afreen Kazi](https://github.com/Afreen-Kazi-1)
* [Mahi Palimkar](https://github.com/mahipalimkar)
* [Ishaan Shaikh](https://github.com/Ishaan0132)

## Acknowledgements and Resources

* [DigiHuman](https://github.com/Danial-Kord/DigiHuman)

* [ACGPN paper](https://arxiv.org/pdf/2003.05863)
