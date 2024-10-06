using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoneMapping : MonoBehaviour
{
    public Animator animator; // Animator component of the rigged character

    // Bone Transforms
    private Transform hips, spine, spine1, spine2;
    private Transform leftShoulder, leftArm, leftForeArm, leftFingerBase;
    private Transform rightShoulder, rightArm, rightForeArm, rightFingerBase;
    private Transform leftUpLeg, leftLeg, leftFoot, leftToeBase;
    private Transform rightUpLeg, rightLeg, rightFoot, rightToeBase;

    // Mediapipe keypoints (update these vectors with real-time keypoints)
    public Vector3 mediapipeLeftShoulderKeypoint, mediapipeRightShoulderKeypoint;
    public Vector3 mediapipeLeftElbowKeypoint, mediapipeRightElbowKeypoint;
    public Vector3 mediapipeLeftWristKeypoint, mediapipeRightWristKeypoint;
    public Vector3 mediapipeLeftHipKeypoint, mediapipeRightHipKeypoint;
    public Vector3 mediapipeLeftKneeKeypoint, mediapipeRightKneeKeypoint;
    public Vector3 mediapipeLeftFootKeypoint, mediapipeRightFootKeypoint;
    public Vector3 mediapipeLeftToeKeypoint, mediapipeRightToeKeypoint;
    public Vector3 mediapipeSpineBaseKeypoint, mediapipeSpineMidKeypoint;
    public Vector3 mediapipeSpineTopKeypoint;

    public MediapipeOutput mediapipeOutput;

    void Start()
    {
        // Accessing bones using the HumanBodyBones enum
        hips = animator.GetBoneTransform(HumanBodyBones.Hips);
        spine = animator.GetBoneTransform(HumanBodyBones.Spine);
        spine1 = animator.GetBoneTransform(HumanBodyBones.Chest);
        spine2 = animator.GetBoneTransform(HumanBodyBones.UpperChest);

        leftShoulder = animator.GetBoneTransform(HumanBodyBones.LeftShoulder);
        leftArm = animator.GetBoneTransform(HumanBodyBones.LeftUpperArm);
        leftForeArm = animator.GetBoneTransform(HumanBodyBones.LeftLowerArm);
        leftFingerBase = animator.GetBoneTransform(HumanBodyBones.LeftHand);

        rightShoulder = animator.GetBoneTransform(HumanBodyBones.RightShoulder);
        rightArm = animator.GetBoneTransform(HumanBodyBones.RightUpperArm);
        rightForeArm = animator.GetBoneTransform(HumanBodyBones.RightLowerArm);
        rightFingerBase = animator.GetBoneTransform(HumanBodyBones.RightHand);

        leftUpLeg = animator.GetBoneTransform(HumanBodyBones.LeftUpperLeg);
        leftLeg = animator.GetBoneTransform(HumanBodyBones.LeftLowerLeg);
        leftFoot = animator.GetBoneTransform(HumanBodyBones.LeftFoot);
        leftToeBase = animator.GetBoneTransform(HumanBodyBones.LeftToes);

        rightUpLeg = animator.GetBoneTransform(HumanBodyBones.RightUpperLeg);
        rightLeg = animator.GetBoneTransform(HumanBodyBones.RightLowerLeg);
        rightFoot = animator.GetBoneTransform(HumanBodyBones.RightFoot);
        rightToeBase = animator.GetBoneTransform(HumanBodyBones.RightToes);
    }

    // This method will be called by PoseReceiver
public void UpdateBonePositions(Vector3[] keypoints)
{
    if (keypoints == null || keypoints.Length < 15) // Ensure you have at least 15 keypoints
        return;

    // Update hips
    if (hips != null)
    {
        hips.position = (keypoints[11] + keypoints[12]) / 2; // Average of left and right hips
        Vector3 hipsDirection = keypoints[12] - keypoints[11]; // Direction between hips
        hips.rotation = Quaternion.LookRotation(hipsDirection);
    }

    // Update spine
    if (spine != null && spine1 != null && spine2 != null)
    {
        spine.position = keypoints[0]; // Spine Base
        spine1.position = keypoints[1]; // Spine Mid
        spine2.position = keypoints[2]; // Spine Top

        Vector3 spineDirection = keypoints[1] - keypoints[0];
        Vector3 spine1Direction = keypoints[2] - keypoints[1];

        spine.rotation = Quaternion.LookRotation(spineDirection);
        spine1.rotation = Quaternion.LookRotation(spine1Direction);
    }

    // Update left arm
    if (leftShoulder != null && leftArm != null && leftForeArm != null)
    {
        leftShoulder.position = keypoints[5]; // Left Shoulder
        leftArm.position = keypoints[6];      // Left Elbow
        leftForeArm.position = keypoints[7];  // Left Wrist

        Vector3 leftArmDirection = keypoints[6] - keypoints[5]; // Shoulder to Elbow
        Vector3 leftForeArmDirection = keypoints[7] - keypoints[6]; // Elbow to Wrist

        leftShoulder.rotation = Quaternion.LookRotation(leftArmDirection);
        leftArm.rotation = Quaternion.LookRotation(leftForeArmDirection);
    }

    // Update right arm
    if (rightShoulder != null && rightArm != null && rightForeArm != null)
    {
        rightShoulder.position = keypoints[2]; // Right Shoulder
        rightArm.position = keypoints[3];      // Right Elbow
        rightForeArm.position = keypoints[4];  // Right Wrist

        Vector3 rightArmDirection = keypoints[3] - keypoints[2]; // Shoulder to Elbow
        Vector3 rightForeArmDirection = keypoints[4] - keypoints[3]; // Elbow to Wrist

        rightShoulder.rotation = Quaternion.LookRotation(rightArmDirection);
        rightArm.rotation = Quaternion.LookRotation(rightForeArmDirection);
    }

    // Update left leg
    if (leftUpLeg != null && leftLeg != null && leftFoot != null)
    {
        leftUpLeg.position = keypoints[11]; // Left Hip
        leftLeg.position = keypoints[13];   // Left Knee
        leftFoot.position = keypoints[15];  // Left Ankle

        Vector3 leftLegDirection = keypoints[13] - keypoints[11]; // Hip to Knee
        Vector3 leftFootDirection = keypoints[15] - keypoints[13]; // Knee to Ankle

        leftUpLeg.rotation = Quaternion.LookRotation(leftLegDirection);
        leftLeg.rotation = Quaternion.LookRotation(leftFootDirection);
    }

    // Update right leg
    if (rightUpLeg != null && rightLeg != null && rightFoot != null)
    {
        rightUpLeg.position = keypoints[12]; // Right Hip
        rightLeg.position = keypoints[14];   // Right Knee
        rightFoot.position = keypoints[16];  // Right Ankle

        Vector3 rightLegDirection = keypoints[14] - keypoints[12]; // Hip to Knee
        Vector3 rightFootDirection = keypoints[16] - keypoints[14]; // Knee to Ankle

        rightUpLeg.rotation = Quaternion.LookRotation(rightLegDirection);
        rightLeg.rotation = Quaternion.LookRotation(rightFootDirection);
    }

    // Update left toe
    if (leftToeBase != null)
    {
        leftToeBase.position = keypoints[17]; // Left Toe
    }

    // Update right toe
    if (rightToeBase != null)
    {
        rightToeBase.position = keypoints[18]; // Right Toe
    }
}


    void Update()
    {
        // Update the hips based on the mediapipe keypoints
        if (hips != null)
        {
            hips.position = (mediapipeLeftHipKeypoint + mediapipeRightHipKeypoint) / 2;
            Vector3 directionHips = mediapipeRightHipKeypoint - mediapipeLeftHipKeypoint;
            hips.rotation = Quaternion.LookRotation(directionHips);
        }

        // Update spine based on mediapipe spine keypoints
        if (spine != null && spine1 != null && spine2 != null)
        {
            spine.position = mediapipeSpineBaseKeypoint;
            spine1.position = mediapipeSpineMidKeypoint;
            spine2.position = mediapipeSpineTopKeypoint;

            Vector3 directionSpine = mediapipeSpineMidKeypoint - mediapipeSpineBaseKeypoint;
            Vector3 directionSpine1 = mediapipeSpineTopKeypoint - mediapipeSpineMidKeypoint;

            spine.rotation = Quaternion.LookRotation(directionSpine);
            spine1.rotation = Quaternion.LookRotation(directionSpine1);
        }

        // Update the left arm bones
        if (leftShoulder != null && leftArm != null && leftForeArm != null)
        {
            leftShoulder.position = mediapipeLeftShoulderKeypoint;
            leftArm.position = mediapipeLeftElbowKeypoint;
            leftForeArm.position = mediapipeLeftWristKeypoint; // Use forearm keypoint if available

            Vector3 directionLeftArm = mediapipeLeftElbowKeypoint - mediapipeLeftShoulderKeypoint;
            Vector3 directionLeftForeArm = mediapipeLeftWristKeypoint - mediapipeLeftElbowKeypoint;

            leftShoulder.rotation = Quaternion.LookRotation(directionLeftArm);
            leftArm.rotation = Quaternion.LookRotation(directionLeftArm);
            leftForeArm.rotation = Quaternion.LookRotation(directionLeftForeArm);
        }

        // Update the right arm bones
        if (rightShoulder != null && rightArm != null && rightForeArm != null)
        {
            rightShoulder.position = mediapipeRightShoulderKeypoint;
            rightArm.position = mediapipeRightElbowKeypoint;
            rightForeArm.position = mediapipeRightWristKeypoint; // Use forearm keypoint if available

            Vector3 directionRightArm = mediapipeRightElbowKeypoint - mediapipeRightShoulderKeypoint;
            Vector3 directionRightForeArm = mediapipeRightWristKeypoint - mediapipeRightElbowKeypoint;

            rightShoulder.rotation = Quaternion.LookRotation(directionRightArm);
            rightArm.rotation = Quaternion.LookRotation(directionRightArm);
            rightForeArm.rotation = Quaternion.LookRotation(directionRightForeArm);
        }

        // Update the left leg bones
        if (leftUpLeg != null && leftLeg != null && leftFoot != null)
        {
            leftUpLeg.position = mediapipeLeftHipKeypoint;
            leftLeg.position = mediapipeLeftKneeKeypoint;
            leftFoot.position = mediapipeLeftFootKeypoint;
            leftToeBase.position = mediapipeLeftToeKeypoint;

            Vector3 directionLeftLeg = mediapipeLeftKneeKeypoint - mediapipeLeftHipKeypoint;
            Vector3 directionLeftFoot = mediapipeLeftFootKeypoint - mediapipeLeftKneeKeypoint;

            leftUpLeg.rotation = Quaternion.LookRotation(directionLeftLeg);
            leftLeg.rotation = Quaternion.LookRotation(directionLeftFoot);
            leftFoot.rotation = Quaternion.LookRotation(directionLeftFoot);
        }

        // Update the right leg bones
        if (rightUpLeg != null && rightLeg != null && rightFoot != null)
        {
            rightUpLeg.position = mediapipeRightHipKeypoint;
            rightLeg.position = mediapipeRightKneeKeypoint;
            rightFoot.position = mediapipeRightFootKeypoint;
            rightToeBase.position = mediapipeRightToeKeypoint;

            Vector3 directionRightLeg = mediapipeRightKneeKeypoint - mediapipeRightHipKeypoint;
            Vector3 directionRightFoot = mediapipeRightFootKeypoint - mediapipeRightKneeKeypoint;

            rightUpLeg.rotation = Quaternion.LookRotation(directionRightLeg);
            rightLeg.rotation = Quaternion.LookRotation(directionRightFoot);
            rightFoot.rotation = Quaternion.LookRotation(directionRightFoot);
        }
    }
}
