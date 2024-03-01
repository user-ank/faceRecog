# faceRecog
Project that detect and recognizes faces after providing proper training.

<h2>Steps to run the project:</h2>
<h3>Pre-requisites:</h3>
<p>1) You need to set up a MYSQL database which will store student information (This will store details of student against its user_id which will be shown at the time of detection, the training photos of users will be stored in the local machine itself).</p>
<p>2) Create a database(on mysqlworkbench OR xampp) with name:"face_recognition_system", host:"localhost", username:"root", password:""; Now start the database server.</p>
<p>3) Import the file named "face_recognition_system.sql" from the project directory. This will create the table for you.</p>
<p>4) Create an empty folder "data" inside "AI_FaceRecognition" folder.</p>
<p>5) Install all the required dependencies using requirements.txt</p>
<p>6) After installing, go to main.py and run.</p>
<h3>How to use the project:</h3>
<p>1) A UI window(1st) will open, Click on student detail.</p>
<p>2) Another window(2nd) will open, fill all the required details and click on save.</p>
<p>3) Then on the same window(2nd) there is "Take Photo Sample" button. Click on it and let the camera of your device take multiple pictures of you. These pictures will be stored in the "data" folder inside the project folder.</p>
<p>4) After the process completes go to the window(1st), there is a section named "Train Data", Click on it and wait till it completes. This trains the model based on the data provided.</p>
<p>5) Now again on window(1st) there is a section saying "Face Detection"; Click on it and a window with people in the frame of your camera will be visible.</p>
<p>6) It would detect and try to recognize the faces in that window. If the user data was trained then his information will be shown on his face otherwise it would say "unknown face".</p>
