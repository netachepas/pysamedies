# Workshop Program


During our weekly meeting with Pysamedies (www.samedies.be) we originally setted to learn together some programming langages starting from Python. To this aim we chose to base on learning on datasets originating from personnal caption devices. Those tools seems to trigger a common interest between us, some of us wera already using them, others were thinking of doing so, some because they wanted to face the conséquences of a chronique desease, while others were intrigued by those props out of the desire to get a better overview of their health, or out of sheer curiosity, because they were interested by things related to health, as many women's group: their health or the health of the person they were taking care of.

## Short presentation of quantified self practices.

What is a dataset, and what is it used for?
  
As many of us are using tools to help us keeping our physicl shape, among other things by measuring our efforts, but how do they work? Electronic caption devices are integrated to those props, data is captured by those commercial interfaces (fitbit, apple watch, jawbone etc...), and is further transmited and hosted on the server of the corporations that offer their services (among other things their social network. Did you ever asked your self how those data look like?
Here are several data sets that you can download in order to look at how thi information looks like. Some are the self tracking data that commercial providers send you upon demand, some is regular sensing data:

  - [Fitbit](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/fitbit_export.csv)
  - [Jawbone](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/jawbone.csv)
  - [Accéléromètre](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/accelero.txt)
  - [Autre chose](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/autre_chose.mp3) 


Which informations are captured:
  - Weight
  - Number of glasses of water
  - Number of steps
  - Actives minuts/sleep

Furthermore the social network of each device also propose their service to help organize a community around fitness issues:
  - Possibility to set a personnalised eating program.
  - Possibility to organize a friends network who will help support your endeavour.
  - Possibility to synchrononise your fitness tracker with your smart phone that captures all sorts of other informations such as géolocalistion (through gps, but not only)


However there seems to be a number of things that the interface of these fitness trackers do not propose.
  - Inform contextual data would they be environemental (how is the weather), personnals (haven't got the time my kid got sick ), subjectives ( I am sad, deceveid anxious...).
  - Some very useful measures as the periodic table that lets you better know your cycle.
  - General health. 
  - Any type of particularities: I only have one leg, I am a small person, or following a hormon treatment) or only I do not fit the profile.

How to think a social interface that would take those difference into account as they make for the life of most of us.

## The issue of visuals 

Data is omnipresent, indeed we live in a time where everything can be measured Les données sont omniprésentes, nous vivons à une époque où nous pouvons tout mesurer, chaque détail, archiver chaque action de notre vie, nous en avons les moyens. Mais alors il faut un peu se pencher sur l'environnement dans lequel nous allons vivre au milieu de toutes ces données.
Que voulons nous exactement retranscrire, voulons nous que notre vie ressemble à un immense tableau de bord?
Aussi cet atelier vous proposera une interface en ligne pour regarder à quoi ressemblent ces données et envisager de les représenter différemment. 
 
### data workshop

How to get your data from the commercial websites.

It is feasible to recuperate one's data from fitbit using the interface of their website to achieve this one needs to follow a few simple steps:
  - First log onto your profile
  - Then clicking on the icon on the top right of the screenn goto settings/data export.
  - You will be able to chose the data that you want to download (body, activity, sleep etc...) and the period, one month is a maximum. 
  - Then you will need to choose the format of the file, (xls ou csv) during this workshop we will use a CSV file.

How to do one's own charts. 
  - Use those data sets and reinterpret them using MPL.
  - Associate new visuals that would be personnalised and allow us to step out of the * Dashboard * style to represent our bodies.

We propose during this workshop to reemploy tools developed during Pysamedies workshop, (Vera did many of them). 

#### How to start a python server.

Start a local server: by double-cliquing on the folder localCGIServer.py. 
This will open a window that will show: Localhost CGI started. 
You need to leave this window open during all the sesion, since closing it will shut down the server.

Open a browser and copy the following address to charge the program:
localhost:8080/fitbit_phaser/
( fitbit_phaser is the sub-file that contains the program itself. 

In the browser you can now see a new page, click Start and naviguate to the file fitbit_export.csv (or another csv file you might have downloaded from fitbit)


#### Which Images


The intrusive presence of digital system that visualize corporal practices is extremely intrusive we already have tried to ask ourselves how to transform the usual visuals, among other things we did a workshop during [Relearn](http://relearn.be) [more visuals here](http://water-wheel.net/media_items/view/5944) last august.

## Privacy in question: 

A fitness tracker is a tool that allows to retrace one's fitness habits to the aim of triggering behavioural change leading to a enhance wellbeing, however, this practice can eventually lead to unsuspected benefices for example in a number of place (up to now, not in Belgium) insurance company offer to their clients selftracking devices (fitbit le plus souvent). Furthermore, those companies propose benefices and all sorts of rewards to the clients that will share their data with them.

### Your fitness tracker can show that you are having an affair during lunch hour.

Many systems couple fitbit information with localisation features on smartphones for example, this allows to correlate many different information, even retrace the movements of people even tens of years after their death. This occurence is far more detailed then what we have been able to do up to now.

In this perspaective, certain persons have developed systems to lie to their [fitbit](http://www.unfitbit.com)

## Health data issue.

Are those self tracking data comparable to health data?
There is a fair amount of models that are usually employed in the health systems, they are characteristic of a medical relation.
  * How can a social network such as fitbit reemplace them?
  * Which should then be its characteristics? 
  * How to organise it, on which basis?
  * What should such a network be concerned about?

## Commercial issues.

[fitbit is on the stock market since august 2015](http://www.marketwatch.com./investing/stock/fit/profile)




g
