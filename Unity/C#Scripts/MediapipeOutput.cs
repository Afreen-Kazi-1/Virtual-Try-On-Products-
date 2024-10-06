using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MediapipeOutput : MonoBehaviour
{
    // Reference to the BoneMapping script
    public BoneMapping boneMapping;

    // This function will be called with the real-time Mediapipe keypoints data
    public void UpdateMediapipeKeypoints(MediapipeKeypointsData keypointsData)
    {
        // Update boneMapping keypoints from Mediapipe data
        boneMapping.mediapipeLeftShoulderKeypoint = keypointsData.leftShoulder;
        boneMapping.mediapipeRightShoulderKeypoint = keypointsData.rightShoulder;
        boneMapping.mediapipeLeftElbowKeypoint = keypointsData.leftElbow;
        boneMapping.mediapipeRightElbowKeypoint = keypointsData.rightElbow;
        boneMapping.mediapipeLeftWristKeypoint = keypointsData.leftWrist;
        boneMapping.mediapipeRightWristKeypoint = keypointsData.rightWrist;
        boneMapping.mediapipeLeftHipKeypoint = keypointsData.leftHip;
        boneMapping.mediapipeRightHipKeypoint = keypointsData.rightHip;
        boneMapping.mediapipeLeftKneeKeypoint = keypointsData.leftKnee;
        boneMapping.mediapipeRightKneeKeypoint = keypointsData.rightKnee;
        boneMapping.mediapipeLeftFootKeypoint = keypointsData.leftFoot;
        boneMapping.mediapipeRightFootKeypoint = keypointsData.rightFoot;
        boneMapping.mediapipeLeftToeKeypoint = keypointsData.leftToe;
        boneMapping.mediapipeRightToeKeypoint = keypointsData.rightToe;
        boneMapping.mediapipeSpineBaseKeypoint = keypointsData.spineBase;
        boneMapping.mediapipeSpineMidKeypoint = keypointsData.spineMid;
        boneMapping.mediapipeSpineTopKeypoint = keypointsData.spineTop;

        // Once the data is updated, BoneMapping will handle the positions and rotations in its Update() method.
    }
}

[System.Serializable]
public class MediapipeKeypointsData
{
    // These are the Mediapipe keypoints as Vector3
    public Vector3 leftShoulder;
    public Vector3 rightShoulder;
    public Vector3 leftElbow;
    public Vector3 rightElbow;
    public Vector3 leftWrist;
    public Vector3 rightWrist;
    public Vector3 leftHip;
    public Vector3 rightHip;
    public Vector3 leftKnee;
    public Vector3 rightKnee;
    public Vector3 leftFoot;
    public Vector3 rightFoot;
    public Vector3 leftToe;
    public Vector3 rightToe;
    public Vector3 spineBase;
    public Vector3 spineMid;
    public Vector3 spineTop;
}
