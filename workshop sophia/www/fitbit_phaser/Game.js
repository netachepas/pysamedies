

Fitbit.Game = function (game) {

    //  When a State is added to Phaser it automatically has the following properties set on it, even if they already exist:

    this.game;      //  a reference to the currently running game (Phaser.Game)
    this.add;       //  used to add sprites, text, groups, etc (Phaser.GameObjectFactory)
    this.camera;    //  a reference to the game camera (Phaser.Camera)
    this.cache;     //  the game cache (Phaser.Cache)
    this.input;     //  the global input manager. You can access this.input.keyboard, this.input.mouse, as well from it. (Phaser.Input)
    this.load;      //  for preloading assets (Phaser.Loader)
    this.math;      //  lots of useful common math operations (Phaser.Math)
    this.sound;     //  the sound manager - add a sound, play one, set-up markers, etc (Phaser.SoundManager)
    this.stage;     //  the game stage (Phaser.Stage)
    this.time;      //  the clock (Phaser.Time)
    this.tweens;    //  the tween manager (Phaser.TweenManager)
    this.state;     //  the state manager (Phaser.StateManager)
    this.world;     //  the game world (Phaser.World)
    this.particles; //  the particle manager (Phaser.Particles)
    this.physics;   //  the physics manager (Phaser.Physics)
    this.rnd;       //  the repeatable random number generator (Phaser.RandomDataGenerator)

    //  You can use any of these from any function within this State.
    //  But do consider them as being 'reserved words', i.e. don't create a property for your own game called "world" or you'll over-write the world reference.

    var imageSize = 250;
    //this.curve = [[15, 25], [30, 44], [45, 373], [60, 220], [75, 189], [90, 200], [105, 165], [120, 258], [135, 251], [150, 157]];
    //var curve = [[15, 25], [30, 44], [45, 373], [60, 220], [75, 189], [90, 200], [105, 165], [120, 258], [135, 251], [150, 157], [165, 113], [180, 360], [195, 234], [210, 374], [225, 959], [240, 630], [255, 391], [270, 7], [285, 348], [300, 155], [315, 131], [330, 220], [345, 229], [360, 257], [375, 576], [390, 124], [405, 220], [420, 670], [435, 374], [450, 199], [465, 111], [480, 219], [495, 134], [510, 208], [525, 180], [540, 110], [555, 132], [570, 219], [585, 101], [600, 180], [615, 290], [630, 154], [645, 348], [660, 45], [675, 18], [690, 132], [705, 221], [720, 136], [735, 172], [750, 233], [765, 26], [780, 211], [795, 7], [810, 1], [825, 1], [840, 106], [855, 288], [870, 251], [885, 437], [900, 437]];
    //var yListe = [[25, 44, 373, 220, 189, 200, 165, 258, 251, 157, 113, 360, 234, 374, 959, 630, 391, 7, 348, 155, 131, 220, 229, 257, 576, 124, 220, 670, 374, 199, 111, 219, 134, 208, 180, 110, 132, 219, 101, 180, 290, 154, 348, 45, 18, 132, 221, 136, 172, 233, 26, 211, 7, 1, 1, 106, 288, 251, 437, 437]];
    var curve = [];
    var yListe = [];
    var maxY = 959;
    var un_niveau = 959/19;
    var timeCheck;

    var posx = 0;
    var posy = 0;


    var posxSuivant = 0;
    var posySuivant = 0;

    var graphics;

    var mijnDelayTimer;

    var i = 0;

    //nergens gebruikt ?
    var nodeList = new Array();
    var curveSprite;
    var slider;
    var lijn;
    var nodes;
    var laatsteFoto = "";
    var tekeningBezig;
    var beginpositieSlider;
     var beginpositieGraphics;
     var Sound;
     var music;
     //var muziekBezig;
     var node_highlight;
     var retry;
     var tekst;
     var style;
     var schaal;



};

