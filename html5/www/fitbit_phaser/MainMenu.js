Fitbit.MainMenu = function (game) {

	this.music = null;
	this.playButton = null;

};

Fitbit.MainMenu.prototype = {

	create: function () {

		//	We've already preloaded our assets, so let's kick right into the Main Menu itself.
		//	Here all we're doing is playing some music and adding a picture and button
		//	Naturally I expect you to do something significantly better :)
		console.log("Nu zijn we in mainmenu")

		this.music = this.add.audio('titleMusic');
		this.music.loop = true;
		this.music.play();
		//this.add.sprite(0, 0, 'background');
		//this.add.sprite(0, 0, 'titlepage');
		console.log("Nu zijn we in mainmenu bis")
		//this.playButton = this.add.button(400, 600, 'button-start', this.startGame, this, 'buttonOver', 'buttonOut', 'buttonOver');
		this.playButton = this.add.button(300, 100, 'button-start', this.startGame, this, 1, 0, 2);
		//laatste drie parameters zijn de frames: button over, button out..
		//this.add.button(Candy.GAME_WIDTH-401-10, Candy.GAME_HEIGHT-143-10, 'button-start', this.startGame, this, 1, 0, 2);
		console.log("Nu zijn we in mainmenu ter")
	},

	update: function () {

		//	Do some nice funky main menu effect here

	},

	startGame: function (pointer) {

		//	Ok, the Play Button has been clicked or touched, so let's stop the music (otherwise it'll carry on playing)
		//this.music.stop();
		console.log("Nu gaan we naar game")
		//this.music.stop();
		//	And start the actual game
		this.state.start('Game');

	}

};
