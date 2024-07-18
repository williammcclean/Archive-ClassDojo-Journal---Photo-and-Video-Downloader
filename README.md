# Archive ClassDojo Journal - Photo and Video Downloader by kecebongsoft

Download all ClassDojo photos and videos in your timeline by kecebongsoft.

"Tested on a Mac with Safari! It should be similar for other devices and browsers"
<br />
What it does:

	1.	Fetches a list of items from your ClassDojo timeline.
	2.	Collects URLs for the attachments of each item.
	3.	Downloads the files (photos, videos) into a local directory and saves the timeline activity as a JSON file.
<br />
How to Use:

	1.	Modify Session Cookies:
	•	Open ClassDojo in your browser and login.
	•	Enable Dev Tools and on the web page right click, Inspect Element, then go to Storage then Cookies.
	•	Copy the following vaules from the cookies: dojo_log_session_id, dojo_login.sid, and dojo_home_login.sid.
	•	Paste them into the SESSION_COOKIES section of the script.
<br /><br />
<img width="691" alt="Screenshot 2024-07-17 at 09 56 19" src="https://github.com/user-attachments/assets/a47ca4bf-b3c8-449a-85d1-70104100b2b4">
<br />
<br />
<img width="309" alt="Screenshot 2024-07-17 at 09 55 31" src="https://github.com/user-attachments/assets/ea8ff1cb-0dda-4603-b8e9-d380c91becb6">
<br />
<br />
<img width="505" alt="Screenshot 2024-07-17 at 09 57 59" src="https://github.com/user-attachments/assets/bc9922b8-fbcb-44ac-863c-e1c342cb02c8">
<br /><br /><br />
 
	2.	Install Python and Run the Script:
	•	Open Terminal.
	•	Run the script using "python script_name.py"
	•	You files will be listed in the deafult folder shown in Terminal.
 <br />
 
 <img width="398" alt="Screenshot 2024-07-17 at 10 48 57" src="https://github.com/user-attachments/assets/c12ef08d-aa44-4638-b490-fc868af4a326">


	•	If you get an error about classdojo_output you might need to create this folder in the User directory 
 <br /> <br />
<img width="398" alt="Screenshot 2024-07-18 at 13 25 56" src="https://github.com/user-attachments/assets/ad5af7e9-053f-4db9-81b0-38e46859a72d">
