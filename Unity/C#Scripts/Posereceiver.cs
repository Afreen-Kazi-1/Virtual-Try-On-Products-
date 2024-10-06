using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;             
using System.Net.Sockets;     
using System.Text;            // Add this for encoding/decoding strings
using Newtonsoft.Json;        // Add this for JSON deserialization
using System.Threading; 

public class PoseReceiver : MonoBehaviour
{
    public Transform[] keypoints; // Keypoint placeholders
    public BoneMapping boneMapping;
    private UdpClient client;
    private IPEndPoint remoteEndPoint;
    
    void Start()
    {
        client = new UdpClient(5005); // Adjust port if needed
        remoteEndPoint = new IPEndPoint(IPAddress.Any, 0);
        Thread receiveThread = new Thread(ReceiveData);
        receiveThread.Start();
    }

    void ReceiveData()
{
    while (true)
    {
        try
        {
            byte[] data = client.Receive(ref remoteEndPoint);
            string jsonData = Encoding.UTF8.GetString(data);
            Debug.Log("Received Data: " + jsonData);  // Log received data
            
            // Deserialize JSON array into Vector3[]
            Vector3[] poseKeypoints = JsonConvert.DeserializeObject<Vector3[]>(jsonData);
            UpdatePose(poseKeypoints);
             // Send the keypoints to BoneMapping
            boneMapping.UpdateBonePositions(poseKeypoints);
        }
        catch (Exception e)
        {
            Debug.LogError(e.ToString());
        }
    }
}


    void UpdatePose(Vector3[] poseKeypoints)
    {
        if (poseKeypoints != null && poseKeypoints.Length == keypoints.Length)
        {
            for (int i = 0; i < keypoints.Length; i++)
            {
                keypoints[i].position = poseKeypoints[i];
            }
        }
    }
}
