# Electron Flight 13 Telemetry
Telemetry of Electron's Flight 13 using OCR with Tesseract in Python. Tesseract was trained with a custom font that uses slashed zeros. The artifacts in the video input caused some erroneous values, which were fixed by manual review. Additionally, I had to smooth the signals quite a bit.

Anyways, here are some pretty graphs:

##Acceleration-time:
![Acceleration-time graph](/graphs/acceleration-time.png "Acceleration-time graph")

##Trajectory:
![Trajectory graph](/graphs/trajectory.png "trajectory.png")