Fitbit.Game.prototype = {

    create: function () {
        console.log("game create");
        //console.log(lines);
         //maxY = 959;
        //maxY = arrayMax(lines); //maxY moet veranderd naar 400 (100%) en alle andere waarden moeten daaraan aangepast
        //lines est une variable globale, défini en OpenFile
        maxY = lines.reduce(function(previous,current){
                      return previous > current ? previous:current
                   });

        //console.log("maxY :");
        //console.log(maxY);

        schaal = 400/maxY; //om y waarden te herleiden naar hoogte 400 van scherm
        //de nieuwe maxY
        maxY = parseInt(maxY * schaal);
        //doe het ook voor alle y waarden
        for (var p=0; p<lines.length; p++)
        {
            lines[p] = parseInt(lines[p] * schaal);
            lines[p] = 400 - lines[p];

        }

        //un_niveau = 959/19;
        un_niveau = maxY/19;


        var xListe = [];
        for (i = 0; i< lines.length ;i++)
        {
            xListe.push(i*15);
        }

        yListe = [];
        yListe.push(lines); //push een array in een leeg array

        curve = this.zip(xListe, lines);
        //console.log("geschaalde curve:")
        //console.log(curve);
        //curve = [[15, 25], [30, 44], [45, 373], [60, 220], [75, 189], [90, 200], [105, 165], [120, 258], [135, 251], [150, 157], [165, 113], [180, 360], [195, 234], [210, 374], [225, 959], [240, 630], [255, 391], [270, 7], [285, 348], [300, 155], [315, 131], [330, 220], [345, 229], [360, 257], [375, 576], [390, 124], [405, 220], [420, 670], [435, 374], [450, 199], [465, 111], [480, 219], [495, 134], [510, 208], [525, 180], [540, 110], [555, 132], [570, 219], [585, 101], [600, 180], [615, 290], [630, 154], [645, 348], [660, 45], [675, 18], [690, 132], [705, 221], [720, 136], [735, 172], [750, 233], [765, 26], [780, 211], [795, 7], [810, 1], [825, 1], [840, 106], [855, 288], [870, 251], [885, 437], [900, 437]];
        //yListe = [[25, 44, 373, 220, 189, 200, 165, 258, 251, 157, 113, 360, 234, 374, 959, 630, 391, 7, 348, 155, 131, 220, 229, 257, 576, 124, 220, 670, 374, 199, 111, 219, 134, 208, 180, 110, 132, 219, 101, 180, 290, 154, 348, 45, 18, 132, 221, 136, 172, 233, 26, 211, 7, 1, 1, 106, 288, 251, 437, 437]];


        nodeListe = [];
        posx = 0;
        posy = 0;


        posxSuivant = 0;
        posySuivant = 0;

        tekeningBezig = true;

        imageSize = 250;
        laatsteFoto = "";
        beginpositieSlider = 0;
        beginpositieGraphics = 0;

        music = this.add.audio('titleMusic');

        if (muziekBezig == 1) {
            console.log("muziekbezig");
            console.log(muziekBezig);
            music.loop = true;
            music.play();
            //muziekBezig = 1;      //maintenant initalisé comme variable globale en OpenFile.js
            sound = this.game.add.sprite(800, 0, "sound");
        } else {
            console.log("muziek niet bezig");
            console.log(muziekBezig);
            sound = this.game.add.sprite(800, 0, "soundOff");
        }
        sound.inputEnabled = true;
        sound.input.useHandCursor = true;
        sound.events.onInputDown.add(this.soundButton, this);


        i = 0;

        //container voor curve en nodes
        graphics = this.add.graphics(0, 0);


        rail = this.add.graphics(0, 0);
        rail.lineStyle(3, 0xFFFFFF);
        rail.moveTo(0,430);                  //20 is de helft van de breedte van hand icon
        rail.lineTo(1200, 430);

        //slider als lege container die hand en vertikale rode lijn gaat bevatten
        slider = this.game.add.sprite(0,0, null);
        slider.anchor.setTo(0.5, 0.5);
        hand = this.game.add.sprite(0, 410, "hand");
        hand.anchor.setTo(0.5, 0);
        lijn = this.game.add.sprite(0, 0, "cursor");
        lijn.anchor.setTo(0.5, 0);
        //parenting
        slider.addChild(lijn);
        slider.addChild(hand);

        slider.inputEnabled = true;
        slider.input.enableDrag();
        slider.input.allowVerticalDrag = false;

        slider.events.onDragStart.add(this.startDrag, this);
        slider.events.onDragStop.add(this.stopDrag, this);

        nodes = this.game.add.group();


        retry = this.game.add.sprite(800, 320, "retry");
        retry.inputEnabled = true;
        retry.input.useHandCursor = true;
        retry.events.onInputDown.add(this.recommencer, this);

        style = {font: "24px Arial", fill: "#ff0044", wordWrap: true, wordWrapWidth: 80, align: "center" };

        tekst = this.game.add.text(0, 0, "", style);


        //plaats hem eerst buiten veld
        node_highlight = this.game.add.sprite(-10,-10, "node_highlight");
        node_highlight.anchor.setTo(0.5, 0.5);
        graphics.addChild(node_highlight);      //om samen met graphics te verschuiven

        curveGenerator = this.game.time.events.loop(Phaser.Timer.SECOND * 0.15, this.tekenCurve, this, curve);
        curveGenerator.timer.start();

    },

    zip: function () {
        for (var b = 0; b < arguments.length; b++) {
            if (!arguments[b].length || !arguments.toString()) {
                return false;
            }
            if (b >= 1) {
                if (arguments[b].length !== arguments[b - 1].length) {
                    return false;
                }
            }
        }
        var zipped = [];
        for (var f = 0; f < arguments[0].length; f++) {
            var toBeZipped = [];
            for (var k = 0; k < arguments.length; k++) {
                toBeZipped.push(arguments[k][f]);
            }
            zipped.push(toBeZipped);
        }
        return zipped;
    },



    startDrag: function(){
        //voorkomt dat programma tegelijk overlap en click nodes tracht te verwerken: beeldje switcht heen en weer bij klik
        tekeningBezig = false;

    },

    stopDrag: function(){
        tekeningBezig = true;
    },

    soundButton: function(){
        if (muziekBezig == 1) {
            music.stop();
            sound = this.game.add.sprite(800, 0, "soundOff");


        } else if (muziekBezig == -1){
            music.play();
            sound = this.game.add.sprite(800, 0, "sound");
        }
        muziekBezig = - muziekBezig;

    },

    recommencer:function() {
        if (muziekBezig == 1) {
            music.stop(); //sinon deux versions se superposent
            //muziekBezig = - muziekBezig;
        }
        //sound = this.game.add.sprite(800, 0, "sound");
        this.state.start('Game');

    },


    tekenCurve: function(c) {
        var lengte = c.length;
		if (i<lengte-1) {
		    posx = c[i][0];
		    posy = c[i][1];

		    posxSuivant = c[i+1][0];
		    posySuivant = c[i+1][1];
		    //teken stuk van de curve
		    graphics.lineStyle(3, 0x00FF00);
		    graphics.moveTo(posx,posy);
		    graphics.lineTo(posxSuivant, posySuivant);

		    //scroll één x eenheid naar links als curve meer dan 800 pixels breed wordt

            if (i == 0){
                posxSuivant = posx;
                posySuivant = posy;

            }
            node = this.game.add.sprite(posxSuivant, posySuivant, 'node');
            node_highlight.x = posxSuivant;
            node_highlight.y = posySuivant;

            //graphics.addChild(node);
            node.anchor.setTo(0.5, 0.5);     //om centrum van node als xy te hebben

            node.inputEnabled = true;
            node.input.useHandCursor = true;

            node.name = "node" + i;

            node.events.onInputDown.add(this.clickBox, this);
            nodes.add(node);

            //toon beeldje naargelang node.y
            this.kiesBeeldje(node);
            //console.log(node.y);

            //als curve midden van scherm bedekt beginnen we ze naar links te verschuiven
            if (posx > 500)
			{
			    graphics.x -= 15;
			    nodes.x -= 15;


			    //slider gaat de andere kant uit
			    slider.x = nodes.x + ((i+2) * 15);


			} else {
                slider.x = node.x;
			}

            i += 1;
        }else{
            curveGenerator.timer.stop();
            tekeningBezig = false;
            //nodig voor scratch
            beginpositieSlider = slider.x;
            beginpositieGraphics = graphics.x;

            graphics.addChild(tekst);


        }

	},


	 checkOverlap: function(node, lijn) {
        //console.log("check overlap");
        var boundsA = lijn.getBounds();
        var boundsB = node.getBounds();

        geraakt = Phaser.Rectangle.intersects(boundsA, boundsB);
        if ((geraakt == true) && (node.name != this.laatsteFoto)){
            //console.log("intersectie");
            //console.log(node.name);
            //laatsteFoto = node.name;
            //if(fotoGetoond == false){
            if (laatsteFoto != node.name) {
                //console.log("toon de foto ");

                //toonZe(node.name);
                this.kiesBeeldje(node);
                //foto = this.game.add.sprite(300, 0, node.name);
                if (tekeningBezig == false){
                    node_highlight.x = node.x;
                    node_highlight.y = node.y;
                }

                 var omkeringY = -(node.y - 400);
                    tekst.text = parseInt(omkeringY/schaal) + " steps";   //herstel schaal
                    tekst.x = node.x + 10;
                    tekst.y = node.y;

            }

        } else {

            laatsteFoto = node.name;
        }


    },


    clickBox: function(node, pointer)
    {
        console.log("geklikt");
        console.log(node.name);
        //console.log(node.y);
        this.kiesBeeldje(node);
        node_highlight.x = node.x;
        node_highlight.y = node.y;
        var omkeringY = -(node.y - 400);
        tekst.text = parseInt(omkeringY/schaal) + " steps";   //herstel schaal
        tekst.x = node.x + 10;
        tekst.y = node.y;



    },

    kiesBeeldje: function(node){
        var niv = node.y/19;
        //console.log(niv);
        if (niv > 18){
            this.game.add.sprite(10, 10, "img19");
        } else if (niv > 17){
            this.game.add.sprite(10, 10, "img18");
        } else if (niv > 16){
            this.game.add.sprite(10, 10, "img17");
        } else if (niv > 15){
            this.game.add.sprite(10, 10, "img16");
        } else if (niv > 14){
            this.game.add.sprite(10, 10, "img15");
        } else if (niv > 13){
            this.game.add.sprite(10, 10, "img14");
        } else if (niv > 12){
            this.game.add.sprite(10, 10, "img13");
        } else if (niv > 11){
            this.game.add.sprite(10, 10, "img12");
        } else if (niv > 10){
            this.game.add.sprite(10, 10, "img11");
        } else if (niv > 9){
            this.game.add.sprite(10, 10, "img10");
        } else if (niv > 8){
            this.game.add.sprite(10, 10, "img9");
        } else if (niv > 7){
            this.game.add.sprite(10, 10, "img8");
        } else if (niv > 6){
            this.game.add.sprite(10, 10, "img7");
        } else if (niv > 5){
            this.game.add.sprite(10, 10, "img6");
        } else if (niv > 4){
            this.game.add.sprite(10, 10, "img5");
        } else if (niv > 3){
            this.game.add.sprite(10, 10, "img4");
        } else if (niv > 2){
            this.game.add.sprite(10, 10, "img3");
        } else if (niv > 1){
            this.game.add.sprite(10, 10, "img2");
        } else if (niv > 0){
            this.game.add.sprite(10, 10, "img1");
        } else {
            this.game.add.sprite(10, 10, "img0");
        }


    },


    render: function() {
        //checkOverlap(slider, node1);
        //console.log("render")
        if (tekeningBezig == false) {
            nodes.forEach(function(item) {
            //        console.log("doe iets");
            //        console.log(item.name);
                    this.checkOverlap(item, lijn);
            }, this);
        }

                    //bv. 300
        if (tekeningBezig == false) {
            verschuiving = slider.x - beginpositieSlider;       // -100

            graphics.x = beginpositieGraphics - verschuiving;    //min omdat we de andere richting uitmoeten
            nodes.x = graphics.x;
        }

         //this.graphics = this.add.graphics(0, 0);
        this.game.world.bringToTop(graphics);
        //this.game.world.bringToTop(this.curveSprite);
        this.game.world.bringToTop(nodes);
        this.game.world.bringToTop(slider);
        this.game.world.bringToTop(node_highlight);
        this.game.world.bringToTop(tekst);


    },



    update: function () {

        //  Honestly, just about anything could go here. It's YOUR game after all. Eat your heart out!
        //this.nodes.forEach(function(item) {
        //    checkOverlap(item, slider);
        //    //game.physics.arcade.collide(item, platforms);
        //    //game.physics.arcade.overlap(player, item, gameOver);
        //    //item.body.velocity.x = -120;
        //}, this);

    },

    quitGame: function (pointer) {

        //  Here you should destroy anything you no longer need.
        //  Stop music, delete sprites, purge caches, free resources, all that good stuff.

        //  Then let's go back to the main menu.
        this.state.start('MainMenu');

    }

};
