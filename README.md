# Project 4: React /Python Django PostgreSQL DB Full-stack CRUD Application
 
## Description
 
My final project was to create another Full Stack Web Application using Python, Django and PostgreSQL, for the backend, while the front end was run on React. This was our third full CRUD Application (Create, Read, Update and Delete) however the challenge this time was to do it combining a few technologies that we had not combined before. Once again, I chose to build an app for another of my passions, photography. My idea was to develop an app where people could share great photographs. As a photographer I have become very disillusioned with Instagram as it has become a bit of a contest for the most likes and follows, and it has also become dominated by stories, reels and videos, not to mention algorithms and advertising. Exposure is a place to showcase beautiful still images, where they won’t be uploaded and forgotten within 30 minutes.
Deployment link
 
My project was deployed to GitHub and Railway and can be found by clicking the link below:
 
project-4-frontend-production.up.railway.app/  
 
## Timeframe
 
This was a solo project following the content we had been taught over the final module. We were given seven working days to complete, from planning to submission, however we did lose nearly a day for an additional tutorial on deployment and S3 Buckets.
We received the brief late on a Wednesday afternoon and were expected to begin planning and coding as soon as we had decided on a suitable project. Being the final project there was a certain amount of expectation to make this the best project that we could, so I was certainly feeling the pressure to choose wisely.  This meant reading, rereading, and understanding the brief, prior to deciding on an idea, planning, and being ready to start first thing Monday morning. Once I had come up with an idea, I drew up a rough plan in Excalidraw, and made an ERD of the basic Schema with Lucidchart. I also set up the repos as we would be working with a Back End and a Front End. My goals were to get most of the Back End coded and have Postman and Mongo DB working on Monday, then to start the Front End on Tuesday and into Wednesday. I wanted to have full functionality by midday on Thursday leaving me some time to style, proof and deploy before 14:00 on Friday.  
Technologies Used
 
The main aim of this project was to utilise the skills that we had learned in Python, Django, PostgreSQL and React. We would of course be using Axios, JavaScript and CSS, as well. I also used Bootstrap, Bootswatch, Excalidraw, Lucidchart and Adobe Photoshop to style, plan, compose an ERD and create a logo respectively. 
 
## Brief
Technical Requirements
Your App Must:
 
Be a full-stack Django/React application.
Connect to and perform data operations on a PostgreSQL database.
If consuming an API (OPTIONAL), have at least one data entity (Model) in addition to the built-in User model. The related entity can be either a one-to-many (1:M) or a many-to-many (M:M) relationship. 
If not consuming an API, have at least two data entities (Models) in addition to the built-in User model. It is preferable to have at least one one-to-many (1:M) and one many-to-many (M:M) relationship between entities/models. 
Have full-CRUD data operations across any combination of the app's models (excluding the User model). For example, creating/reading/updating posts and creating/deleting comments qualifies as full-CRUD data operations.
Authenticate users using Django's built-in authentication.
Implement authorization by restricting access to the Creation, Updating & Deletion of data resources** using the `login required` decorator in the case of view functions; or, in the case of class-based views, inheriting from the `LoginRequiredMixin` class.
Be deployed online using Railway. Presentations must use the deployed application.
 
The app may optionally:
Upload images to AWS S3
Consume an API installation of the Requests package will be necessary.  
 
## Planning
 
Once I had come up with a concept that I was happy with, and one that I thought would work well, I began planning, firstly the functionality and after that, the aesthetic I wanted for the final user experience. 
There were limitless options to choose from, but following the advice of my tutors, I chose to make an app for a personal passion, photography. I had a pretty good idea of what I wanted the finished product to look like, so after drawing up the ERD I got drafting an idea in Excalidraw. I like committing ideas to paper, so I also had a double page spread of A4 as a scratchpad to jot ideas down along with a rough timeline of what I wanted completed by when.  


 





## Build/Code Process
 
STEP BY STEP THROUGH THE PROCESS


1. 	Once I had chosen a project idea, I needed to create an ERD diagram illustrating the basic Schema.
2. 	With the ERD worked out I could draw a rough plan in Excalidraw
3. 	Before I could start coding, I had to set up two repos, one for the Back End and one for Front End.
4. 	Having done this, I needed to install all the dependencies for each one. 
5. 	The next stage was to set up the backend and create a PostgreSQL database.
6. 	Once this was ready, I had to set up the localhost 3000 port and make sure this was connected to the database and the Django Framework.
7. 	With the database in place, I could set up my Views in Python, followed by the Models and urls, and then test it all with Postman.
8. 	With the database all connected I could set up an admin page on the Django Framework on the backend so that I could see all of the data and requests.
9. 	The next step was to be able to add photographs via the backend, through the admin panel on localhost 3000, at this stage I was only able to load images by url.
10.  Now that I had my database connected to the back end, I could create a “super user” so that only I could make certain changes.
11.  With myself set up as the superuser, I then set about creating login and signup pages
12.  On the Front End I started to make all the pages that were going to display content and ensured that they were all properly connected to my back end.
13.  Once I had a homepage and image view page that were seeing images that were loaded from the admin panel on the back end. I could go ahead and create the login and sign up pages.
14.  With those in place I could then set about creating an Amazon S3 bucket and connecting that to my database. With this working I could then make a start on being able to upload images from the frontend.
15.  The beauty of the S3 bucket system is that you can upload by selecting images from files or folders on your computer or phone.
16.  With this process now working I could create a “POST” or image upload form.
17.  The next task was to implement a delete function so that images could be removed, this was a case of writing code on the front end and creating the “Delete” button.
18.  At this point the app was able to Create, Read, and Delete, all that was left was the update.
19.  Initially the plan was for people to be able to like and comment on the images and for them to be searched for by category/keyword, however time was running out so all I could manage was to update the category and keywords for the image.
20.  The final stage prior to deployment was to spend some time on styling and create a more visually appealing user interface. This was done with a combination of regular CSS, Bootstrap and Bootswatch.
21.  Deployment to Railway was the final step.





