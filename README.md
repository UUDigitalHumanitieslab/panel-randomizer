# Panel Randomizer #

Panel Randomizer is a Python/Django application to create URLs that forward to a specified LimeSurvey questionaire

* The respondent fills out his/her (student) ID, which is saved AES encoded in the database.
* Respondents are only forwarded one first time to a questionaire. If the respondents ID is retrieved from the database, the respondent is redirected to a screenout. 
* The resulting forwarding URL contains two GET variables (key-value pairs) that can be used to prefill questions in the Lime Survey questionaire:
	*  Respondent ID. The URL key can be named randomly in the admin (see: Manual)
	*  Branching. The URL key can be named randomly in the admin. The value in the URL is a rotating number, which runs from 1 to the limit value that is defined in the admin. Using this as a pre-answered value, a specified group of questions can be shown in LimeSurvey using LimeSurvey's so called 'relevance equation'<br><br>

* A javascript to run YouTube films. The YouTube player is activated without controls, and without pause/stop feature. After film ending LimeSurvery's 'next' button is automatically activated to turn the survey page.
* Recognizes the device of the participant. Desktop users wil be forwarded to a survey that is specified in the admin settings. Mobile users can be forwarded to an other specified survey that is optimized for mobile devices. If in the admin no mobile version is specified, all users are forwarded to the desktop version  

### Prerequisites ###
Python > 3.0 <br>
Django > 2.0<br>


### Next steps ###

Download or clone from GitHub<br>
Deploy on your server<br>
Have a LimeSurvey account ready

## Manual ##
1.  Create a survey in LimeSurvey (optional: with different groups)
2.  Put one or two questions in the first group to be prefilled by the URL of Panel Randomizer: student number and (optional) branching. These questions can be made 'hidden' optionally
3.  Optional: create other groups that will be shown if the answer on the routing question is 1 to ... [number of groups]. Fill out in 'relevance equation' of this group: [questionid]==[rotation number]. For example Q001==1. In this case this particular group will only show when the question Q001 was prefilled with 1 by the forwarding url made by Panel Randomizer.
4. in 'Panel integration' in Lime Survey settings, add the url parameters that are used for prefilling the answers. Choose a name for the student number parameter that needs to be taken from the url and assign the parameter to the target question from step 2.<br> Choose a name for the branching parameter (taken form the url of Panel Randomizer with the rotating group number) and assign the parameter to the target question for the branching from step 2.
5. Enter the Admin of Panel Randomizer. (https://panel-randomizer.hum.uu.nl/admin/)
6. Right from 'Surveys'  choose 'add'.
7. Fill out in the new screen:<br>
	* A survey name (required). This name will be used as the last part of the link for the respondents. E.g. https://panel-randomizer.hum.uu.nl/survey1. The name you entered was 'survey1'. Now all your settings for this survey will be retrieved and used.
	* Survey desktop url (required). This is the url you see in your LimeSurvey for desktop users under 'Survey URL'. Panel Randomizer wil generate this url with extra GET variables.
	* Survey mobile url (optional). The LimeSurvey url for the users of mobile devices.
	* Expected completion time. This will be shown on the welcome screen of Panel Randomizer
	* Group count. The number of groups that need to be rotated. The group number is passed as a GET variable (integer) in the forwarding URL generated by Panel Randomizer. For every new respondent this integer will be incremented with 1 until the max number is reached, and starts again at 1.
	* Integration parameter student enc (required). The parameter name you choose (in step 4) in LimeSurveys 'panelintegration' to save the (encrypted) student number. Please fill out the exact same name. The encrypted student number wil be passed as a GET variable in the URL to LimeSurvey with this name. I.e when you choose the name 'student' in panelintegration as the url parameter that prefills the student number question, please fill out the same name here. The forwarding URL to Limesurvey will then contain this: '&student=[encrypted number]'
	* Integration parameter branching (optional). The parameter name you choose in LimeSurveys 'panelintegration' to save the answer needed for showing a particular group. Please fill out the exact same name. I.e when you choose the name 'branch' in panelintegration as the url parameter that prefills the question that decides which group of questions is shown next, fill out 'branch' here as well. In the generated url the GET parameter will then contain this: '&branch=1', and a '1' will be prefilled as the question answer in LimeSurvey. For the next respondent the number will be '2' until the number you filled in 'Group count' is met.
	* click 'save'<br><br>
8. In order to test the connection to your LimeSurvey survey, use as a student number '123'. This number is (for the moment) availabele for testing purposes and will not be saved in the database of Panel Randomizer, as all other numbers will allow only one entry.
9. When you get 'Onderzoeksnaam ontbreekt of is onjuist', you probably forgot to add to the url the name of the survey you just created in Panel Randomizer admin. Please use a slash (/) and the survey name after the base url in the browser address bar 
10. To add a YouTube movie you need to add two lines of code to a question: 
 
`<script src="https://panel-randomizer.hum.uu.nl/static/panel_randomizer_app/js/YouTube_helper.js" async></script>`

`<div class="single-play-video" data-video-url="https://www.youtube.com/watch?v=9RTaIpVuTqE" id="video_player1"> </div>`

The first line starting with `<script>` will retrieve the javascript code that calls youtube_helper.js<br>
The second line will place a YouTube player, which will start automatically playing the url you entered. The url after 'data-video-url=' needs to be adjusted for the aimed video.

