
Fitbit.Preloader = function (game) {

	this.background = null;
	this.preloadBar = null;

	this.ready = false;

};

Fitbit.Preloader.prototype = {

	preload: function () {

		//	These are the assets we loaded in Boot.js
		//	A nice sparkly background and a loading progress bar
		//this.background = this.add.sprite(0, 0, 'preloaderBackground');
		this.preloadBar = this.add.sprite(300, 300, 'preloaderBar');

		//	This sets the preloadBar sprite as a loader sprite.
		//	What that does is automatically crop the sprite from 0 to full-width
		//	as the files below are loaded in.
		this.load.setPreloadSprite(this.preloadBar);

		//	Here we load the rest of the assets our game needs.
		//	As this is just a Project Template I've not provided these assets, swap them for your own.
		this.load.image('background', 'images/background.png');
		//this.load.image('titlepage', 'images/title.png');
		this.load.spritesheet('button-start', 'images/button-start.png', 401, 143);
		//this.load.atlas('playButton', 'images/play_button.png', 'images/play_button.json');
		this.load.audio('titleMusic', ['audio/happyloop.mp3']);
		//this.load.audio('titleMusic', ['audio/background.mp3','audio/background.ogg', 'audio/background.wav' ]);

		//this.load.bitmapFont('caslon', 'fonts/caslon.png', 'fonts/caslon.xml');
		//	+ lots of other required assets here

		this.load.image("img0", "images/animation0.jpg");
		this.load.image("img1", "images/animation1.jpg");
		this.load.image("img2", "images/animation2.jpg");
		this.load.image("img3", "images/animation3.jpg");
		this.load.image("img4", "images/animation4.jpg");
		this.load.image("img5", "images/animation5.jpg");
		this.load.image("img6", "images/animation6.jpg");
		this.load.image("img7", "images/animation7.jpg");
		this.load.image("img8", "images/animation8.jpg");
		this.load.image("img9", "images/animation9.jpg");
		this.load.image("img10", "images/animation10.jpg");
		this.load.image("img11", "images/animation11.jpg");
		this.load.image("img12", "images/animation12.jpg");
		this.load.image("img13", "images/animation13.jpg");
		this.load.image("img14", "images/animation14.jpg");
		this.load.image("img15", "images/animation15.jpg");
		this.load.image("img16", "images/animation16.jpg");
		this.load.image("img17", "images/animation17.jpg");
		this.load.image("img18", "images/animation18.jpg");
		this.load.image("img19", "images/animation19.jpg");

		this.load.image("node", "images/node_klein.png");
		this.load.image("node_highlight", "images/node_highlight.png");
		this.load.image("hand", "images/Hand_black.png")
		this.load.image("cursor", "images/cursor.png");
		this.load.image("sound", "images/sound2.png");
		this.load.image("soundOff", "images/sound2b.png");
		this.load.image("retry", "images/retry.png");


	},

	create: function () {
		console.log("Nu zijn we in preloader")
		//	Once the load has finished we disable the crop because we're going to sit in the update loop for a short while as the music decodes
		this.preloadBar.cropEnabled = false;

	},

	update: function () {

		//	You don't actually need to do this, but I find it gives a much smoother game experience.
		//	Basically it will wait for our audio file to be decoded before proceeding to the MainMenu.
		//	You can jump right into the menu if you want and still play the music, but you'll have a few
		//	seconds of delay while the mp3 decodes - so if you need your music to be in-sync with your menu
		//	it's best to wait for it to decode here first, then carry on.
		
		//	If you don't have any music in your game then put the game.state.start line into the create function and delete
		//	the update function completely.
		
		if (this.cache.isSoundDecoded('titleMusic') && this.ready == false)
		{
			this.ready = true;
			console.log("sound decoded, overgang naar openfile")
			//this.state.start('MainMenu');
			this.state.start('OpenFile');

		}

	}

};