The snippet of code below is from my backend and shows a section of the views.py one of the key parts of the app. It is the “GET” request to get an object and then, if there is an image it gets uploaded to the AWS S3 bucket. It also creates the object in the database with the URL along with any additional data like keyword or category.


````python
def create(self, request):
       print(request)
       photo_file = request.FILES.get('image', None)
       if photo_file:
           s3 = boto3.client('s3')
           key = f"{uuid.uuid4().hex[:6]}_{photo_file.name}"
           try:
               bucket = os.environ['S3_BUCKET']
               s3.upload_fileobj(photo_file, bucket, key)
               url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
               print('Generated URL:', url)      
               Image.objects.create(url=url, keywords=request.data.get('keywords'),category=request.data.get('category'))
               return Response(status=status.HTTP_205_RESET_CONTENT)
           except Exception as e:
               print('An error occurred uploading file to S3')
               print(e)
           return Response(status=status.HTTP_400_BAD_REQUEST)
````


The function below handles the submission of the form data (including the image file, keywords, and category) to the backend server using a “POST” request. It provides error handling for failed requests and triggers actions upon successful upload.


 const handleSubmit = async (e) => {
   e.preventDefault();


   const formData = new FormData();
   formData.append('image', image);
   formData.append('keywords', keyword);
   formData.append('category', category);


   try {
     await axios.post(`${process.env.REACT_APP_BACKEND_URL}/images/`, formData, {
       headers: {
         'Content-Type': 'multipart/form-data',
       },
     });
     handleUploadSuccess();
     window.location.reload()
   } catch (error) {
     console.error('Error uploading image:', error);
   }
 };


## Challenges
 
The most daunting part of this project for me was the combining of various technologies that we had been taught. In the final Module we just learned Python and Django and in all of the exercises we did, we never combined them as part of a full stack Application, instead we built a single stack application which was directly rendered to a webpage. For this project we had to combine React (for the front end) with Python and Django, so had no real reference to look back on. Aside from that I had quite a few issues getting my detail modal for the images to render with consistent size margin and padding and space at the bottom for keywords as Bootstrap was conflicting with CSS. The thumbnails were also tricky and, in the end, I cheated as I ensured all the images I uploaded were square. I was hoping to keep the boxes square and constrain either the height or width to get landscapes and portraits to sit well within the containers on my grid.
 
  
## Wins 

Finally getting all the CRUD functionality working was a massive relief in the end as I was getting close to the deadline. I was very satisfied with the final look and feel of the app, especially when remembering the first rendering of the Front End with no styling.
 
## Key Learnings/Takeaways
 
Being our final project there was a lot of pressure to build something special. Our previous project had been a group effort, now, back on an individual undertaking, I was solely responsible for every single aspect of the project. I soon realised that I had bigger ambitions than I had time. The biggest lesson learned was not to bite off more than I can chew. I think the ability to assess current progress and amend the final goal is a more realistic way of working rather than ploughing on and not meeting the minimum requirements. I was also happy with how I managed to utilise Bootstrap better than I had in the past. I also enjoyed using the Amazon S3 bucket for storing images, it is a lot easier than needing a url for every image.
 

1. 	Being realistic about the amount of work that can be achieved within a finite time frame.
2. 	Amazon S3 Buckets are a great way to store images.
3. 	I developed a much better understanding of Bootstrap on this project.
4. 	Understanding the logs on the Railway during deployment and being able to correct the issues.
 
 
## Bugs
 
There are no real bugs that I have come across in the final version yet, there are however some things that are not working as well as I would have liked, but they are all listed below in future improvements. 
 

## Future Improvements
 
I think that there is quite a lot of scope to improve my app if I had had more time, however my primary goal was to satisfy the requirements of the brief. With the benefit of more time, these are some improvements that I would like to implement:
I would like to amend the user privileges so that only the user or myself as superuser could delete images.
I had planned to add a comment and like function to each individual image.
I wanted to be able to search for images by keyword and category, at present they are editable and are saved to the database, however they do not display.
Protecting user’s copyright was also a part of my plan. I was hoping to disable right click, so that the images could not be downloaded.
Writing this readme has also made me look at the app in quite a bit more detail and I have just realised that I would like to reverse the order of the feed, so the newer images are displayed at the top of the feed. 
 
 
View of the final app. Homepage on the left and a shot of the image modal on the right.
 
 
 






