[![Build Status](https://travis-ci.org/UUDigitalHumanitieslab/panelrandomizer.svg?branch=develop)](https://travis-ci.org/UUDigitalHumanitieslab/panelrandomizer)

Manual: [dhlab-manuals.sites.uu.nl/handleiding/panel-randomizer-manual](https://dhlab-manuals.sites.uu.nl/handleiding/panel-randomizer-manual/)

# Panel Randomizer #

Panel Randomizer is a Python/Django application to redirect participants to LimeSurvey questionnaires. It has the following features:

* Anonymises participant ID based on a student number.
* Limits participation to only one time, over multiple surveys.
* Detects device type and redirect to a mobile version of a survey.
* Helps rotating different question groups in a survey. 
* Helps displaying YouTube videos in a survey: the YouTube player is started without controls. After playing the video the participant is sent to the next page.

How it works:

* Participants fill out their (student) ID, which is saved AES encoded in the database.
* Participants are only forwarded one first time to a questionnaire. If the respondent's ID is already present in the database, the participant is redirected to a screenout page.
* Recognizes the device of the participant. Desktop users wil be forwarded to a survey that is specified in the admin settings. Mobile users can be forwarded to an other specified survey that is optimized for mobile devices. If in the admin no mobile version is specified, all users are forwarded to the desktop version  
* The resulting forwarding URL contains two GET variables (key-value pairs) that can be used to pre-fill questions in the Lime Survey questionnaire:
  * Respondent ID. The URL key can be named arbitrarily in the admin (see: Manual)
  * Branching. The URL key can be named arbitrarily in the admin. The value in the URL is a rotating number, which runs from 1 to the limit value that is defined in the admin. Using this as a pre-answered value, a specified group of questions can be shown in LimeSurvey using LimeSurvey's so called 'relevance equation'.

## Prerequisites ##

* Python > 3.0
* Django > 2.0

### Next steps ###

* Download or clone from GitHub.
* Deploy on your server.
* Have a LimeSurvey account ready.

## Manual ##

See: [dhlab-manuals.sites.uu.nl/handleiding/panel-randomizer-manual](https://dhlab-manuals.sites.uu.nl/handleiding/panel-randomizer-manual/)

1. Create a survey in LimeSurvey (optional: with different groups)
2. Put one or two questions in the first group to be pre-filled by the URL of Panel Randomizer: student number and (optional) branching. These questions can be made 'hidden' optionally
3. Optional: create other groups that will be shown if the answer on the routing question is 1 to ... [number of groups]. Fill out in 'relevance equation' of this group: `[questionid]==[rotation number]`. For example `Q001==1`. In this case this particular group will only show when the question `Q001` was pre-filled with 1 by the forwarding url made by Panel Randomizer.
4. in 'Panel integration' in Lime Survey settings, add the url parameters that are used for pre-filling the answers. Choose a name for the student number parameter that needs to be taken from the url and assign the parameter to the target question from step 2.<br> Choose a name for the branching parameter (taken form the url of Panel Randomizer with the rotating group number) and assign the parameter to the target question for the branching from step 2.
5. Enter the Admin of Panel Randomizer. (https://panel-randomizer.hum.uu.nl/admin/)
6. Right from 'Surveys'  choose 'add'.
7. Fill out in the new screen:
	* A survey name (required). This name will be used as the last part of the link for the participants. E.g. https://panel-randomizer.hum.uu.nl/survey1. The name you entered was 'survey1'. Now all your settings for this survey will be retrieved and used.
	* Survey desktop url (required). This is the url you see in your LimeSurvey for desktop users under 'Survey URL'. Panel Randomizer wil generate this url with extra GET variables.
	* Survey mobile url (optional). The LimeSurvey url for the users of mobile devices.
	* Expected completion time. This will be shown on the welcome screen of Panel Randomizer
	* Group count. The number of groups that need to be rotated. The group number is passed as a GET variable (integer) in the forwarding URL generated by Panel Randomizer. For every new participant this integer will be incremented with 1 until the max number is reached, and starts again at 1.
	* Integration parameter student enc (required). The parameter name you choose (in step 4) in LimeSurveys 'panelintegration' to save the (encrypted) student number. Please fill out the exact same name. The encrypted student number wil be passed as a GET variable in the URL to LimeSurvey with this name. I.e when you choose the name 'student' in panelintegration as the url parameter that prefills the student number question, please fill out the same name here. The forwarding URL to Limesurvey will then contain this: '&student=[encrypted number]'
	* Integration parameter branching (optional). The parameter name you choose in LimeSurveys 'panelintegration' to save the answer needed for showing a particular group. Please fill out the exact same name. I.e when you choose the name 'branch' in panelintegration as the url parameter that prefills the question that decides which group of questions is shown next, fill out 'branch' here as well. In the generated url the GET parameter will then contain this: '&branch=1', and a '1' will be prefilled as the question answer in LimeSurvey. For the next participant the number will be '2' until the number you filled in 'Group count' is met.
	* Click 'save'<br><br>
8. In order to test the connection to your LimeSurvey survey, use as a student number '123'. This number is (for the moment) available for testing purposes and will not be saved in the database of Panel Randomizer, as all other numbers will allow only one entry.
9. When you get 'Onderzoeksnaam ontbreekt of is onjuist', you probably forgot to add to the url the name of the survey you just created in Panel Randomizer admin. Please use a slash `/` and the survey name after the base url in the browser address bar.
10. To add a YouTube movie you need to add two lines of code to a question:

```html
<script src="https://panel-randomizer.hum.uu.nl/static/panel_randomizer_app/js/YouTube_helper.js" async></script>
<div class="single-play-video" data-video-url="https://www.youtube.com/watch?v=9RTaIpVuTqE"> </div>`
```

The first line starting with `<script>` will retrieve the javascript code that calls `youtube_helper.js`.
The second line will place a YouTube player, which will start automatically playing the url you entered. The url after `data-video-url=` needs to be adjusted for the aimed video.
